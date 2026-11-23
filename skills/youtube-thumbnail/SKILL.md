---
name: youtube-thumbnail
description: 'Builds a branded YouTube thumbnail brief and a ready image prompt from the video title, a reference photo of the creator and brand colours. Use for "thumbnail", "youtube thumbnail", "capa do vídeo", "build me a thumbnail". NÃO usar para banner de canal (banner-design) nem para criativo de anúncio.'
---

# YouTube Thumbnail

## CRITICAL: Auto-start on load

When this skill triggers, go straight to Step 1.

## Step 1. Gather inputs

Check the project for a reference photo config. Look in this order:

1. `thumbnail-config.md` in the project root
2. `brand-kit.md` — look for a reference image path and brand colours
3. `about-me.md` — for the creator's name and positioning

If a reference photo path is stored, pre-fill it. Otherwise ask:

> Upload or provide the path to the reference photo of yourself you want used in the thumbnail. Ideally a clear headshot with distinctive lighting and expression you plan to reuse across videos for brand consistency.

Ask only what is missing, in one message:

- **Video title** — if not given, propose 3 click-worthy titles from the topic and use the strongest.
- **Emotional tone** — default: inferred from the title (shock / surprise, curious / thinking, confident / direct, frustrated /
  strong take). Say it in one line: "Assumi: tom X (é só pedir para mudar)."

## Step 2. Apply thumbnail best practices

Every thumbnail must follow these rules:

- **Face fills 30 to 50 percent** of the frame. Readable at small sizes.
- **3 to 5 words maximum** of large text. 6 if absolutely necessary.
- **Two colours dominate**. Brand primary + one high-contrast accent (yellow, red, cyan work well).
- **One clear focal element** besides the face. Tool logo, bold number, arrow, or prop.
- **High contrast** between face, text, and background. Test by squinting.
- **Text is not a sentence**. It is a hook phrase. Examples: "I fired my team", "Claude can now...", "Don't do this".
- **No small text, no logos bottom-right** (watch time icon sits there).

## Step 3. Build the thumbnail brief

Output a concise brief the user can review:

```
THUMBNAIL BRIEF: [video title]

Composition: [face position, % of frame, direction of gaze]
Text: "[hook phrase, 3-5 words]"
Text placement: [left, right, top, wraps around face]
Colour palette: [primary hex], [accent hex], [background hex]
Supporting element: [logo / prop / arrow / number]
Emotional tone: [tone from Step 1]
```

Then ask:

> Here's the brief. Say "generate" to output the image prompt or tell me what to change.

## Step 4. Output the image prompt

Once approved, output the image generation prompt in a code block:

```
Using the attached reference photo of me, generate a YouTube thumbnail at 1280 x 720 pixels (16:9).

Composition:
- Place me [left / right / centre] filling [30-50]% of the frame
- My expression: [tone details — e.g., shocked with wide eyes and open mouth]
- My gaze: [direction — e.g., looking directly at camera / looking off-frame toward the text]

Text:
- Display "[hook phrase]" in large bold sans-serif typography
- Text colour: [hex]
- Text outline: [colour, thickness for readability]
- Text placement: [specific area]

Colour palette:
- Primary: [hex]
- Accent: [hex]
- Background: [hex] — [describe treatment: flat, gradient, blurred scene, etc.]

Supporting element: [specific description of the supporting visual]

Constraints:
- Face must be clear and sharp
- Text must be readable at 320px wide (YouTube mobile size)
- No watermarks, no YouTube UI elements, no bottom-right corner text
- High contrast between face, text, and background
```

Tell the user:

> Paste this into the image generator you already use (e.g. Gemini with image creation, or ChatGPT), attach your reference photo, and generate at 1280x720. If an image generator is available in this environment, I can run it directly.

## Step 5. Offer the next move

> Want me to outline the video next? Hook, mid, CTA from the thumbnail. Or call the create skill if you have one.

## Rules

- 1280x720 pixels (16:9). YouTube's native thumbnail size.
- Never include the reference photo path in the prompt itself — the user attaches the photo separately.
- Never allow more than 6 words of text, 5 is ideal, 3 is best.
- Face must always be a visible focal point. No face-hidden compositions.
- Never use em dashes.
- British English unless voice.md specifies otherwise.
- If brand-kit.md is in the project, read it and use exact brand colours.
- Recommend the user keep a consistent thumbnail style across videos for channel recognition.
