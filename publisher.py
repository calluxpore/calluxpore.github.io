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

def clean_alt_text(filename: str) -> str:
    """Helper to clean a filename and generate a readable image alt text."""
    name_part, _ = os.path.splitext(filename)
    clean_name = name_part.replace('_', ' ').replace('-', ' ')
    clean_name = re.sub(r'\s+', ' ', clean_name).strip()
    return clean_name.capitalize()

def process_images(markdown_content: str) -> str:
    """Finds ![[image]] tags, copies the files from Obsidian images folder to Jekyll _assets/images, 
    and replaces tags with standard markdown image links. Handles optional alt text or width.
    """
    # Pattern matches ![[filename.ext]] or ![[filename.ext|alt_text_or_width]]
    pattern = r'!\[\[([^\]|]+)(?:\|([^\]]*))?\]\]'
    
    def replace_match(match):
        original_filename = match.group(1).strip()
        alt_or_width = match.group(2).strip() if match.group(2) else ""
        filename_lower = original_filename.lower()
        
        # Check if alt_or_width is a width number (e.g., 300, 300x200)
        is_width = bool(re.match(r'^\d+(?:x\d+)?$', alt_or_width))
        
        if alt_or_width and not is_width:
            alt_text = alt_or_width
        else:
            alt_text = clean_alt_text(original_filename)
            
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
                return f"![{alt_text}](/_assets/images/{safe_filename})"
            except Exception as e:
                print(f"⚠️ Failed to copy image {original_filename}: {str(e)}")
                return match.group(0) # Keep original if copy failed
        else:
            print(f"⚠️ Image not found in Obsidian images folder: '{original_filename}'")
            return match.group(0) # Keep original
            
    return re.sub(pattern, replace_match, markdown_content)


def generate_description(content: str, max_len: int = 155) -> str:
    """Auto-generates a clean plain text meta description from markdown content."""
    # 1. Remove code blocks
    text = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    
    # 2. Remove wiki image links ![[...]]
    text = re.sub(r'!\[\[.*?\]\]', '', text)
    
    # 3. Remove standard image links ![alt](url)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    
    # 4. Replace standard markdown links [text](url) with just text
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    
    # 5. Remove headers completely (lines starting with #)
    text = re.sub(r'(?m)^#+.*$', '', text)
    
    # 6. Remove bullet/numbered list markers at start of lines
    text = re.sub(r'(?m)^[-*+]\s+', '', text)
    text = re.sub(r'(?m)^\d+\.\s+', '', text)
    
    # 7. Remove blockquote markers at start of lines
    text = re.sub(r'(?m)^>\s*', '', text)
    
    # 8. Remove bold/italic/code markers
    text = re.sub(r'\*\*|__|\*|_|`', '', text)
    
    # 9. Clean up whitespace and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    
    if not text:
        return ""
        
    if len(text) <= max_len:
        return text
        
    truncated = text[:max_len]
    last_space = truncated.rfind(' ')
    if last_space > max_len - 20:
        truncated = truncated[:last_space]
        
    return truncated.strip() + "..."

def publish_to_jekyll(title: str, clean_markdown: str, metadata: dict) -> bool:
    """Saves the content right into the Jekyll compilation pipeline."""
    try:
        date_str = datetime.date.today().strftime("%Y-%m-%d")
        safe_title = title.lower().replace(" ", "-").replace("_", "-")
        # Remove characters that aren't letters, numbers, or hyphens
        safe_title = re.sub(r'[^a-z0-9\-]', '', safe_title)
        # Collapse multiple hyphens and strip leading/trailing hyphens
        safe_title = re.sub(r'-+', '-', safe_title).strip('-')
        file_name = f"{date_str}-{safe_title}.md"
        file_path = os.path.join(JEKYLL_POSTS_DIR, file_name)
        
        post = frontmatter.Post(clean_markdown)
        post['layout'] = 'post'
        post['title'] = title
        post['date'] = date_str
        
        # Handle categories (mapping tags to categories and deduplicating)
        categories = []
        if 'tags' in metadata:
            tags_val = metadata['tags']
            if isinstance(tags_val, list):
                categories.extend(tags_val)
            elif isinstance(tags_val, str):
                categories.append(tags_val)
        if 'categories' in metadata:
            cats_val = metadata['categories']
            if isinstance(cats_val, list):
                categories.extend(cats_val)
            elif isinstance(cats_val, str):
                categories.append(cats_val)
        
        # De-duplicate while preserving order
        unique_categories = []
        for cat in categories:
            if cat not in unique_categories:
                unique_categories.append(cat)
                
        if unique_categories:
            post['categories'] = unique_categories
            
        # Add description for SEO optimization
        description = metadata.get('description', '').strip()
        if not description:
            description = generate_description(clean_markdown)
        if description:
            post['description'] = description
                
        # Resolve and copy frontmatter image if specified
        if 'image' in metadata and metadata['image']:
            raw_img_path = str(metadata['image']).strip()
            # Strip wiki-link syntax [[image.png]] if present
            raw_img_path = re.sub(r'^\[\[(.*)\]\]$', r'\1', raw_img_path).strip()
            
            src_path = os.path.join(OBSIDIAN_IMAGES_DIR, raw_img_path)
            if not os.path.exists(src_path):
                src_path = None
                if os.path.exists(OBSIDIAN_IMAGES_DIR):
                    for f in os.listdir(OBSIDIAN_IMAGES_DIR):
                        if f.lower() == raw_img_path.lower():
                            src_path = os.path.join(OBSIDIAN_IMAGES_DIR, f)
                            break
            
            if src_path and os.path.exists(src_path):
                base_name = os.path.basename(src_path)
                name_part, ext_part = os.path.splitext(base_name)
                safe_name = name_part.lower().replace(" ", "-").replace("_", "-")
                safe_name = re.sub(r'[^a-z0-9\-]', '', safe_name)
                safe_filename = f"{safe_name}{ext_part.lower()}"
                
                os.makedirs(JEKYLL_IMAGES_DIR, exist_ok=True)
                dest_path = os.path.join(JEKYLL_IMAGES_DIR, safe_filename)
                
                try:
                    shutil.copy2(src_path, dest_path)
                    print(f"📸 Copied frontmatter image: '{raw_img_path}' -> '{dest_path}'")
                    post['image'] = f"/_assets/images/{safe_filename}"
                except Exception as e:
                    print(f"⚠️ Failed to copy frontmatter image {raw_img_path}: {str(e)}")
                    post['image'] = raw_img_path
            else:
                # If image starts with a web URL or is already resolved, keep as is
                if raw_img_path.startswith('/') or raw_img_path.startswith('http'):
                    post['image'] = raw_img_path
                else:
                    print(f"⚠️ Frontmatter image not found in Obsidian images folder: '{raw_img_path}'")
                    post['image'] = raw_img_path

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