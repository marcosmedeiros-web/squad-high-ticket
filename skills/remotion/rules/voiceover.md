---
name: voiceover
description: Adding AI-generated voiceover to Remotion compositions using TTS
metadata:
  tags: voiceover, audio, voicestudio, tts, speech, calculateMetadata, dynamic duration
---

# Adding AI voiceover to a Remotion composition

Use the local VoiceStudio TTS (free, open-source, runs on this machine; no API key) to generate speech audio per scene, then use [`calculateMetadata`](./calculate-metadata) to dynamically size the composition to match the audio.

## Prerequisites

Use only free tools. The TTS here is a local OpenAI-compatible server such as **VoiceStudio**; if it is not running, offer to set it up and say what will be installed, with the person's OK. Without it, use Kokoro (`npx hyperframes tts "<text>" --voice <voice> -o file.wav`). If both fail, deliver the composition with on-screen text and no voiceover, and say so. Never ask for a paid TTS key.

```bash
node --strip-types generate-voiceover.ts
```

## Generating audio with VoiceStudio

Create a script that reads the config, calls the local VoiceStudio for each scene, and writes WAV files to the `public/` directory so Remotion can access them via `staticFile()`.

The core API call for a single scene (OpenAI-compatible endpoint on localhost):

```ts title="generate-voiceover.ts"
const response = await fetch("http://127.0.0.1:3900/v1/audio/speech", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    model: "omnivoice",
    input: "Bem-vindo ao programa.",
    language: "pt",
    // voice: "<cloned profile id>", only with the owner's consent
  }),
  signal: AbortSignal.timeout(300_000), // CPU-only: ~88 s per ~6 s of speech
});
if (!response.ok) throw new Error(`VoiceStudio HTTP ${response.status}`);

const audioBuffer = Buffer.from(await response.arrayBuffer());
writeFileSync(`public/voiceover/${compositionId}/${scene.id}.wav`, audioBuffer);
```

## Dynamic composition duration with calculateMetadata

Use [`calculateMetadata`](./calculate-metadata.md) to measure the [audio durations](./get-audio-duration.md) and set the composition length accordingly.

```tsx
import { CalculateMetadataFunction, staticFile } from "remotion";
import { getAudioDuration } from "./get-audio-duration";

const FPS = 30;

const SCENE_AUDIO_FILES = [
  "voiceover/my-comp/scene-01-intro.wav",
  "voiceover/my-comp/scene-02-main.wav",
  "voiceover/my-comp/scene-03-outro.wav",
];

export const calculateMetadata: CalculateMetadataFunction<Props> = async ({
  props,
}) => {
  const durations = await Promise.all(
    SCENE_AUDIO_FILES.map((file) => getAudioDuration(staticFile(file))),
  );

  const sceneDurations = durations.map((durationInSeconds) => {
    return durationInSeconds * FPS;
  });

  return {
    durationInFrames: Math.ceil(sceneDurations.reduce((sum, d) => sum + d, 0)),
  };
};
```

The computed `sceneDurations` are passed into the component via a `voiceover` prop so the component knows how long each scene should be.

If the composition uses [`<TransitionSeries>`](./transitions.md), subtract the overlap from total duration: [./transitions.md#calculating-total-composition-duration](./transitions.md#calculating-total-composition-duration)

## Rendering audio in the component

See [audio.md](./audio.md) for more information on how to render audio in the component.

## Delaying audio start

See [audio.md#delaying](./audio.md#delaying) for more information on how to delay the audio start.
