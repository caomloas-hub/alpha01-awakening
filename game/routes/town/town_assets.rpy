image town road day = Transform("images/backgrounds/bg-surface-kingdom.png", xysize=(1920, 1080))
image town road evening = Transform("images/backgrounds/bg-surface-kingdom.png", xysize=(1920, 1080), matrixcolor=TintMatrix("#d6b080"))
image town cg axle = Transform("images/town_route/cg/cg-town-axle-catch-v1.png", xysize=(1920, 1080))
image town cg clothes = Transform("images/town_route/cg/cg-town-pov-change-clothes-v3.png", xysize=(1920, 1080))
image town cg road = Transform("images/town_route/cg/cg-town-road-to-greybridge-v1.png", xysize=(1920, 1080))
image town cg city = Transform("images/town_route/cg/cg-town-first-city-view-v2.png", xysize=(1920, 1080))
image town cg south_market = Transform("images/town_route/cg/cg-town-south-market-v1.png", xysize=(1920, 1080))
image town cg south_yard = Transform("images/town_route/cg/cg-town-south-caravan-yard-v1.png", xysize=(1920, 1080))
image town cg bunk_room = Transform("images/town_route/cg/cg-town-bunk-room-lamplight-v1.png", xysize=(1920, 1080))
image town yard night = Transform("images/town_route/cg/cg-town-first-city-view-v2.png", xysize=(1920, 1080), matrixcolor=TintMatrix("#596a86"))
image town bunk night = Transform("images/town_route/cg/cg-town-first-city-view-v2.png", xysize=(1920, 1080), zoom=1.22, xalign=0.86, yalign=0.56, matrixcolor=TintMatrix("#303c57"))
image town_map base = Transform("images/town_route/map/map-town-caravan-base-v1.png", xysize=(1920, 1080))
image town_map route = Transform("images/town_route/map/map-town-caravan-route-v1.png", xysize=(1920, 1080))
image town_paw pointer = "images/town_route/map/paw-lan-map-pointer-v2.png"

transform town_paw_enter_city:
    zoom 0.62
    xpos 1.04
    ypos 0.30
    alpha 0.0
    easeout 0.65 xpos 0.73 alpha 1.0

transform town_paw_to_road:
    zoom 0.62
    xpos 0.73
    ypos 0.30
    easein 0.85 xpos 0.13 ypos 0.62

transform town_paw_back_to_city:
    zoom 0.62
    xpos 0.13
    ypos 0.62
    easein 0.90 xpos 0.73 ypos 0.30
    linear 0.10 yoffset -13
    linear 0.10 yoffset 0
    pause 0.08
    linear 0.10 yoffset -13
    linear 0.10 yoffset 0

transform town_chapter_appear:
    alpha 0.0
    yoffset 28
    easeout 0.45 alpha 1.0 yoffset 0

transform town_permit_item_appear:
    alpha 0.0
    zoom 0.88
    yoffset 24
    easeout 0.34 alpha 1.0 zoom 1.04 yoffset -6
    easein 0.18 zoom 1.0 yoffset 0

transform town_permit_notice_appear:
    alpha 0.0
    yoffset 14
    pause 0.16
    easeout 0.30 alpha 1.0 yoffset 0
