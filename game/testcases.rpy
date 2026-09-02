testcase argue_technology_route:
    $ _test.timeout = 150.0
    $ _test.transition_timeout = 0.08

    click "开始游戏"
    advance until screen "choice"
    click "抗辩"
    advance until screen "choice"
    click "前往中央控制室"
    advance until screen "choice"
    click "返回休眠舱，检查其余原型体"
    advance until screen "choice"
    click "沿主通道前往出口"
    advance until screen "choice"
    click "采用名字“敖浔奕”"
    advance until screen "choice"
    click "进行最低功率神经加速测试"
    advance until screen "choice"
    $ assert tech_insight >= 2 and inspected_prototypes
    click "带走设施离线核心"
    advance until screen "choice"
    click "走向乡间小道"
    advance until screen "main_menu"
    $ assert persistent.prologue_cleared and persistent.unlocked_core_route
    $ assert persistent.last_player_name == "敖浔奕"
    $ assert persistent.last_surface_plan == "core"
    $ assert persistent.last_origin_route == "village_preview"


testcase silent_observer_route:
    $ _test.timeout = 150.0
    $ _test.transition_timeout = 0.08

    click "开始游戏"
    advance until screen "choice"
    click "沉默"
    advance until screen "choice"
    click "搜索医疗与应急物资"
    advance until screen "choice"
    click "前往中央控制室"
    advance until screen "choice"
    click "沿主通道前往出口"
    advance until screen "choice"
    click "采用名字“敖浔奕”"
    advance until screen "choice"
    click "不在未知环境中启动义体"
    advance until screen "choice"
    click "先观察通往王国的道路"
    advance until screen "choice"
    click "向远处的建筑物探索"
    advance until screen "main_menu"
    $ assert persistent.last_court_response == "silent"
    $ assert persistent.last_caution >= 3
    $ assert persistent.last_origin_route == "wanderer_preview"


testcase prototype_memorial_route:
    $ _test.timeout = 150.0
    $ _test.transition_timeout = 0.08

    click "开始游戏"
    advance until screen "choice"
    click "抗辩"
    advance until screen "choice"
    click "返回休眠舱，检查其余原型体"
    advance until screen "choice"
    click "前往中央控制室"
    advance until screen "choice"
    click "沿主通道前往出口"
    advance until screen "choice"
    click "采用名字“敖浔奕”"
    advance until screen "choice"
    click "不在未知环境中启动义体"
    advance until screen "choice"
    click "在出口为其他原型体留下标记"
    advance until screen "choice"
    click "走向乡间小道"
    advance until screen "main_menu"
    $ assert persistent.last_surface_plan == "memorial"
    $ assert persistent.remembered_prototypes


testcase custom_name_input:
    $ _test.timeout = 90.0
    $ _test.transition_timeout = 0.08

    run Jump("approach_exit")
    advance until screen "choice"
    click "自己取一个名字"
    type "Linchuan"
    keysym "K_RETURN"
    pause 0.3
    $ assert player_name == "Linchuan"


testcase escape_pause_and_secondary_menu:
    $ _test.timeout = 60.0
    $ _test.transition_timeout = 0.08

    click "开始游戏"
    advance until screen "choice"
    keysym "K_ESCAPE"
    advance until screen "pause_menu"
    click "保存进度"
    advance until screen "save"
    click "返回暂停"
    advance until screen "pause_menu"
    click "继续游戏"
    advance until screen "choice"


