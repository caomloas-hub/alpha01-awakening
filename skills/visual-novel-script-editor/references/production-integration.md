# Production Integration for Visual-Novel Revisions

Read this reference when a script revision also changes CGs, backgrounds, menus, sound, Ren'Py screens, branch tests, or platform builds.

## Freeze the story contract

Before editing, list the labels, menu captions, variables, persistent fields, interpolation, branch joins, save-directory identity, and test selectors that must remain stable. Treat these as interfaces. A prose improvement must not silently break automation, localization, old saves, or route state.

## Build a scene-state sheet

Reuse existing notes and record only facts relevant to the change. For an asset replacement or multi-scene revision, the useful fields are:

- location, time, weather, and light;
- visible characters and their positions;
- protagonist viewpoint and visible body parts;
- current clothing, carried objects, injuries, and props;
- the dramatic change the beat must deliver;
- background or CG, ambience, music, and action sounds;
- variables read or written before leaving the scene.

Use this sheet to detect attractive assets being reused across unrelated places, clothing changing before the script says it does, or dialogue referring to a prop that is not visible.

## Decide where text belongs

Bake text into art only when it is stable and physically or visually part of that art, such as a title logo, engraved courtroom sign, fixed menu label, or chapter emblem. Match perspective, surface, wear, light, and shadow.

Keep player names, save dates, page numbers, counters, changing descriptions, error messages, and other stateful content in the engine. Do not bake dynamic information merely to improve visual integration.

For image-backed buttons:

- animate the whole labeled button, not a separate text layer;
- retain an engine hotspot and an invisible semantic label for keyboard focus and tests;
- give touch targets adequate size and a pressed state that does not depend on hover;
- keep dynamic save-slot content separate from static menu decoration.

For transparent title art, inspect the alpha fringe on both light and dark backgrounds. Place decorative silhouettes so they support the word shape rather than obscure recognition.

An invisible label does not by itself prove screen-reader support, visible keyboard focus, or that a pointer hotspot matches the pictured button. Check those behaviors separately when in scope. Baking text also creates localization and scaling costs; follow the project's chosen art direction while retaining editable source and exact text specifications.

## Preserve viewpoint continuity

If the protagonist's complete appearance is intentionally withheld, prefer first-person compositions and reveal only necessary paws, sleeves, maps, tools, or sight-line edges. State exactly which garment is already worn. For furry characters, check tail origin, ear and horn placement, limb anatomy, sleeve openings, tail holes, and how clothing reacts to movement.

Anchor pointing hands or paws by the fingertip or claw actually indicating the target, not by the image rectangle's center. Trim unused transparent margins before calibrating screen coordinates.

## Integrate sound by cause

Separate ambience, music, event effects, and UI feedback. Use short crowd or gate texture to establish a place without competing with dialogue. A sound should correspond to an audible action, a spatial identity, or an interaction state. Keep hover and confirm sounds distinct from map taps, chapter notices, impacts, and physical-world objects.

For licensing and asset preparation, read [audio-direction.md](audio-direction.md).

## Validate in layers

1. Run the engine syntax check and compile.
2. Run the smallest branch test that exercises the changed label or screen.
3. Confirm images, screens, sounds, and dynamic fields load without exceptions.
4. Confirm the route reaches its intended join and writes the same required state.
5. Build the target platform only after the source path is stable.
6. Leave composition, wording, loudness, and emotional fit to human playtesting.

Do not assume lint proves menu semantics. A dialogue line at the wrong indentation may still parse while changing the choices presented. Read changed menu blocks and run a route that selects the affected option.

Separate delayed-behavior tests into two claims. A fixture that sets the revealed flag can test the revealed menu and route, but cannot validate the timer, its callback, or the preceding dialogue. To test the trigger, invoke the production callback with a controlled clock or test-only duration where supported, or exercise the actual wait. Verify that it is absent before the trigger, appears after it, and does not fire twice. If only the fixture ran, explicitly leave timer behavior unverified. Do not weaken a failing test merely to obtain a pass.

Initialize each route test from a known state. Isolate test saves and persistent data from the user's playthrough; reset relevant fixtures between cases. Verify changed preconditions and resulting state, not just that an ending label was reached. Saving and loading requires an actual round trip that restores representative state; opening the save page alone proves only navigation. Keep these checks proportional to the change, and build or deploy only platforms included in the current request.

On Windows, Ren'Py GUI executables may not expose terminal output reliably. Redirect stdout and stderr from a separate process when evidence is needed. For Android, verify the exact JDK required by the installed Ren'Py/RAPT version before building; package creation does not replace device-level touch, keyboard, crop, and audio acceptance.

## Hand off for acceptance

Report what changed in voice, pacing, scene continuity, art dependencies, sound, and state handling. Separate objective checks from subjective acceptance:

- objective: syntax, loading, route reachability, variable writes, package metadata;
- subjective: composition, readability, character appeal, prose tone, animation feel, and mix balance.

Do not use screenshot pixel equality, hashes, or full file-tree checks as substitutes for either category unless the user specifically requests them.
