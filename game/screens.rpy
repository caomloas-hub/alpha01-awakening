################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox_chamfer.svg", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

transform choice_appear:
    alpha 0.0
    yoffset 18
    easeout 0.20 alpha 1.0 yoffset 0


screen choice(items):
    style_prefix "choice"
    modal True
    zorder 100

    key "game_menu" action ShowMenu("pause_menu")

    add Solid("#010711a6")

    vbox:
        at choice_appear

        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    xalign 0.5
    xsize 900
    yminimum 84

style choice_button_text is default:
    properties gui.text_properties("choice_button")
    xalign 0.5
    textalign 0.5


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    zorder 100

    if quick_menu:
        textbutton _("菜单"):
            style "quick_button"
            xalign 0.985
            yalign 0.98
            action ShowMenu("pause_menu")


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = False

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Pause Menu ##################################################################

define _game_menu_screen = "pause_menu"


screen pause_menu():

    tag menu
    modal True
    zorder 200
    style_prefix "pause"

    add Solid("#010610d9")

    key "game_menu" action Return()

    frame:
        style "pause_panel"

        hbox:
            spacing 54

            vbox:
                xsize 330

                text _("PAUSED") style "pause_eyebrow"
                text _("暂停") style "pause_title"
                null height 10
                add Solid(gui.accent_color) xsize 88 ysize 3
                null height 26
                text _("设施仍在低鸣。\n你的选择和名字都留在这里。") style "pause_hint"

                null height 150

                textbutton _("继续游戏"):
                    style "pause_resume_button"
                    action Return()

                null height 18

                textbutton _("退出游戏"):
                    style "pause_minor_button"
                    action Quit(confirm=True)

            vbox:
                spacing 24

                text _("功能") style "pause_section"

                grid 2 3:
                    spacing 18

                    textbutton _("保存进度") action ShowMenu("save")
                    textbutton _("读取进度") action ShowMenu("load")
                    textbutton _("对话记录") action ShowMenu("history")
                    textbutton _("游戏设置") action ShowMenu("preferences")
                    textbutton _("苏醒记录") action ShowMenu("endings")
                    textbutton _("返回标题") action MainMenu(confirm=True)

                null height 16
                text _("快捷操作") style "pause_section"

                hbox:
                    spacing 12

                    textbutton _("快速保存"):
                        style "pause_small_button"
                        action QuickSave()

                    textbutton _("快速读取"):
                        style "pause_small_button"
                        action QuickLoad()

                    textbutton _("自动播放"):
                        style "pause_small_button"
                        action [Preference("auto-forward", "toggle"), Return()]

                text _("Esc / 右键：返回游戏　　Ctrl：快进　　滚轮：回退") style "pause_footer"


style pause_panel is frame:
    xalign 0.5
    yalign 0.5
    xsize 1180
    ysize 720
    left_padding 58
    right_padding 58
    top_padding 52
    bottom_padding 48
    background Solid("#061524")

style pause_eyebrow is gui_text:
    size 20
    color "#5edcf6"
    kerning 5

style pause_title is gui_text:
    size 64
    color "#f4fbff"

style pause_hint is gui_text:
    size 24
    color "#9fb5c8"
    line_spacing 8

style pause_section is gui_text:
    size 22
    color "#6edcf2"

style pause_button is button:
    xsize 300
    ysize 74
    left_padding 24
    right_padding 24
    background Solid("#0a2236d9")
    hover_background Solid("#10506ae8")

style pause_button_text is button_text:
    size 28
    color "#d9e8f1"
    hover_color "#ffffff"
    xalign 0.5
    textalign 0.5

style pause_resume_button is pause_button:
    xsize 300
    ysize 86
    background Solid("#0b506be8")
    hover_background Solid("#1683a0f2")

style pause_resume_button_text is pause_button_text:
    size 31

style pause_minor_button is pause_button:
    xsize 300
    ysize 58
    background Solid("#091827c8")
    hover_background Solid("#4b2635e8")

style pause_minor_button_text is pause_button_text:
    size 23
    color "#9fb5c8"

style pause_small_button is pause_button:
    xsize 192
    ysize 58

style pause_small_button_text is pause_button_text:
    size 22

