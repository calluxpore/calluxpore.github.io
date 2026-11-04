---
name: Mind Palace
description: You walk into the palace. A doorway opens to fill the screen, and each essay is a room with one memory in it.
colors:
  bg: "#ece9e2"
  surface: "#dfdcd2"
  ink: "#1c1c1c"
  muted: "#55564f"
  accent: "#46603f"
  accent-ink: "#ffffff"
  accent-text: "#3d5537"
  field: "#232322"
  field-ink: "#f1f1ef"
  room-4: "#d3d9cb"
  dark-bg: "#1c1c1c"
  dark-surface: "#262626"
  dark-ink: "#f1f1ef"
  dark-muted: "#b4b5b0"
  dark-accent: "#8fa68e"
  dark-accent-ink: "#1c1c1c"
  dark-accent-text: "#a8bea7"
  dark-field: "#c8c5ba"
  dark-field-ink: "#1c1c1c"
  dark-room-4: "#34392f"
typography:
  mega:
    fontFamily: "Big Shoulders, Impact, sans-serif"
    fontSize: "clamp(4.5rem, 10vw, 10rem)"
    fontWeight: 800
    lineHeight: 0.9
    textTransform: uppercase
  head:
    fontFamily: "Big Shoulders, Impact, sans-serif"
    fontSize: "clamp(2.75rem, 1.2rem + 6vw, 6.5rem)"
    fontWeight: 800
    lineHeight: 0.9
    textTransform: uppercase
  lead:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: "clamp(1.25rem, 1.1rem + 0.7vw, 1.625rem)"
    fontWeight: 400
    lineHeight: 1.3
  body:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: "clamp(1.0625rem, 1rem + 0.25vw, 1.1875rem)"
    fontWeight: 400
    lineHeight: 1.68
  small:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: "clamp(0.875rem, 0.85rem + 0.1vw, 0.9375rem)"
    fontWeight: 400
  code:
    fontFamily: "MonoLisa, Consolas, Monaco, monospace"
    fontSize: "15px"
rounded:
  none: "0px"
  image: "clamp(12px, 1.6vw, 24px)"
spacing:
  margin: "32px"
  margin-mobile: "20px"
---

# Design System: Mind Palace

## Overview

**Creative North Star: "The Doorway"**

The name is the idea. A mind palace is a building you walk through to find what you remembered, so the site is a building. The homepage opens on a small window onto `hero-doorway.jpg`, the window grows to fill the screen as you scroll, and past it each new essay is a room with its own ground colour. Essay pages continue the walk: their last section offers the related rooms and the room before and after.

The direction came from the taste skill (`design-taste-frontend`, direction `pinned-poster`), then adapted to this subject.

**Key characteristics:**
- One very large face and one plain reading face, with little in between.
- Whole fields of flat colour separate sections. There are no rules, cards, shadows or gradients.
- The essay covers are the colour. The interface stays quiet around them.
- Light and dark are full token swaps. The reader's system setting decides until they choose.

## Colour

Charcoal or stone holds the page, depending on the theme. Grey sage is the one accent.

- **Ground and surface** (`--bg`, `--surface`): the page, and one tone step up for controls and the footer.
- **Ink and muted** (`--ink`, `--muted`): running text is always full ink. Muted is for dates, counts and secondary notes.
- **Accent** (`--accent`, with `--accent-ink` on it): the primary button, the play button, the active filter and year, the reading progress bar and text selection. `--accent-text` is the version that is safe as a text colour.
- **Field** (`--field`, `--field-ink`): the inverse of the page, used once or twice per page, on the publishing record and on related rooms.
- **Room grounds** (`--room-1` to `--room-4`): the four newest essays take these in turn.
- **Calendar ramp** (`--cell-level-0` to `--cell-level-4`, `--cell-future`): tuned for the field it sits on, so it inverts between themes.

The graph page keeps its own node colours, because they mark clusters of data.

## Typography

**Big Shoulders** 800, always uppercase and always large, for titles and section heads. **Public Sans** for everything read, from 14px captions to the essay column. **MonoLisa** for code only. All are self-hosted from `/_fonts`.

Every headline holds to two lines at every width. Essay titles step down in size by length: over 24 characters take `.t-m`, over 40 take `.t-s`.

## Layout

A 12-column grid between one pair of equal margins: 32px on desktop, 20px under 900px. The space between sections is clearly larger than any space inside one, at about 120 to 180px on desktop. Every image, cover and essay box has rounded corners, all using `--radius`. Buttons, fields of colour and other controls stay square, and graph nodes stay round because they are data points. The doorway's corners flatten as it opens to fill the screen.

Breakpoints: 900px (rooms, essay heads and footer stack, and the doorway switches to its phone framing) and 720px (the header takes two rows, and the calendar scrolls sideways inside its own band, opening on the latest months).

## Motion

- **The signature:** the doorway opens with the scroll over one screen. The picture settles while the title and sentence fade. This uses `position: sticky` and never takes over the scroll.
- **Entrances:** parts of a section rise 24px and fade in, staggered by 70ms. Only what starts below the fold is held back, and only once the script runs, so nothing depends on it.
- **The frame:** the covers count up from the first essay to the newest, only while the frame is on screen.
- **Feedback:** every control responds to hover, press and focus.
- **Reduced motion:** the doorway stays as a still window, at normal page height, and nothing travels.

## Components

- **Room:** a full-width field with the title sticky on the left and the cover on the right. Stacks on a phone.
- **Essay box:** the full essay list is a grid of boxes: six across on a typical desktop, eight on very wide screens, two on a phone. Each box holds the cover, title, date, reading time and an audio button. The whole box links to the essay, and the audio button goes straight to the player.
- **Theme filter:** filled square buttons, most-used themes first, with the rest behind a text toggle. The URL hash holds the filter, so category links on essays land on a filtered list.
- **Publishing record:** a full-width calendar on the field, with a year selector, tooltips and a legend.
- **Listen player:** a surface panel with a large accent play button, seek, speed and volume. It always says the voice is AI.
- **Footer:** the name at nearly full width, then the description and two groups of links.

## Do's and Don'ts

**Do**
- Keep the doorway as the first thing a visitor sees, and the covers as the main source of colour.
- Carry every colour through the tokens, in both themes.
- Give every section a heading, and keep both outer margins equal.

**Don't**
- Add rules, outlined boxes, cards, shadows, gradients or glass.
- Round anything other than images, covers and the essay boxes that hold them, or use more than one radius.
- Add small uppercase labels, a label above a heading, or index numbers like 01 / 02 / 03. The covers already carry the numbers.
- Add a second accent colour, or use the display face below heading size.
- Use monospace outside code.
