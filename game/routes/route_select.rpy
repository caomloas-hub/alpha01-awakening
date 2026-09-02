label origin_route_select:
    scene bg surface with dissolve

    centered "地表路线"
    ao "道路、聚落和远处的旧建筑分别通向不同的人群。"
    ao "我现在需要的不是最安全的答案，而是一条能够继续活下去的路。"

    menu:
        "走向乡间小道":
            $ origin_route = "village"
            jump village_route_preview

        "沿着国道边缘前进":
            $ origin_route = "town"
            jump town_route_start

        "向远处的建筑物探索":
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
