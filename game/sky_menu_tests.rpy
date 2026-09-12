testcase sky_menu_navigation:
    $ _test.timeout = 45.0
    pause 3.0
    $ assert sky_menu_seen
    screenshot "sky-menu-idle.png"
    click pos (960,865)
    advance until screen "preferences"
    keysym "K_ESCAPE"
    advance until screen "main_menu"
    click pos (130,1000)
    advance until screen "load"
    keysym "K_ESCAPE"
    advance until screen "main_menu"
    click pos (330,1000)
    advance until screen "endings"
    keysym "K_ESCAPE"
    advance until screen "main_menu"
    click pos (1270,865)
    advance until screen "confirm"
    click "取消"
    click pos (650,865)
    advance until screen "choice"
    keysym "K_ESCAPE"
    advance until screen "pause_menu"

testcase sky_menu_intro:
    $ _test.timeout = 20.0
    pause .9
    screenshot "sky-menu-intro-09.png"
    pause .55
    screenshot "sky-menu-intro-15.png"
    pause .8
    screenshot "sky-menu-intro-23.png"
    pause 1.0
    screenshot "sky-menu-intro-settled.png"
    $ assert sky_menu_seen
    click "动效：开"
    $ assert persistent.sky_menu_reduced_motion
    screenshot "sky-menu-reduced.png"
    click "游戏设置"
    advance until screen "preferences"
    keysym "K_ESCAPE"
    advance until screen "main_menu"
    click "动效：关"
    $ assert not persistent.sky_menu_reduced_motion

testcase sky_menu_skip:
    $ _test.timeout = 20.0
    pause .15
    click pos (650,865)
    pause .1
    $ assert sky_menu_seen
    $ assert renpy.get_screen("main_menu")
    $ assert not renpy.get_screen("choice")
    click "开始游戏"
    advance until screen "choice"

testcase sky_menu_save_restore:
    $ _test.timeout = 35.0
    pause 3.0
    click "开始游戏"
    advance until screen "choice"
    click "抗辩"
    advance until screen "choice"
    $ assert store.court_response == "argue" and store.resolve == 1
    keysym "K_ESCAPE"
    advance until screen "pause_menu"
    click "保存进度"
    advance until screen "save"
    run FileSave(1, page="99", confirm=False)
    pause .5
    $ assert renpy.can_load("99-1")
    run MainMenu(confirm=False)
    advance until screen "main_menu"
    $ assert store.court_response == ""
    click "读取进度"
    advance until screen "load"
    run FileLoad(1, page="99", confirm=False)
    pause 1.0
    $ assert store.court_response == "argue" and store.resolve == 1
    $ assert renpy.get_screen("choice")

testcase sky_menu_social:
    $ _test.timeout = 20.0
    pause 3.0
    screenshot "sky-menu-social-idle.png"
    move pos (1628,999)
    pause .3
    $ assert GetTooltip() == "X / @Furry_Xunyi"
    screenshot "sky-menu-social-hover.png"
    $ renpy.queue_event("focus_right")
    pause .3
    $ assert GetTooltip() == "抖音", repr(GetTooltip())
    $ renpy.queue_event("focus_right")
    pause .3
    $ assert GetTooltip() == "制作组（施工中）"
    $ renpy.queue_event("button_select")
    $ assert renpy.get_screen("main_menu")
    click "动效：开"
    move pos (1836,999)
    pause .3
    $ assert persistent.sky_menu_reduced_motion
    $ assert GetTooltip() == "制作组（施工中）"
    screenshot "sky-menu-social-reduced.png"

testcase sky_menu_keyboard:
    $ _test.timeout = 20.0
    pause .15
    keysym "K_RETURN"
    pause .2
    $ assert sky_menu_seen and renpy.get_screen("main_menu")
    # Keysym test nodes move the mouse first; queue mapped keyboard events
    # directly so this test does not replace keyboard focus with mouse focus.
    run renpy.queue_event("focus_right")
    pause .3
    run renpy.queue_event("button_select")
    advance until screen "endings"
    keysym "K_ESCAPE"
    advance until screen "main_menu"
    run renpy.queue_event("focus_up")
    pause .3
    run renpy.queue_event("focus_right")
    pause .3
    screenshot "sky-menu-keyboard-focus.png"
    run renpy.queue_event("button_select")
    advance until screen "preferences"
    keysym "K_ESCAPE"
    advance until screen "main_menu"