style pause_footer is gui_text:
    size 19
    color "#71889c"


## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("开始游戏") action Start()

        else:

            textbutton _("对话记录") action ShowMenu("history")

            textbutton _("保存进度") action ShowMenu("save")

        textbutton _("读取进度") action ShowMenu("load")

        textbutton _("设置") action ShowMenu("preferences")

        textbutton _("苏醒记录") action ShowMenu("endings")

        if _in_replay:

            textbutton _("结束回放") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("返回标题") action MainMenu()

        textbutton _("关于") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("操作帮助") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and Web.
            textbutton _("退出") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

image main_menu_slide_kingdom = Transform("gui/main_menu.png", xysize=(1920, 1080))
image main_menu_slide_awakening = Transform("images/backgrounds/cg-alpha01-awakening.png", xysize=(1920, 1080))
image main_menu_slide_hands = Transform("images/backgrounds/cg-alpha01-pov-hands-v2.png", xysize=(1920, 1080))
image main_menu_slide_mirror = Transform("images/backgrounds/cg-alpha01-pov-mirror-v2.png", xysize=(1920, 1080))

default main_menu_departing = None

image main_menu_cg_slideshow:
    "main_menu_slide_kingdom"
    pause 9.0
    "main_menu_slide_awakening" with Dissolve(1.25)
    pause 9.0
    "main_menu_slide_hands" with Dissolve(1.25)
    pause 9.0
    "main_menu_slide_mirror" with Dissolve(1.25)
    pause 9.0
    "main_menu_slide_kingdom" with Dissolve(1.25)
    repeat


transform main_landing_button_ready:
    subpixel True

    on idle:
        easeout 0.16 xoffset 0

    on hover:
        easeout 0.16 xoffset 10


transform main_landing_button_selected:
    subpixel True
    alpha 1.0
    xoffset 0
    easeout 0.18 xoffset 14


transform main_landing_button_depart(button_index):
    subpixel True
    alpha 1.0
    xoffset 0
    pause (0.025 * button_index)
    easein 0.27 xoffset -118 alpha 0.0


transform main_social_button_motion:
    subpixel True

    on idle:
        easeout 0.14 yoffset 0

    on hover:
        easeout 0.14 yoffset -9


screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    on "show" action SetVariable("main_menu_departing", None)

    style_prefix "main_menu"

    add "main_menu_cg_slideshow"
    add Transform(
        Crop((50, 120, 770, 750), "gui/main_menu_chrome_v3.png"),
        zoom=0.73,
        xpos=40,
        ypos=90,
    )
    add Transform(
        Crop((1150, 750, 470, 170), "gui/main_menu_chrome_v3.png"),
        zoom=0.88,
        xalign=1.0,
        yalign=1.0,
        xoffset=-40,
        yoffset=-32,
    )

    textbutton _("开始游戏"):
        style "main_landing_button"
        at (main_landing_button_ready if main_menu_departing == None else main_landing_button_selected if main_menu_departing == 0 else main_landing_button_depart(0))
        xpos 62
        ypos 112
        xsize 414
        action [
            SetVariable("main_menu_departing", 0),
            Pause(0.34),
            Start(),
        ]

    textbutton _("读取进度"):
        style "main_landing_button"
        at (main_landing_button_ready if main_menu_departing == None else main_landing_button_selected if main_menu_departing == 1 else main_landing_button_depart(1))
        xpos 86
        ypos 222
        xsize 410
        action [
            SetVariable("main_menu_departing", 1),
            Pause(0.34),
            ShowMenu("load"),
        ]

    textbutton _("游戏设置"):
        style "main_landing_button"
        at (main_landing_button_ready if main_menu_departing == None else main_landing_button_selected if main_menu_departing == 2 else main_landing_button_depart(2))
        xpos 112
        ypos 325
        xsize 406
        action [
            SetVariable("main_menu_departing", 2),
            Pause(0.34),
            ShowMenu("preferences"),
        ]

    textbutton _("苏醒记录"):
        style "main_landing_button"
        at (main_landing_button_ready if main_menu_departing == None else main_landing_button_selected if main_menu_departing == 3 else main_landing_button_depart(3))
        xpos 140
        ypos 428
        xsize 402
        action [
            SetVariable("main_menu_departing", 3),
            Pause(0.34),
            ShowMenu("endings"),
        ]

    textbutton _("退出游戏"):
        style "main_landing_exit_button"
        at (main_landing_button_ready if main_menu_departing == None else main_landing_button_selected if main_menu_departing == 4 else main_landing_button_depart(4))
        xpos 170
        ypos 529
        xsize 398
        action Show(
            "confirm",
            message="Are you sure you want to quit?",
            yes_action=[
                Hide("confirm"),
                SetVariable("main_menu_departing", 4),
                Pause(0.34),
                Quit(confirm=False),
            ],
            no_action=Hide("confirm"),
        )

    button:
        style "main_social_button"
        at main_social_button_motion
        xalign 1.0
        yalign 1.0
        xoffset -316
        yoffset -48
        tooltip _("X / @Furry_Xunyi")
        action OpenURL("https://x.com/Furry_Xunyi")

    button:
        style "main_social_button"
        at main_social_button_motion
        xalign 1.0
        yalign 1.0
        xoffset -187
        yoffset -48
        tooltip _("抖音 / Furry_Xunyi")
        action OpenURL("https://v.douyin.com/afT-TbA2v3c/")

    button:
        style "main_social_button"
        at main_social_button_motion
        xalign 1.0
        yalign 1.0
        xoffset -58
        yoffset -48
        tooltip _("关于制作组（施工中）")
        action NullAction()

    $ social_tooltip = GetTooltip()

    if social_tooltip:
        frame:
            style "main_social_tooltip"

            text social_tooltip:
                style "main_social_tooltip_text"

    text "version [config.version!t]":
        style "main_landing_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xsize 960
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


