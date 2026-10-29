---
name: Mind Palace
description: A type specimen of one research practice; every essay is a numbered entry on a visible construction grid.
colors:
  paper: "#ffffff"
  sheet: "#ffffff"
  ink: "#111111"
  ink-muted: "#4f5764"
  crouwel-blue: "#0057ff"
  crouwel-blue-ink: "#0047d6"
  grid-line: "#e2e9f6"
  rule-soft: "#c9d6f0"
  signal-orange: "#ff4f1f"
  signal-ink: "#111111"
  surface: "#f5f7fa"
  code-text: "#b0300c"
  cell-level-0: "#edf1f8"
  cell-level-1: "#b9cdf7"
  cell-level-2: "#6f99f2"
  cell-level-3: "#2c69ec"
  cell-level-4: "#0040b8"
  dark-paper: "#0b0d12"
  dark-sheet: "#0f1219"
  dark-ink: "#e9edf5"
  dark-ink-muted: "#9aa4b5"
  dark-blue: "#6b98ff"
  dark-blue-ink: "#8eb0ff"
  dark-rule: "#3f74ff"
  dark-signal-orange: "#ff6a3d"
  dark-surface: "#151a24"
typography:
  display:
    fontFamily: "Chakra Petch, Atkinson Hyperlegible, system-ui, sans-serif"
    fontSize: "clamp(36px, 5vw, 60px)"
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "-0.015em"
  headline:
    fontFamily: "Chakra Petch, Atkinson Hyperlegible, system-ui, sans-serif"
    fontSize: "28px"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0.01em"
  title:
    fontFamily: "Chakra Petch, Atkinson Hyperlegible, system-ui, sans-serif"
    fontSize: "28px"
    fontWeight: 600
    lineHeight: 1.12
  body:
    fontFamily: "Atkinson Hyperlegible, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.68
  body-ui:
    fontFamily: "Atkinson Hyperlegible, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Chakra Petch, Atkinson Hyperlegible, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 600
    letterSpacing: "0.06em"
  numeral-index:
    fontFamily: "Chakra Petch, Atkinson Hyperlegible, system-ui, sans-serif"
    fontSize: "34px"
    fontWeight: 700
    lineHeight: 1
    fontFeature: "tnum"
  code:
    fontFamily: "MonoLisa, Consolas, Monaco, monospace"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.55
rounded:
  none: "0px"
spacing:
  cell: "40px"
  cell-mobile: "24px"
  cell-2: "80px"
  cell-3: "120px"
  inset: "16px"
components:
  button:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.crouwel-blue}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0 14px 0 18px"
    height: "40px"
    width: "200px"
  button-primary:
    backgroundColor: "{colors.signal-orange}"
    textColor: "{colors.signal-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0 14px 0 18px"
    height: "40px"
    width: "200px"
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  filter-cell:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.crouwel-blue}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0 16px"
    height: "40px"
  filter-cell-active:
    backgroundColor: "{colors.signal-orange}"
    textColor: "{colors.signal-ink}"
  tool-button:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.crouwel-blue}"
    rounded: "{rounded.none}"
    width: "40px"
    height: "38px"
  tool-button-pressed:
    backgroundColor: "{colors.crouwel-blue}"
    textColor: "{colors.paper}"
  play-button:
    backgroundColor: "{colors.signal-orange}"
    textColor: "{colors.signal-ink}"
    rounded: "{rounded.none}"
    width: "80px"
    height: "80px"
  nav-link:
    textColor: "{colors.crouwel-blue}"
    typography: "{typography.label}"
    padding: "6px 0"
---

# Design System: Mind Palace

## Overview

**Creative North Star: "The Grid Specimen"**

The blog is a type specimen of one research practice. A visible construction grid, drawn in pale Crouwel-blue hairlines on a white sheet, holds every page; each essay is a numbered entry placed on it. Structure is spoken in blue (rules, links, numerals in the index), the reader's text sits in near-black ink, and one plane of signal orange marks the single thing to act on. Nothing is rounded, nothing floats, nothing is shadowed: depth comes from rules and from the paper the reading column is cut out of.

