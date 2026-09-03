image origin concept town = "images/route_select/concept-route-town-highway-v1.png"
image origin concept wanderer = "images/route_select/concept-route-wanderer-ruins-v1.png"
image origin concept village = "images/route_select/concept-route-village-path-v1.png"


transform origin_hidden_choice_appear:
    alpha 0.0
    xoffset -28
    easeout 0.45 alpha 1.0 xoffset 0


screen origin_route_choice(show_wanderer=False):
    style_prefix "choice"
    modal True
    zorder 100

    key "game_menu" action ShowMenu("pause_menu")

    add Solid("#010711a6")

    if not show_wanderer:
        timer 120.0 action Return("waited")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing gui.choice_spacing

        textbutton "走向乡间小道" action Return("village")
        textbutton "沿着国道边缘前进" action Return("town")

        if show_wanderer:
            textbutton "向远处的建筑物探索":
                at origin_hidden_choice_appear
                action Return("wanderer")


label origin_route_select:
    scene origin concept town with dissolve
    centered "地表路线"
    ao "国道伸向山谷外。路上暂时没有行人，远处却能看见炊烟。"

    scene origin concept wanderer with dissolve
    ao "另一侧，旧建筑越过荒野露出轮廓。那里不像聚落，也没有正在使用的道路。"

    scene origin concept village with dissolve
    ao "乡间小道钻进林带。枝叶遮住了尽头，泥地上还留着新鲜的足迹。"

    scene bg surface with dissolve
    ao "我现在需要的不是最安全的答案，而是一条能够继续活下去的路。"

    $ _origin_wanderer_revealed = False

label origin_route_choose:
    call screen origin_route_choice(_origin_wanderer_revealed)

    if _return == "waited":
        scene origin concept wanderer with dissolve
        ao "我在岔路前停得太久，远处那片建筑却始终没有从视野里消失。"
        ao "也许，我不必立刻走向任何一处聚落。"
        scene bg surface with dissolve
        $ _origin_wanderer_revealed = True
        jump origin_route_choose

    if _return == "village":
        $ origin_route = "village"
        jump village_route_preview

    if _return == "town":
        $ origin_route = "town"
        jump town_route_start

    $ origin_route = "wanderer"
    jump wanderer_route_preview


label village_route_preview:
    scene bg surface with fade
    centered "村庄路线正在开发中"
    "乡间小道没入林带。更深处传来枝叶断裂的声音，绝不是风。"
    ao "这条路有人走，也有别的东西在走。"
    $ persistent.last_origin_route = "village_preview"
    return


label wanderer_route_preview:
    scene bg surface with fade
    centered "流浪者路线正在开发中"
    "远处建筑的轮廓横在天际，既不像聚落，也不像还能正常运转的设施。"
    ao "那里至少会留下能够判断来路的痕迹。"
    $ persistent.last_origin_route = "wanderer_preview"
    return
