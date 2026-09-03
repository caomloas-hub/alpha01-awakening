transform ctc_paw_blink:
    xpos 1530
    ypos 1028
    xanchor 0.5
    yanchor 0.5
    alpha 0.20
    linear 0.55 alpha 0.95
    linear 0.55 alpha 0.20
    repeat

define ctc_paw = At("gui/ctc_paw.svg", ctc_paw_blink)

## Bare narration uses the same end-of-line cue as named dialogue.
define narrator = Character(None, ctc=ctc_paw, ctc_position="fixed")
