import os
import datetime
import frontmatter
import re
import shutil
import sys
import io

# Set encoding for standard streams to UTF-8 to prevent encoding crashes on Windows console
if sys.platform.startswith('win'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# --- CONFIGURATION PATHS ---
OBSIDIAN_POSTS_DIR = r"D:\Vault\Sammy.Decimal\80-89 🦋 Documents\86 Writing"
OBSIDIAN_IMAGES_DIR = r"D:\Vault\Sammy.Decimal\90-99 🐙 Archives\98 Digital Archives"
JEKYLL_POSTS_DIR = "./_posts" 
JEKYLL_IMAGES_DIR = "./_assets/images"

def process_images(markdown_content: str) -> str:
    """Finds ![[image]] tags, copies the files from Obsidian images folder to Jekyll _assets/images, 
    and replaces tags with standard markdown image links.
    """
    # Pattern matches ![[filename.ext]] or ![[filename.ext|width]]
    pattern = r'!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]'
    
    def replace_match(match):
        original_filename = match.group(1).strip()
        filename_lower = original_filename.lower()
        
        # Look for the file in the Obsidian images folder
        src_path = os.path.join(OBSIDIAN_IMAGES_DIR, original_filename)
        
        # If not found directly, do a case-insensitive check in the folder
        if not os.path.exists(src_path):
            src_path = None
            if os.path.exists(OBSIDIAN_IMAGES_DIR):
                for f in os.listdir(OBSIDIAN_IMAGES_DIR):
                    if f.lower() == filename_lower:
                        src_path = os.path.join(OBSIDIAN_IMAGES_DIR, f)
                        break
        
        if src_path and os.path.exists(src_path):
            # Generate a URL-safe destination filename
            base_name = os.path.basename(src_path)
            name_part, ext_part = os.path.splitext(base_name)
            safe_name = name_part.lower().replace(" ", "-").replace("_", "-")
            # Remove characters that aren't letters, numbers, or hyphens
            safe_name = re.sub(r'[^a-z0-9\-]', '', safe_name)
            safe_filename = f"{safe_name}{ext_part.lower()}"
            
            os.makedirs(JEKYLL_IMAGES_DIR, exist_ok=True)
            dest_path = os.path.join(JEKYLL_IMAGES_DIR, safe_filename)
            
            # Copy the file
            try:
                shutil.copy2(src_path, dest_path)
                print(f"📸 Copied image: '{original_filename}' -> '{dest_path}'")
                # Return standard markdown image syntax pointing to the copied asset
                return f"![{original_filename}](/_assets/images/{safe_filename})"
            except Exception as e:
                print(f"⚠️ Failed to copy image {original_filename}: {str(e)}")
                return match.group(0) # Keep original if copy failed
        else:
            print(f"⚠️ Image not found in Obsidian images folder: '{original_filename}'")
            return match.group(0) # Keep original
            
    return re.sub(pattern, replace_match, markdown_content)

def publish_to_jekyll(title: str, clean_markdown: str, metadata: dict) -> bool:
    """Saves the content right into the Jekyll compilation pipeline."""
    try:
        date_str = datetime.date.today().strftime("%Y-%m-%d")
        safe_title = title.lower().replace(" ", "-").replace('"', '').replace("'", "")
        file_name = f"{date_str}-{safe_title}.md"
        file_path = os.path.join(JEKYLL_POSTS_DIR, file_name)
        
        post = frontmatter.Post(clean_markdown)
        post['layout'] = 'post'
        post['title'] = title
        post['date'] = date_str
        post['tags'] = metadata.get("tags", [])
        
        os.makedirs(JEKYLL_POSTS_DIR, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            frontmatter.dump(post, f)
            
        print(f"🎉 Successfully generated Jekyll file: {file_name}")
        return True
    except Exception as e:
        print(f"❌ Error writing to Jekyll: {str(e)}")
        return False

def flag_note_as_published(file_path: str, post_data):
    """Updates the original Obsidian note frontmatter so it is never re-published."""
    post_data['status'] = 'done-publishing'
    post_data['published_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        frontmatter.dump(post_data, f)
    print(f"📝 Marked local file '{os.path.basename(file_path)}' as published.")

def run_pipeline():
    print(f"🛰️ Scanning directory: {OBSIDIAN_POSTS_DIR}")
    
    if not os.path.exists(OBSIDIAN_POSTS_DIR):
        print(f"❌ Error: The path '{OBSIDIAN_POSTS_DIR}' does not exist. Please check your folder naming.")
        return

    processed_count = 0

    for root, _, files in os.walk(OBSIDIAN_POSTS_DIR):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    # Skip parsing our own API file if it happens to sit in a scanned path branch
                    if file == "api.md":
                        continue
                        
                    post = frontmatter.load(file_path)
                    
                    if post.get('status') == 'publish' and 'published_at' not in post.metadata:
                        print(f"\n✨ New article draft discovered: {file}")
                        
                        title = post.get('title', file.replace('.md', ''))
                        raw_content = post.content
                        
                        # 1. Process and copy images
                        processed_content = process_images(raw_content)
                        
                        # 2. Output to Jekyll static folder build array
                        success = publish_to_jekyll(title, processed_content, post.metadata)
                        
                        # 3. Alter frontmatter locally to seal it
                        if success:
                            flag_note_as_published(file_path, post)
                            processed_count += 1
                            
                except Exception as e:
                    print(f"⚠️ Failed reading file {file}: {str(e)}")
                    
    if processed_count == 0:
        print("😴 No new notes marked 'status: publish' found. Everything is up to date!")

if __name__ == "__main__":
    run_pipeline()