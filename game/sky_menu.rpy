# Sunny ruins menu. Legacy screen/assets intentionally retained for comparison.
default persistent.sky_menu_reduced_motion = False

init python:
    import math

    # Process-local: returning from submenus never replays the entrance.
    sky_menu_seen = False
    SKY_ROOT = "gui/sky-menu-v1/"

    def sky_label(index, width, height):
        # Tight, explicit source crops keep all letters and remove only padding.
        boxes = [(100,180,320,190), (610,180,320,190),
                 (100,650,310,190), (525,650,480,190),
                 (30,1120,475,195), (560,1120,440,195)]
        return Transform(Crop(boxes[index], SKY_ROOT + "buttons.png"),
                         xysize=(width,height), nearest=True)

    sky_logo = Transform(Crop((20,95,2135,505), SKY_ROOT + "title.png"),
                         xysize=(1080,255), nearest=True)

    def sky_dragon_frame(index):
        # Normalize the contact baseline rather than positioning by image centre.
        baseline = [484,484,507,420,420,420][index]
        return Transform(Crop(((index % 3)*512,(index // 3)*512,512,512),
                              SKY_ROOT + "dragon.png"),
                         xysize=(300,300), yoffset=int((420-baseline)*300/512),
                         nearest=True)

    def sky_dragon_pose(st, at):
        if st < 1.0:
            index = int(st / .13) % 2
        elif st < 1.35:
            index = 2
        elif st < 1.52:
            index = 3
        elif st < 1.72:
            index = 4
        else:
            index = 5
        return sky_dragon_frame(index), (.05 if st < 1.8 else None)

    class SkyRipple(renpy.Displayable):
        """Localized integer-pixel water distortion; no scene-wide wobble."""
        def __init__(self, child, w, h, strength=3, **kwargs):
            super(SkyRipple, self).__init__(**kwargs)
            self.child = renpy.displayable(child)
            self.w, self.h, self.strength = w, h, strength

        def render(self, width, height, st, at):
            source = renpy.render(self.child, self.w, self.h, st, at)
            rv = renpy.Render(self.w, self.h)
            for y in range(0, self.h, 6):
                offset = int(math.sin(y*.06 + st*1.1)*self.strength)
                rv.blit(source.subsurface((0,y,self.w,min(6,self.h-y))), (offset,y))
            renpy.redraw(self, .05)
            return rv

        def visit(self):
            return [self.child]

    def sky_finish_intro():
        global sky_menu_seen
        sky_menu_seen = True

    class SkyMotes(renpy.Displayable):
        def render(self, width, height, st, at):
            rv = renpy.Render(1920,1080)
            canvas = rv.canvas()
            for i in range(10):
                x = int((i*197+st*(7+i%3))%1920)
                y = int(110+(i*113)%660+math.sin(st*.35+i)*18)
                canvas.rect((255,250,213,110),(x,y,3+i%2,3+i%2))
            renpy.redraw(self,.05)
            return rv

transform sky_reveal(delay=0.0, duration=.8):
    alpha 0.0
    pause delay
    linear duration alpha 1.0

transform sky_dragon_arrive:
    subpixel True
    xoffset 520
    yoffset -470
    pause .8
    easeout 1.0 xoffset 90 yoffset -130
    easein .35 xoffset 0 yoffset 0
    pause .17
    easeout .2 yoffset 0

image sky_dragon_animated:
    Null(300,300)
    pause .8
    DynamicDisplayable(sky_dragon_pose)

transform sky_button_motion:
    on idle:
        easeout .14 yoffset 0 matrixcolor BrightnessMatrix(0)
    on hover:
        easeout .14 yoffset -5 matrixcolor BrightnessMatrix(.10)

transform sky_cloud_drift:
    xoffset 0
    linear 45.0 xoffset 100
    linear 45.0 xoffset 0
    repeat

transform sky_exit:
    alpha 0.0
    linear .35 alpha 1.0

transform sky_static:
    alpha 1.0

transform sky_darkness:
    alpha 1.0
    linear 1.2 alpha 0.0

screen sky_picture_button(label, index, action, width=160, height=86):
    button:
        style "sky_button"
        xysize (width,height)
        at (sky_static if persistent.sky_menu_reduced_motion else sky_button_motion)
        action action
        tooltip label
        alt label
        default_focus (index == 0)
        add sky_label(index,width-12,height-12) align (.5,.5)
        # Preserve existing text-targeted automation without drawing a second label.
        text label size 1 color "#ffffff00"

screen sky_social_icon(label, index, action):
    button:
        style "sky_button"
        xysize (88,88)
        action action
        alt label
        tooltip label
        add Transform(Crop((index*724,0,724,724), SKY_ROOT + "social-icons-v1.png"), xysize=(80,80), nearest=True):
            align (.5,.5)
            at (sky_static if persistent.sky_menu_reduced_motion else sky_button_motion)
        text label size 1 color "#ffffff00"

screen main_menu():
    tag menu
    default ready = sky_menu_seen or persistent.sky_menu_reduced_motion
    default leaving = False
    $ quiet = persistent.sky_menu_reduced_motion
    $ animate = not ready

    add Transform(SKY_ROOT + "background.png", xysize=(1920,1080))
    add Transform(SKY_ROOT + "cloud.png", xysize=(470,157), alpha=.55) xpos 410 ypos 70 at (sky_static if quiet else sky_cloud_drift)
    if not quiet:
        add SkyRipple(Crop((0,650,1920,430), Transform(SKY_ROOT + "background.png", xysize=(1920,1080))),1920,430,2) ypos 650
        add SkyMotes()

    # The reflected title stays below the logo and never displaces the controls.
    if quiet:
        add Transform(sky_logo, yzoom=-.60, alpha=.28) xpos 420 ypos 675
    else:
        add SkyRipple(Transform(sky_logo, yzoom=-.60, alpha=.28),1080,153,5) xpos 420 ypos 675

    add sky_logo xpos 420 ypos 420 at (sky_reveal(.15,.7) if animate else sky_static)
    if animate:
        add "sky_dragon_animated" xpos 885 ypos 210 at sky_dragon_arrive
    else:
        add sky_dragon_frame(5) xpos 885 ypos 210

    if not ready:
        # One click/Enter finishes the animation; it cannot also start a new game.
        add Solid("#071c29") at sky_darkness
        timer 2.7 action [Function(sky_finish_intro), SetScreenVariable("ready",True)]
        key "dismiss" action [Function(sky_finish_intro), SetScreenVariable("ready",True)]
    else:
        hbox:
            xalign .5
            ypos 825
            spacing 150
            at (sky_static if quiet else sky_reveal(0,.25))
            use sky_picture_button("开始游戏",0,SetScreenVariable("leaving",True))
            use sky_picture_button("游戏设置",1,ShowMenu("preferences"))
            use sky_picture_button("退出游戏",2,Quit(confirm=True))

        hbox:
            xpos 40
            ypos 965
            spacing 20
            use sky_picture_button("读取进度",3,ShowMenu("load"),180,70)
            use sky_picture_button("苏醒记录",4,ShowMenu("endings"),180,70)

        hbox:
            xalign 1.0
            xoffset -40
            ypos 955
            spacing 16
            use sky_social_icon("X / @Furry_Xunyi",0,OpenURL("https://x.com/Furry_Xunyi"))
            use sky_social_icon("抖音",1,OpenURL("https://v.douyin.com/afT-TbA2v3c/"))
            use sky_social_icon("制作组（施工中）",2,NullAction())

        $ social_tip = GetTooltip()
        if social_tip in ("X / @Furry_Xunyi", "抖音", "制作组（施工中）"):
            frame:
                xalign 1.0
                xoffset -40
                ypos 898
                background Solid("#123b46ee")
                padding (16,10)
                text social_tip size 24 color "#fff1cb"

        textbutton ("动效：关" if quiet else "动效：开"):
            style "sky_motion_option"
            xpos 40 ypos 30
            action ToggleField(persistent,"sky_menu_reduced_motion")

    text "version [config.version!t]":
        xpos 1660 ypos 34 size 24 color "#183d4d"

    if leaving:
        add Solid("#07131c") at sky_exit
        button:
            xfill True yfill True
            action NullAction()
        timer .36 action Start()

style sky_button is button:
    background None
    hover_background Solid("#fff7d52c")
    padding (0,0)
    hover_sound "audio/ui_hover_soft.wav"
    activate_sound "audio/ui_confirm_soft.wav"

style sky_social is button:
    xminimum 82
    yminimum 70
    background None
    hover_background Solid("#fff7d580")

style sky_social_text is button_text:
    color "#173e4c"
    hover_color "#8a5319"
    size 28
    outlines [(1,"#ffffdd",0,0)]

style sky_motion_option is sky_social:
    yminimum 48

style sky_motion_option_text is sky_social_text:
    size 22
