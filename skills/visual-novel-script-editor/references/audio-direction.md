# Audio Direction for Visual-Novel Scenes

Read this reference only when selecting, editing, integrating, or reviewing audio.

## Build a scene in layers

- **Ambience:** a restrained loop that establishes place, time, enclosure, and distance.
- **Event sound:** a one-shot tied to a visible or narrated action.
- **Interface feedback:** short hover, confirm, back, disabled, and major-notice sounds kept separate from diegetic events.
- **Music:** emotional structure or recurring identity; do not use it to conceal missing ambience or action sounds.

Start with ambience and the few actions that change the scene. Silence can be intentional. Avoid attaching a sound to every sentence or gesture.

## Choose and document assets

Prefer CC0. CC BY is usable when commercial use and modification are allowed and attribution is recorded. Avoid NC assets in a project that may later be sold, crowdfunded, or published commercially.

For every external file, record:

- final in-project filename;
- title and creator;
- original asset page URL;
- exact license and license URL;
- download date;
- edits such as trimming, fades, EQ, layering, pitch, or normalization.

“Free,” “royalty-free,” and “open source” are not interchangeable. Read the license attached to the individual asset or pack. Preserve a copy or link to the terms that applied when the asset was downloaded.

## Prepare game-ready audio

- Make ambience loops seamless and avoid sudden noise-floor or stereo-image changes at the seam.
- Keep dialogue intelligible; reduce competing midrange and use conservative ambience levels.
- Consider variants for repeated physical actions when repetition is audible. Consistent UI feedback may be preferable; do not require random variation for every click.
- Use short fades when changing locations. Let shared distant sounds bridge adjacent scenes only when geography and time make that credible.
- Keep UI sounds dry and consistent. Do not reuse a hover sound as a chapter sting, map marker, notification, and physical-world effect.

## Integrate and verify

Use separate engine channels for ambience, music, ordinary SFX, and UI when the engine supports them. Verify that each file loads, loops, stops, fades, and respects volume settings. Run syntax and branch checks, then leave final loudness, timbre, and emotional fit to listening-based user acceptance rather than waveform snapshots or hashes.

In text-led games without voice acting, judge fatigue and distraction during reading rather than claiming speech masking. When changing event triggers, check whether advancing, skipping, rollback, or load can repeat or overlap a sound unexpectedly. Only test playback modes affected by the change.