The voice is Swiss and engineered rather than editorial-soft. Chakra Petch, a chamfered grid-built face, carries labels, numerals, the masthead and essay titles; Atkinson Hyperlegible carries every reading line. The one permitted rebellion is a single diagonal stroke (bottom-left to top-right) that recurs as the slash in the masthead, the arrow in buttons, the giant diagonal beside the hero numeral, and the blockquote mark.

The signature is the cell-built numeral: the newest essay's number assembled from whole grid cells, 5 by 7 per digit, with its last cell lit orange. The grid itself is real state, not decoration; readers can switch it off and the choice persists.

**Key Characteristics:**
- 40px construction grid (24px under 720px), centred so 31-cell and 17-cell columns land on its lines.
- Square corners everywhere; 1px blue structural rules, 2px ink rules under section heads.
- One accent plane: signal orange, always carrying ink text when it carries text.
- Chakra Petch caps for labels, Chakra Petch mixed case for titles, Atkinson Hyperlegible for reading.
- Cell-built 5x7 numerals with one orange terminal cell.
- Light and dark themes are full token swaps, not filters.

## Colors

A cold white sheet ruled in Crouwel blue, inked near-black, with one hot orange signal.

### Primary
- **Crouwel Blue** (crouwel-blue): the structural voice. Header and footer rules, panel borders, links, nav links, index numerals, the slash, list markers, pressed tool buttons and the active year cell. Hover on blue text resolves to ink, not to a deeper blue. In dark mode it lifts to dark-blue for text and dark-rule for structure.
- **Blue Ink** (crouwel-blue-ink): the deeper blue kept as the legacy accent-hover alias; rarely seen.

### Secondary
- **Signal Orange** (signal-orange): the single accent plane. As a filled plane it appears only on the primary button, the active category filter cell, the play button, the skip link and text selection, and it always carries signal-ink text. As a mark it appears only as thin signals: the 2px active-nav underline, the 3px reading progress bar, the hover outline on calendar cells, and the one terminal cell of a cell-built numeral. Dark mode uses dark-signal-orange with dark-paper text.

### Neutral
- **Paper** (paper / dark-paper): the page and the cut-out behind the reading column and lists.
- **Sheet** (sheet / dark-sheet): resting fill of buttons, filter cells, panels and nav cards. Identical to paper in light mode; one step up in dark.
- **Ink** (ink / dark-ink): headings, body text, 2px section-head rules, and the hover state of every orange or blue control.
- **Muted Ink** (ink-muted / dark-ink-muted): metadata, excerpts, dates, the contents column at rest.
- **Grid Hairline** (grid-line): the construction grid only. In dark mode it is dark-blue at 11% alpha.
- **Soft Rule** (rule-soft): secondary 1px dividers between index rows, filter cells, table rows and image frames; also the "/" before category tags. Dark: dark-blue at 26% alpha.
- **Surface** (surface / dark-surface): code blocks, inline code and empty image frames.
- **Code Rust** (code-text): inline code and function names in highlighted code.

### Calendar Ramp
- **Cell levels 0 to 4** (cell-level-0 through cell-level-4): a five-step blue ramp for the publishing calendar and its legend. Dark mode inverts it so higher activity reads lighter. Future days are an inset 1px level-0 outline, not a fill.

### Named Rules
**The One Plane Rule.** Signal orange is the only accent fill on any screen, and a filled orange plane always carries ink text (signal-ink), never white.

**The Blue Is Structure Rule.** Blue marks structure and navigation: rules, links, numerals, borders. It is never used as a large decorative fill; its only fills are pressed or active controls.

**The Ink Hover Rule.** Interactive blue and orange resolve to ink on hover (orange planes invert to ink with paper text).

## Typography

**Display Font:** Chakra Petch (with Atkinson Hyperlegible, system-ui)
**Body Font:** Atkinson Hyperlegible (with system-ui, Segoe UI)
**Label/Mono Font:** Chakra Petch caps for labels; MonoLisa for code only

**Character:** A chamfered, grid-built technical face for everything that labels, numbers or names, set against a warm, highly legible humanist sans for everything that is read. All three faces are self-hosted from /_fonts and the display/body weights are preloaded.

