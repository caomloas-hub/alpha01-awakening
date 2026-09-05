---
name: visual-novel-script-editor
description: Review and rewrite visual-novel or interactive-fiction chapters while preserving plot structure, branch logic, character intent, and presentation continuity. Use when dialogue feels forced, characters share one authorial voice, emotional beats lack weight, exposition sounds unnatural, or a Ren'Py chapter needs a scene-level production pass. Do not use for inventing a new plot unless the user also requests story development.
---

# Visual Novel Chapter Editor

Rewrite the script at scene level, not as isolated pretty sentences. Preserve the user's plot, route structure, choices, variables, callbacks, and established facts unless they explicitly authorize changes.

When the request includes asset production or implementation, treat text, background/CG, sound, UI, and engine state as one scene. Read [production-integration.md](references/production-integration.md) before changing those systems. Do not rewrite a line in a way that requires art, costume, location, or audio the project does not have without flagging that dependency.

## Establish evidence and edit scope

Use the user's latest accepted direction and current script as the working baseline. Separate established facts, character beliefs, deliberate unknowns, and proposed additions. A compelling interpretation is not automatically canon.

Read the surrounding exchange and relevant branch conditions before diagnosing a line. Choose the smallest effective intervention: retain, trim, rephrase, move, or rewrite the beat. A request to review calls for findings; a request to edit authorizes edits within that scope. Do not silently turn a line polish into a new event or a different character motive.

Before replacing an abstract line with concrete detail, check what the detail asserts. Falling masonry adds danger; a remembered night outside a gate adds biography; a gesture can imply trust the scene has not earned. Prefer established objects and actions, and flag additions that change causality or characterization.

The severity of a problem does not grant a wider edit scope. Separate a factual/branch contradiction from an awkward sentence and from a matter of taste. For Chinese line editing, read [chinese-revision.md](references/chinese-revision.md); for multi-scene or converging-route work, read [route-continuity.md](references/route-continuity.md). These are editing aids, not mandatory reports for every line.

When incorporating author feedback or approved passages into future guidance, read [author-calibration.md](references/author-calibration.md). Keep project canon and author preferences in project notes, not as universal rules in this reusable Skill.

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

Match literary density to the requested voice and the scene. Keep a metaphor, plain emotional statement, or deliberate repetition when it adds perspective, rhythm, or meaning. Trim competing images and redundant interpretation; do not impose a metaphor quota or turn every feeling into a stock gesture. Directness and restraint are choices, not universal measures of quality.

## Control narrative distance and rhythm

Move prose closer during fear, shame, intimacy, or immediate physical danger: use what the viewpoint character can touch, hear, fail to say, or accidentally reveal. Pull back during travel, time skips, and necessary background so every transition does not carry the intensity of a climax.

Let pressure shape sentence length. Under urgent action, shorten syntax and place the decisive verb early. During recovery or observation, allow longer sentences, but keep their physical subject clear. Avoid several consecutive lines with matching length, mirrored clauses, or the same polished cadence.

Choose sensory detail according to character attention. A cautious protagonist notices exits and hands; a trader notices quantities and damaged seals; a gate officer notices discrepancies. Do not add scent, weather, texture, and sound all at once merely to make a paragraph seem literary.

These attention patterns are examples, not occupational scripts. Relationships, fatigue, private concerns, and the specific listener can redirect attention. Do not replace shared authorial wit with equally repetitive character mannerisms.

Do not explain an action and then explain the emotion it already conveyed. When a gesture, interruption, or object carries the beat, let the following line advance the scene instead of translating it into an abstract conclusion.

## Control exposition

Deliver worldbuilding through a current need: passing a gate, repairing a vehicle, finding shelter, misunderstanding currency, or recognizing an old object. Characters explain only what the listener needs, what they would naturally volunteer, and what the immediate situation permits.

Avoid dialogue whose only purpose is teaching the player. If an explanation is necessary, give the speaker a reason to be impatient, cautious, proud, mistaken, or selective about it.

Check who knows each fact and how they learned it, including optional scenes. Distinguish the player's knowledge from the protagonist's and the speaker's. A technically trained viewpoint may naturally use technical vocabulary; remove terms because they obstruct the present exchange, not because they appear on a blacklist. Preserve intentionally withheld information without making basic actions hard to follow.

## Preserve interactive consequences

Different choices should leave small textual consequences even when branches reconverge. Reuse a prior action, piece of knowledge, withheld truth, or emotional reaction later in the scene. Do not make every choice produce a new route; make it alter how the same event is experienced.

Only add callbacks supported by the branch history and requested edit scope. A choice may express attitude without earning a reward or a new consequence. Keep the action promised by the option consistent with what follows; avoid silently making a cautious option aggressive or a neutral option romantic.

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

1. Could characters swap distinctive, consequential lines without changing the exchange? Check motive, knowledge, and relationship before adding verbal quirks. Ordinary acknowledgments may sound alike.
2. Do repeated jokes, maxims, or polished comebacks flatten the emotional range? Retain the ones earned by the speaker and moment.
3. Does narration explain the emotion after the action already showed it? Keep the stronger version.
4. Does a character know something only because the player needs exposition? Change the delivery or defer it.
5. Do images compete or repeat meaning? Keep the combination that carries the intended voice and beat, without a numerical quota.
6. Do reconverged branches remember what the player chose? Add a restrained callback where useful.
7. Does revised text still match the displayed location, costume, time, viewpoint, and available art?
8. Do important actions have an intentional sound cue, and are repeated UI or event sounds varied enough to avoid mechanical repetition?
9. Does static art text belong in the image, while dynamic information remains controllable by the engine?
10. Did syntax checks and affected branch tests exercise the actual changed menu or screen?

Compare meaning in both directions: what did the revision lose, and what does it newly assert? Protect negation, uncertainty, chronology, promises, quantities, and the difference between private thought and spoken dialogue. Do not evaluate literary quality by an AI-detector score or by how many banned words disappeared.

Report the few decisions that materially changed the scene, with representative before/after examples when useful. Identify any proposed new facts and unresolved art dependencies. Preserve strong passages instead of rewriting everything to demonstrate effort. Report tests only for the paths and behaviors actually exercised; separate engine checks from user acceptance. Do not introduce SHA, screenshot pixel equality, or file-tree integrity checks unless the user explicitly asks for them.

The narrative-distance, sensory-selection, and prose-rhythm guidance in this Skill is informed by the Apache-2.0 licensed [Creative Writing Craft](https://github.com/haowjy/creative-writing-skills/blob/main/skills/creative-writing-craft/SKILL.md) and [Prose Writing](https://github.com/haowjy/creative-writing-skills/blob/main/skills/creative-writing-craft/resources/prose-writing.md) references. Apply the principles to visual-novel production rather than copying their example prose.
