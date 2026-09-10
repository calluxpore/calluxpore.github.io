# calluxpore.github.io

Source for **[Samarth Reddy | Creative Technologist](https://calluxpore.github.io)** — a Jekyll blog
about designing for and with Artificial Intelligence.

## How a post gets published

Posts are written in Obsidian and pushed here by `publisher.py`. Nothing in `_posts/` is
edited by hand.

1. Write the note in the Obsidian vault (`80-89 Documents / 86 Writing`).
2. Set `status: publish` in the note's frontmatter.
3. Run the publisher:

   ```bash
   pip install -r requirements.txt
   python publisher.py
   ```

The publisher then:

- copies `![[image]]` attachments into `_assets/images/` with URL-safe names,
- **downscales anything wider than 1600 px** and writes a small WebP card thumbnail
  into `_assets/images/thumbs/` (used by the homepage),
- records the cover's `image_width` / `image_height` so pages reserve its space before it loads,
- generates a meta `description` that ends on a complete sentence,
- synthesises an `edge-tts` MP3 into `_assets/TTS/` (matched to the post by filename),
- writes the post to `_posts/` and marks the Obsidian note `status: done-publishing`
  so it is never republished.

Pillow is optional — without it images are copied unresized and everything else still works.

## Running the site locally

```bash
bundle install
bundle exec jekyll serve
```

## Layout

| Path | What it is |
| --- | --- |
| `_layouts/` | `default` (chrome), `post` (article), `page` |
| `assets/css/main.css` | the whole stylesheet — external so it caches across pages |
| `index.html` | post list, category filter, activity calendar |
| `graph.html` | d3 force-directed category graph (d3 loads only here) |
| `_assets/images/thumbs/` | generated WebP card thumbnails — do not edit by hand |
| `publisher.py` | the Obsidian → Jekyll pipeline |