### Hierarchy
- **Display** (700, clamp(36px, 5vw, 60px), 1.02, -0.015em): essay and page titles in mixed case; the home feature title uses clamp(36px, 4.2vw, 60px) at line-height 1.
- **Headline** (700, 28px, uppercase, 0.01em): section heads such as the essay index and the publishing record; related reading at 22px.
- **Title** (600, 28px, 1.12): index entry titles, mixed case; 22px under 720px. Related and prev/next titles at 19 to 21px.
- **Body** (400, 19px, 1.68): the essay column, about 17 cells (680px) wide; 18px under 720px. Interface body is 18px / 1.6; standfirst and lead 20px / 1.5 at 56 to 66ch.
- **Label** (600, 13px, 0.06em, uppercase): metadata, dates, read time, category tags, player label, footer group titles. Nav links and buttons use the same voice at 15px.
- **Index Numeral** (700, 34px, tabular): the blue entry number in the left cell pair of each index row; 26px under 720px.
- **Code** (MonoLisa, 15px / 1.55 in blocks, 0.86em inline).

### Named Rules
**The Caps Are Metadata Rule.** Chakra caps label data (dates, counts, categories, controls) and section heads. They never sit above a heading as an eyebrow or kicker.

**The Mixed-Case Title Rule.** Essay titles stay mixed case in Chakra Petch for readability of long titles; only section heads and controls go uppercase.

**The Tabular Numbers Rule.** Every numeral in data (counts, dates, times, index numbers) uses tabular figures.

## Layout

One unit governs everything: the cell (40px; 24px under 720px). The construction grid is a background on the html element, sized to the cell and centred horizontally so the 31-cell content container (1240px) and the 17-cell reading column (680px) both land on grid lines. Spacing is expressed in cells: section padding is one cell, main padding two cells top and three bottom, the header is two cells tall, buttons are one cell tall and five cells wide.

The home page is a 31-column grid: the feature hero gives 13 columns to the cell-built numeral and its diagonal, and columns 15 to 31 to title, standfirst, meta and actions. Below, the index takes 22 columns and the sticky contents column takes columns 24 to 31 (shown only at 1100px and wider). Index rows are a two-cell numeral column plus a one-cell gap plus the text.

Essays sit in a 17-cell column on clean paper: the column and its one-cell paper halo blank out the grid so the grid stays in the margins. The post's cell-built numeral hangs two cells left of the column at half-cell size, and moves inline above the title under 900px.

Breakpoints: 1100px (contents column appears, index spans full width below), 900px (hero and intro stack, diagonal hidden, margin numeral goes inline, footer to two columns), 720px (cell shrinks to 24px, header unsticks and wraps, buttons grow to two cells tall and share the row, thumbnails hidden, footer single column).

The grid is persisted state: a pressed toolbar button and the G key toggle it, stored in localStorage and applied before first paint.

## Elevation & Depth

The system is flat. There are no drop shadows. Depth is conveyed by rules (1px blue for structure, 1px soft blue for subdivision, 2px ink under section heads) and by paper cut-outs: the reading column, lists and section heads paint paper over the grid so the grid reads as the layer beneath. The only box-shadow values are functional: a one-cell paper spread that extends the reading column's clean margin, and an inset 1px outline for future calendar days.

### Named Rules
**The Rules Not Shadows Rule.** Separate with a line or a paper cut-out, never with a shadow or a tonal card.

## Shapes

Every corner is square (0px), including range-slider thumbs and the graph page's panels, which are forced square by the stylesheet. The only round form is a graph node and its legend dot, because nodes are data points. Forms are built from whole cells: buttons, filter cells, tool buttons, the back-to-top button and the play button are one or two cells on a side. Groups of controls share borders instead of gaps (filter cells, tool group, year selector, prev/next).

The diagonal is the only non-orthogonal form: one stroke rising left to right, used as the masthead slash, the trailing arrow in buttons (it slides 3px right on hover), the tall hero diagonal beside the feature numeral, and the blockquote mark.

## Components

### Buttons
Rectangular one-cell bars that read like labelled fields on a form.
- **Shape:** square (0px), one cell tall, at least five cells wide, label left and slash right.
- **Default:** sheet fill, 1px blue border, blue Chakra caps 15px at 0.06em.
- **Primary:** signal orange fill and border with ink text. Used once per view for the main action (Read essay).
- **Hover / Focus:** default gains the soft blue wash and ink text; primary inverts to ink fill with paper text; the slash slides 3px right. Focus is a 2px blue outline offset 2px.
- **Tool buttons:** 40x38 icon cells in a shared 1px blue frame; pressed state is a blue fill with paper icon.