style main_landing_button is button:
    ysize 88
    background None
    hover_background Solid("#27ddff14")
    insensitive_background None
    hover_sound "audio/ui_ping.wav"
    left_padding 38
    right_padding 34

style main_landing_button_text is button_text:
    font "fonts/SourceHanSansLite.ttf"
    size 29
    color "#c8dce8"
    hover_color "#ffffff"
    outlines [(2, "#06121edd", 0, 1), (1, "#26d9ff55", 0, 0)]
    xalign 0.47
    yalign 0.5
    textalign 0.5

style main_landing_exit_button is main_landing_button:
    hover_sound "audio/ui_ping.wav"

style main_landing_exit_button_text is main_landing_button_text:
    color "#aebbc6"
    hover_color "#ff8f91"

style main_social_button is button:
    xsize 118
    ysize 118
    background None
    hover_background None
    hover_sound "audio/ui_ping.wav"

style main_social_tooltip is frame:
    xalign 1.0
    yalign 1.0
    xoffset -52
    yoffset -194
    xsize 426
    ysize 44
    background Solid("#04111ed9")
    padding (15, 6)

style main_social_tooltip_text is gui_text:
    font "fonts/SourceHanSansLite.ttf"
    size 19
    color "#9eeeff"
    xalign 1.0
    textalign 1.0

