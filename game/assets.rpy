image bg defendant = Transform("images/backgrounds/cg-defendant-nameplate-v2.png", xysize=(1920, 1080))
image bg laboratory = Transform("images/backgrounds/bg-alpha-laboratory.png", xysize=(1920, 1080))
image bg control room = Transform("images/backgrounds/bg-abandoned-control-room-v2.png", xysize=(1920, 1080))
image bg medical storage = Transform("images/backgrounds/bg-abandoned-medical-storage-v2.png", xysize=(1920, 1080))
image bg cryo intact = Transform("images/backgrounds/bg-cryo-room-intact.png", xysize=(1920, 1080))
image bg cryo damaged = Transform("images/backgrounds/bg-cryo-room-damaged.png", xysize=(1920, 1080))
image bg corridor = Transform("images/backgrounds/bg-damaged-facility-corridor.png", xysize=(1920, 1080))
image bg surface = Transform("images/backgrounds/bg-surface-kingdom.png", xysize=(1920, 1080))
image cg awakening = Transform("images/backgrounds/cg-alpha01-awakening.png", xysize=(1920, 1080))
image cg pov hands = Transform("images/backgrounds/cg-alpha01-pov-hands-v2.png", xysize=(1920, 1080))
image cg pov mirror = Transform("images/backgrounds/cg-alpha01-pov-mirror-v2.png", xysize=(1920, 1080))

transform soft_shake:
    linear 0.04 xoffset -8
    linear 0.05 xoffset 7
    linear 0.04 xoffset -5
    linear 0.05 xoffset 4
    linear 0.04 xoffset 0

screen facility_warning_overlay():
    zorder 25
    frame:
        xalign 0.5
        yalign 0.14
        xsize 1350
        ysize 170
        background Solid("#16080be6")
        padding (32, 20)

        vbox:
            xalign 0.5
            spacing 8
            text "警告：结构稳定性低于安全阈值" xalign 0.5 size 34 color "#ff6d67"
            text "未知授权源已接管　｜　最终预案执行中　｜　休眠舱强制开启" xalign 0.5 size 26 color "#d9bbc0"

screen facility_terminal_overlay():
    zorder 15
    frame:
        xalign 0.16
        yalign 0.18
        xsize 650
        ysize 430
        background Solid("#03141ced")
        padding (34, 28)

        vbox:
            spacing 17
            text "ARES // LOCAL RECOVERY" size 25 color "#72e8ff"
            add Solid("#23677d") xsize 580 ysize 2
            text "设施状态　严重损毁" size 28 color "#d8f8ff"
            text "外部通信　离线" size 28 color "#d8f8ff"
            text "存活人员　0" size 28 color "#ff8d85"
            text "原型体　　ALPHA-01 / 唤醒" size 28 color "#d8f8ff"
            text "ALPHA-02—04 / 生命信号丢失" size 28 color "#a3abb2"
            text "系统历　　溢出（推定休眠 2000 年以上）" size 25 color "#f2cc7d"

screen prologue_complete_overlay():
    zorder 30
    add Solid("#00000099")
    vbox:
        xalign 0.5
        yalign 0.44
        spacing 18
        text "PROLOGUE COMPLETE" xalign 0.5 size 26 color "#77e7ff" kerning 6
        text "苏醒记录" xalign 0.5 size 72 color "#ffffff"
        text "ALPHA-01 已离开地下设施" xalign 0.5 size 28 color "#c3d6df"