### Chips (category filter)
- **Style:** whole cells, one cell tall, sharing 1px soft-blue borders, sheet fill, blue Chakra caps 14px.
- **State:** active cell is signal orange with ink text; hover is the soft blue wash; the "+N more" toggle is muted ink.
- **Category tags in rows** are not chips: they are plain blue Chakra caps prefixed by a soft-blue "/".

### Index Rows
- Two-cell blue numeral, then title (Chakra 600), muted excerpt to 62ch, Chakra-caps meta with an Audio badge, and slash-prefixed category tags. Rows divide with 1px soft-blue rules and one cell of vertical padding. Optional 4x3-cell thumbnail in a soft-blue frame, zooming to 1.04 on hover. A row reached by anchor flashes the soft blue wash once.

### Contents Column
- Sticky at three cells from the top, headed by a 2px ink rule with a blue count. Entries grouped by month (muted caps 12px), 14px muted links with Chakra dates; hover and current entry turn blue, the current entry bold and underlined.

### Navigation
- **Top bar:** two cells tall, sticky, paper fill, 1px blue rule below. Masthead "SAMARTH REDDY / MIND PALACE" in Chakra caps 20px with the second half in blue. Nav links are blue Chakra caps 15px; the current page is ink with a 2px orange underline. Under 720px the bar unsticks and the nav wraps to its own line.
- **Footer:** 1px blue rule above; groups titled in caps over a 1px blue rule.

### Listen Player
- A 1px blue-framed panel. A two-cell square orange play button (ink icon) on the left; label, speed and volume to the right; 2px soft-blue range tracks with 12px square blue thumbs. Play inverts to ink on hover.

### Related and Prev/Next
- **Related:** a 2px ink-ruled head over rows of Chakra titles with caps meta on the right, divided by soft rules.
- **Prev/Next:** a 1px blue-framed two-slot grid; each slot is a sheet card with a blue caps label and a Chakra title, washing soft blue on hover. Collapses to one column when a slot is empty or under 720px.

### Publishing Calendar
- A 1px blue-framed panel: caps summary with a blue count, year selector as shared-border cells (active is blue with paper text), 11px square day cells on the five-step blue ramp with 3px gaps, and an orange outline on hover. Tooltip is an ink block with paper Chakra text.

### Cell-Built Numeral (signature)
- Digits drawn as 5x7 matrices of whole grid cells in ink, one cell column between digits, the final drawn cell lit signal orange. Full cell size in the home hero, half-cell size in the post margin. On load the cells assemble once (scale from 0.4 and fade, 14ms stagger, 0.5s ease-out), only when the page is visible and motion is allowed; cells are visible by default. A Chakra numeral fallback shows before the script runs.

### Reading Progress and Back to Top
- A 3px orange bar fixed to the top edge scales with scroll on essays. Back to top is a one-cell square, sheet fill, blue frame and chevron, inverting to blue on hover.

## Do's and Don'ts

### Do:
- **Do** size and space in cells (40px; 24px under 720px) and keep wide layouts on the 31-cell container and essays on the 17-cell column so both land on the grid.
- **Do** keep every corner square (0px) and separate with 1px blue or soft-blue rules, or a 2px ink rule under section heads.
- **Do** put ink text on every orange plane, and limit orange planes to the one primary action or active state in view.
- **Do** resolve blue and orange hovers to ink.
- **Do** set labels, dates and counts in Chakra Petch caps with tabular figures, and keep essay titles mixed case.
- **Do** carry every token in both themes; dark mode is its own palette, not an inversion.
- **Do** treat the grid toggle as real state: persisted, keyboard-reachable (G), applied before paint.
- **Do** respect reduced motion: numeral assembly and transitions collapse to instant.

### Don't:
- **Don't** round corners or use pill shapes, except data dots in the graph.
- **Don't** use drop shadows or tonal cards for depth.
- **Don't** put white text on signal orange or use orange as a decorative fill.
- **Don't** add a second accent hue to the interface.
- **Don't** place caps labels above headings as eyebrows or kickers.
- **Don't** introduce a second diagonal angle or decorative strokes beyond the one rising slash.
- **Don't** let the grid run behind the reading column; essays sit on clean paper.
- **Don't** use MonoLisa outside code.