style main_landing_version is gui_text:
    xalign 0.0
    yalign 1.0
    xoffset 64
    yoffset -34
    font "fonts/SourceHanSansLite.ttf"
    size 20
    color "#79aebe"
    outlines [(1, "#03101add", 0, 1)]
    kerning 2


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background

        frame:
            style "game_menu_outer_frame"

            hbox:
                frame:
                    style "game_menu_navigation_frame"

                frame:
                    style "game_menu_content_frame"

                    if scroll == "viewport":
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True
                            side_yfill True

                            vbox:
                                transclude

                    elif scroll == "vpgrid":
                        vpgrid:
                            cols 1
                            yinitial 1.0
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True
                            side_yfill True
                            transclude

                    else:
                        transclude

        use navigation

        textbutton _("返回"):
            style "return_button"
            action Return()

        label title
        key "game_menu" action ShowMenu("main_menu")

    else:
        add Solid("#010610")

        frame:
            style "secondary_panel"

            label title:
                style "secondary_title"

            frame:
                style "secondary_content"

                if scroll == "viewport":
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial 1.0
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude

                else:
                    transclude

        textbutton _("返回暂停"):
            style "secondary_back_button"
            action ShowMenu("pause_menu")

        key "game_menu" action ShowMenu("pause_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

style secondary_panel is frame:
    xalign 0.5
    yalign 0.5
    xsize 1680
    ysize 940
    left_padding 56
    right_padding 56
    top_padding 118
    bottom_padding 44
    background Solid("#061524")

style secondary_title is label:
    xpos 56
    ypos 34

style secondary_title_text is gui_label_text:
    size 42
    color "#78e8ff"

style secondary_content is frame:
    xfill True
    yfill True
    background None

style secondary_back_button is button:
    xpos 176
    ypos 78
    xsize 210
    ysize 52
    background Solid("#0a2236d9")
    hover_background Solid("#10506ae8")

style secondary_back_button_text is button_text:
    size 22
    color "#a9bfd0"
    hover_color "#ffffff"
    xalign 0.5


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("[config.version!t]\n")

            text _("个人像素视觉小说原型。剧情、界面与生成美术均服务于本项目。")
            text _("\n使用 {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 制作。")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

style about_small:
    size 20
    minwidth 260
    textalign 1.0
    yalign 0.9


## Ending Record screen ########################################################

screen endings():

    tag menu

    use game_menu(_("苏醒记录"), scroll="viewport"):

        vbox:
            spacing 36

            label _("序章")

            if persistent.prologue_cleared:
                text _("苏醒记录  —  已完成") color gui.accent_color
                text _("最近使用的名字：[persistent.last_player_name or '敖浔奕']")
                text _("ALPHA-01 已离开地下设施，并第一次看见两千年后的王国。")
            else:
                text _("苏醒记录  —  未完成") color gui.idle_small_color

            null height 30
            label _("跨章节条件")

            if persistent.unlocked_core_route:
                text _("离线核心路线  —  已解锁") color gui.accent_color
                text _("未来章节中，与旧时代技术有关的隐藏选项可以出现。")
            else:
                text _("离线核心路线  —  未解锁") color gui.idle_small_color

            if persistent.remembered_prototypes:
                text _("原型体记录  —  已保留") color gui.accent_color
                text _("ALPHA-02 至 ALPHA-04 的存在将影响后续记忆与身份选择。")
            else:
                text _("原型体记录  —  未发现") color gui.idle_small_color


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("保存进度"))


screen load():

    tag menu

    use file_slots(_("读取进度"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d  %H:%M"), empty=_("空存档")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()
                key "save_page_prev" action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()
                key "save_page_next" action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("设置"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("显示")
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("全屏") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("快进")
                    textbutton _("未读文本") action Preference("skip", "toggle")
                    textbutton _("选项后继续") action Preference("after choices", "toggle")
                    textbutton _("保留转场") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("文字速度")

                    bar value Preference("text speed")

                    label _("自动播放间隔")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("音乐音量")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("音效音量")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("试听") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 340

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("对话记录"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("还没有对话记录。")

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("操作帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

init python:
    def localize_confirm_message(message):
        messages = {
            "Are you sure you want to delete this save?": "确定删除这个存档吗？",
            "Are you sure you want to overwrite your save?": "确定覆盖这个存档吗？",
            "Loading will lose unsaved progress.\nAre you sure you want to do this?": "读取存档会丢失未保存的进度。\n确定继续吗？",
            "Are you sure you want to quit?": "确定退出游戏吗？",
            "Are you sure you want to return to the main menu?\nThis will lose unsaved progress.": "确定返回标题画面吗？\n未保存的进度将会丢失。",
            "Are you sure you want to end the replay?": "确定结束回放吗？",
            "Are you sure you want to begin skipping?": "确定开始快进吗？",
        }
        return messages.get(message, message)


screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label localize_confirm_message(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("确定") action yes_action
                textbutton _("取消") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("快进中")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:
        textbutton _("菜单"):
            style "quick_button"
            xalign 0.97
            yalign 0.97
            action ShowMenu("pause_menu")


style window:
    variant "small"
    background Image("gui/phone/textbox_chamfer.svg", xalign=0.5, yalign=1.0)

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 870

style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600

# Shrink the title.
style main_menu_vbox:
    variant "small"
    xsize 900
