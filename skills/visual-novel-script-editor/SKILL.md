---
name: visual-novel-script-editor
description: Review and rewrite visual-novel or interactive-fiction chapters while preserving plot structure, branch logic, character intent, and presentation continuity. Use when dialogue feels forced, characters share one authorial voice, emotional beats lack weight, exposition sounds unnatural, or a Ren'Py chapter needs a scene-level production pass. Do not use for inventing a new plot unless the user also requests story development.
---

# Visual Novel Chapter Editor

Rewrite the script at scene level, not as isolated pretty sentences. Preserve the user's plot, route structure, choices, variables, callbacks, and established facts unless they explicitly authorize changes.

When the request includes asset production or implementation, treat text, background/CG, sound, UI, and engine state as one scene. Read [production-integration.md](references/production-integration.md) before changing those systems. Do not rewrite a line in a way that requires art, costume, location, or audio the project does not have without flagging that dependency.

## Establish the dramatic function

Before rewriting, identify for each scene:

- what materially changes by the end;
- what the viewpoint character wants right now;
- what information must become known;
- where emotional pressure rises, turns, and releases;
- which image, action, or silence should carry the strongest feeling.

Remove or relocate lines that repeat information without changing tension, relationship, or player understanding.

## Separate character voices

Give every speaking character a compact voice model:

- default conversational tactic, such as deflecting, bargaining, observing, ordering, or soothing;
- sentence length and rhythm;
- knowledge and vocabulary they plausibly possess;
- what they avoid saying directly;
- when, if ever, they use humor;
- how their voice changes under fear, embarrassment, authority, or intimacy.

Do not mistake a recurring catchphrase for characterization. A rational character should usually reveal rationality through what they notice, the order in which they act, and the risks they refuse—not by repeatedly saying “objectively,” “variable,” “protocol,” or similar analytical terms. A witty character does not need a punchline in every exchange. Let minor characters decline to match the protagonist's verbal sophistication.

## Put emotion into behavior

Prefer physical and situational evidence before emotional explanation:

- a delayed answer, revised gesture, misplaced object, interrupted routine, or changed distance;
- one concrete sensory detail tied to the present location;
- dialogue that circles an exposed feeling instead of naming it immediately;
- silence when another line would merely explain what the player already understands.

Use literary language sparingly. Start from a concrete object or sensation, then allow at most one strong comparison in an emotional beat. Remove a metaphor if it competes with the action, repeats the same meaning, or makes the viewpoint character sound like the narrator instead of themselves.

## Control narrative distance and rhythm

Move prose closer during fear, shame, intimacy, or immediate physical danger: use what the viewpoint character can touch, hear, fail to say, or accidentally reveal. Pull back during travel, time skips, and necessary background so every transition does not carry the intensity of a climax.

Let pressure shape sentence length. Under urgent action, shorten syntax and place the decisive verb early. During recovery or observation, allow longer sentences, but keep their physical subject clear. Avoid several consecutive lines with matching length, mirrored clauses, or the same polished cadence.

Choose sensory detail according to character attention. A cautious protagonist notices exits and hands; a trader notices quantities and damaged seals; a gate officer notices discrepancies. Do not add scent, weather, texture, and sound all at once merely to make a paragraph seem literary.

Do not explain an action and then explain the emotion it already conveyed. When a gesture, interruption, or object carries the beat, let the following line advance the scene instead of translating it into an abstract conclusion.

## Control exposition

Deliver worldbuilding through a current need: passing a gate, repairing a vehicle, finding shelter, misunderstanding currency, or recognizing an old object. Characters explain only what the listener needs, what they would naturally volunteer, and what the immediate situation permits.

Avoid dialogue whose only purpose is teaching the player. If an explanation is necessary, give the speaker a reason to be impatient, cautious, proud, mistaken, or selective about it.

## Preserve interactive consequences

Different choices should leave small textual consequences even when branches reconverge. Reuse a prior action, piece of knowledge, withheld truth, or emotional reaction later in the scene. Do not make every choice produce a new route; make it alter how the same event is experienced.

When editing Ren'Py or another scripted engine:

- preserve labels, menu text, conditions, variables, interpolation, and control flow unless changes are authorized;
- treat choice labels used by tests or localization as stable identifiers;
- keep dialogue blocks readable at the target resolution;
- align scene and CG changes with actual location, time, clothing, and character state;
- run the engine's syntax check and relevant branch tests after editing.

## Align presentation with the scene

For each location or time change, decide whether it requires a new background/CG, a transition on an existing image, or only textual staging. Do not let one attractive CG silently stand in for several unrelated locations.

Prefer first-person composition when the protagonist's complete appearance is intentionally withheld. Check visible sleeves, paws, tails, props, lighting, and character positions against the exact script state.

Generated words inside images are appropriate when they are stable and belong physically to the world or fixed interface. Keep variable player data and changing values in the engine. When image-backed controls are used, animate the full button and retain semantic hotspots for keyboard focus, touch, and tests.

When sound work is requested, read [audio-direction.md](references/audio-direction.md). Add sound because the scene has an audible cause, spatial identity, or interaction need—not merely because a timeline is quiet.

## Revision pass

After rewriting, read the scene continuously and check:

1. Could two characters swap lines without sounding wrong? If yes, separate their voices further.
2. Does every exchange end in a joke, maxim, or polished comeback? Flatten most of them.
3. Does narration explain the emotion after the action already showed it? Keep the stronger version.
4. Does a character know something only because the player needs exposition? Change the delivery or defer it.
5. Are several metaphors stacked around one feeling? Keep one concrete image.
6. Do reconverged branches remember what the player chose? Add a restrained callback where useful.
7. Does revised text still match the displayed location, costume, time, viewpoint, and available art?
8. Do important actions have an intentional sound cue, and are repeated UI or event sounds varied enough to avoid mechanical repetition?
9. Does static art text belong in the image, while dynamic information remains controllable by the engine?
10. Did syntax checks and affected branch tests exercise the actual changed menu or screen?

Report meaningful voice, pacing, visual-continuity, sound-direction, UI, and state-handling changes. Do not present unchanged plot structure as a creative rewrite. Separate objective engine checks from subjective user acceptance. Do not introduce SHA, screenshot pixel equality, or file-tree integrity checks unless the user explicitly asks for them.

The narrative-distance, sensory-selection, and prose-rhythm guidance in this Skill is informed by the Apache-2.0 licensed [Creative Writing Craft](https://github.com/haowjy/creative-writing-skills/blob/main/skills/creative-writing-craft/SKILL.md) and [Prose Writing](https://github.com/haowjy/creative-writing-skills/blob/main/skills/creative-writing-craft/resources/prose-writing.md) references. Apply the principles to visual-novel production rather than copying their example prose.
