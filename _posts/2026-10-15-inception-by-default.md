---
categories:
- Human Memory
- Artificial Intelligence
date: '2026-10-15'
description: A few months ago, I wrote about a strange unease. I had been feeding
  fragments of my childhood rooms into generative models, and the models kept filling…
image: /_assets/images/cover-020.jpg
image_height: 1264
image_width: 848
layout: post
title: Inception by Default
---

A few months ago, I wrote about a strange unease.

I had been feeding fragments of my childhood rooms into generative models, and the models kept filling the empty corners with polished wood and perfect amber light. Staring at one of those renders, I asked a question I could not answer: was this how I remembered the place, or was the model teaching me how to remember it?

At the time, it was only a feeling. A designer's hunch.

![Neon memory portrait montage](/_assets/images/neon-memory-portrait-montage.jpg)

Then I found a paper from the MIT Media Lab, co-authored by Elizabeth Loftus, the psychologist who spent five decades proving that human memory can be rewritten. Its title does not soften anything: _Synthetic Human Memories: AI-Edited Images and Videos Can Implant False Memories and Distort Recollection._

My hunch now had numbers.

## Hollywood got the method wrong

We have been telling ourselves stories about memory editing for decades.

In _Total Recall_, you walk into Rekall and buy a holiday you never took. In _Eternal Sunshine of the Spotless Mind_, a clinic erases an ex-lover from your head overnight. In _Inception_, a team of specialists descends through dreams within dreams to plant one idea so deep that the dreamer believes it was always his.

And in _Blade Runner_, Rachael holds out a photograph of herself as a little girl with her mother. It is her proof that her childhood happened. Deckard already knows the memories were implanted. The photograph was simply part of the kit.

These films share one assumption: rewriting a memory takes something heavy. A machine strapped to your head. A dream heist. A corporation with a lab.

Psychology has known for decades that it takes far less. In the 1990s, Loftus's "Lost in the Mall" study planted a whole childhood memory of getting lost while shopping in about a quarter of participants. In another study, a doctored photo of a childhood hot-air balloon ride led half of participants to recall, at least partly, a ride that never happened.

Rachael's photograph was the most realistic part of _Blade Runner_.

You do not need to implant a memory. You just need to hand someone a convincing picture.

## What the study did

The researchers showed 200 people in the United States the same 24 photographs: a wedding, sprinters on a track, a team group shot, an icy landscape, a vintage car under the mountains, a military parade, a quiet city street. Two minutes to look. Then two minutes of Pac-Man to clear the head.

Next, everyone saw the photos a second time, split into four groups of 50:

- **Originals.** The same unedited photos again.
- **AI-edited photos.** Half the images quietly changed with Photoshop's AI tools. A bride's neutral face became a smile. A stop sign appeared on the street. Open water on the ice was painted over with snow. Daylight became sunset.
- **AI videos of the originals.** The unedited photos turned into five-second clips.
- **AI videos of the edited photos.** The altered images, brought to life.

Every visual carried a label saying it had been enhanced. Nobody was told what had changed.

Finally, everyone answered questions about the _original_ photos. Did the bride smile? Was there a sign on the street? And how sure are you?

## What they found

The short version: the edits leaked into memory.

- People who saw the **AI-edited photos** reported 1.67 times as many false memories as those who saw the originals.
- People who saw **AI videos of the edited photos** reported 2.05 times as many. Nearly 39% of their answers about the altered images were false, against about 19% for the control group.
- Animating the **unedited** photos made only a small difference. Motion did not invent false memories on its own. It amplified the ones already in the frame.

Then the part that bothers me most: confidence.

The video-of-edits group was about 19% more confident in their false memories than the control group was in theirs. On a seven-point scale, their wrong answers averaged around 5.4, somewhere between "somewhat" and "very" confident. They were not guessing. They were sure.

And the "enhanced" label that every participant saw? It did not stop any of this. Being told something was edited is not the same as remembering that it was.

Skepticism toward media, familiarity with AI filters, and education offered no protection either. Only age mattered, slightly: younger people were a little more susceptible.