testcase town_minimal_road_route:
    $ _test.timeout = 220.0
    $ _test.transition_timeout = 0.08

    click "开始游戏"
    advance until screen "choice"
    $ player_name = "敖浔奕"
    $ tech_insight = 0
    $ gathered_supplies = False
    $ inspected_prototypes = False
    $ tested_accelerator = False
    $ persistent.town_route_opened = False
    run Jump("town_route_start")
    advance until screen "choice"
    click "保持距离，先数清人数"
    advance until screen "choice"
    click "先把双手放在所有人看得见的地方"
    advance until screen "choice"
    click "尽量少说，只保证能工作"
    advance until screen "choice"
    click "走在后车外侧观察路况"
    advance until screen "choice"
    click "接受这个边界"
    advance until eval persistent.town_route_opened timeout 30.0
    $ assert persistent.town_route_opened and persistent.town_permit
    $ assert persistent.town_cover_story == "minimal"
    $ assert persistent.town_work_choice == "road"
    $ assert persistent.town_money == 23 and persistent.town_bed == "south_yard_bunk_07"
    $ assert persistent.town_outfit


testcase town_ordered_axle_route:
    $ _test.timeout = 220.0
    $ _test.transition_timeout = 0.08

    click "开始游戏"
    advance until screen "choice"
    $ player_name = "敖浔奕"
    $ tech_insight = 2
    $ gathered_supplies = True
    $ inspected_prototypes = True
    $ tested_accelerator = False
    $ persistent.town_route_opened = False
    run Jump("town_route_start")
    advance until screen "choice"
    click "观察车辆和路面"
    advance until screen "choice"
    click "指出轮毂还会继续裂开"
    advance until screen "choice"
    click "把塌方、失散和行程整理成完整顺序"
    advance until screen "choice"
    click "协助衡叔加固车轴"
    advance until screen "choice"
    click "反问他为什么愿意担风险"
    advance until eval persistent.town_route_opened timeout 30.0
    $ assert persistent.town_cover_story == "ordered"
    $ assert persistent.town_work_choice == "axle"
    $ assert persistent.town_caravan_trust >= 5


testcase town_learned_tags_route:
    $ _test.timeout = 220.0
    $ _test.transition_timeout = 0.08

    click "开始游戏"
    advance until screen "choice"
    $ player_name = "敖浔奕"
    $ tech_insight = 1
    $ gathered_supplies = False
    $ inspected_prototypes = False
    $ tested_accelerator = True
    $ persistent.town_route_opened = False
    run Jump("town_route_start")
    advance until screen "choice"
    click "靠近断裂护栏，听清他们的谈话"
    advance until screen "choice"
    click "只报姓名，不主动补充经历"
    advance until screen "choice"
    click "先让岚解释每个证件词的含义"
    advance until screen "choice"
    click "和岚一起复核货签"
    advance until screen "choice"
    click "告诉他一小部分真话"
    advance until eval persistent.town_route_opened timeout 30.0
    $ assert persistent.town_cover_story == "learned"
    $ assert persistent.town_work_choice == "tags"
    $ assert old_world_exposure == 1
    $ assert persistent.town_lan_affinity >= 5


testcase town_visual_qa:
    $ _test.timeout = 90.0
    $ _test.transition_timeout = 0.08

    click "开始游戏"
    advance until screen "choice"
    $ player_name = "敖浔奕"
    $ tech_insight = 2
    $ gathered_supplies = False
    $ inspected_prototypes = False
    $ tested_accelerator = False
    run Jump("town_route_start")
    advance until screen "choice"
    click "观察车辆和路面"
    advance until screen "choice"
    click "指出轮毂还会继续裂开"
    advance until "这里是灰桥城，荟屿国的首都。"
    pause 0.8
    screenshot "town/map-greybridge.png"
    advance until "我们现在在第 21 号王国公路上。"
    pause 0.9
    screenshot "town/map-road-21.png"
    advance until "我们此行正是前往灰桥城进行贸易。"
    pause 1.2
    screenshot "town/map-route-complete.png"
    advance until screen "choice"
    click "先让岚解释每个证件词的含义"
    advance until "你的尾巴……平时都从哪里出去？"
    screenshot "town/change-clothes.png"
    advance until screen "choice"
    click "协助衡叔加固车轴"
    advance until "穿过冷暗门洞的一瞬间"
    screenshot "town/first-city-view.png"
    advance until screen "town_short_permit_overlay"
    pause 0.5
    screenshot "town/short-permit.png"
