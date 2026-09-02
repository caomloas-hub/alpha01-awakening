screen town_short_permit_overlay(name, permit_id):
    zorder 35
    add Solid("#0000008c")

    add Transform("images/town_route/ui/ui-town-temporary-entry-token-v2.png", xysize=(1280, 720)):
        at town_permit_item_appear
        xalign 0.5
        yalign 0.37

    text "获得「{color=#e7b954}灰桥城临时准入证明{/color}」":
        at town_permit_notice_appear
        xalign 0.5
        ypos 822
        size 38
        color "#efe7d7"
        outlines [(2, "#1c120be0", 0, 1)]


screen town_route_complete_overlay(name, trust, affinity):
    zorder 40
    add Solid("#03070dcc")

    vbox:
        at town_chapter_appear
        xalign 0.5
        yalign 0.43
        spacing 18

        text "TOWN ROUTE OPENED" xalign 0.5 size 25 color "#d4ae72" kerning 6
        text "城镇路线／灰桥短籍" xalign 0.5 size 66 color "#fff6e7"
        add Solid("#b78d53") xalign 0.5 xsize 220 ysize 3
        text "[name] 已取得三十日临时居民身份" xalign 0.5 size 29 color "#d8d0c2"
        text "商队信任 [trust]　｜　岚的关系 [affinity]" xalign 0.5 size 22 color "#9eafbd"