One more detail stayed with me. Edits to people (a smile, a face, a gender) produced the most false memories overall. But edits to the environment (the time of day, a background, the ice) saw the biggest jump, from about one in ten answers wrong to one in three.

We guard faces. We do not guard the weather.

## Inception without the dream

This is what separates the paper from the films. Nobody in this experiment was drugged, hypnotised, or interviewed three times. There was no team, no kick, no spinning totem. There was a swipeable screen, a label, and five seconds of motion.

The paper opens with a scenario that is already technically possible. You take a photo. An automatic filter quietly removes the "unwanted" people in the background, and the original is not kept. Years later, you remember the scene exactly the way the photo shows it.

Our phones already erase strangers from the frame, swap in a better smile from another shot, and animate old photographs into video.

None of this is malicious. That is exactly the problem. Cobb needed a heist. The camera roll only needs a default setting.

The authors flag an even quieter version for future research: what happens when _you_ make the edit, and later forget you did?

It reminds me of _Memento_. Leonard cannot form new memories, so he lives by his Polaroids and the notes on his skin. By the end, we learn he has been curating his own evidence, writing things down that he knows his future self will trust without question.

We all have a little Leonard in us now. We brighten the sunset, tidy the room, remove the stranger, and leave the result for a future self who will not remember the polish.

## What this means for the tools I build

I cannot read this paper as a neutral observer. Most of my recent work sits right on this fault line.

[Mind Palace XR](https://portfolio-5208db.webflow.io/artificial-intelligence-and-extended-reality/mind-palace-xr) captures a scene through a headset camera and turns it into a 3D object anchored back in the room. [Temporal Self](https://portfolio-5208db.webflow.io/artificial-intelligence-and-extended-reality/temporal-self) resurfaces memories on a map at spaced intervals. [Acoustic Chronotope](https://portfolio-5208db.webflow.io/artificial-intelligence-and-extended-reality/acoustic-chronotope) reads a journal entry and synthesises the ambient sound of that moment. [Memory Mirror](https://portfolio-5208db.webflow.io/artificial-intelligence-and-extended-reality/memory-mirror) floats a name and a note beside a face you might not recognise.

Every one of these tools hands a person an external cue and asks them to trust it. This study is a reminder that the cue can win.

Some early instincts hold up. Mind Palace XR's cues are stylised, closer to small sculptures than photographs, so nobody mistakes them for the record. Acoustic Chronotope generates rain and room tone, never voices or events, and leaves the remembering to you. Temporal Self's spatial walk shows only a place first and asks you to recall before revealing anything.

That last one matters. The paper found passive labels were not enough, and research it cites suggests that prompting people to actively think about accuracy works better. In a memory tool, that means asking before showing.

Others need work. A spaced-repetition system like Temporal Self rehearses whatever it is given, faithfully, on schedule. Give it an edit, and it will rehearse the edit.

So these are the rules I am adopting:

1. **Keep the original, always.** Any tool that edits should store the untouched version one tap away.
2. **Label at recall, not only at viewing.** The moment you are remembering is when you need to know what was recorded, what was inferred, and what was generated.
3. **Ask before you show.** Let the person reach for the memory before the machine fills it in.
4. **Treat motion as the most sensitive format.** Edited video produced the most false memories, and the most confidence in them.

## The photo album we are building

The study has limits: one short exposure, 24 images, US participants only, and memory tested minutes later rather than years. Real life means scrolling past the same edited photo hundreds of times, which the authors expect to make things worse, not better.

Still, I keep coming back to Rachael's photograph.

It was not the implanted memory that convinced her she was human. It was the picture that seemed to prove it.

We are all building that photo album now, one enhancement at a time.

The question is no longer whether machines can plant ideas in our heads.

It is whether we will remember that they did.

---

_Paper:_ Pataranutaporn, P., Archiwaranguprok, C., Chan, S. W. T., Loftus, E., & Maes, P. (2024). [Synthetic Human Memories: AI-Edited Images and Videos Can Implant False Memories and Distort Recollection](https://arxiv.org/abs/2409.08895). arXiv:2409.08895.