define config.name = _("ALPHA-01：苏醒记录")
define gui.show_name = True
define config.version = "0.2.0"
define build.name = "alpha01_awakening_town_route_v020"
define config.window_title = "ALPHA-01：苏醒记录 v0.2.0"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.sample_sound = "audio/ui_ping.wav"

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = dissolve
define config.end_game_transition = fade

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 30
default preferences.auto_forward_time = 10

define config.save_directory = "alpha01-awakening-prologue-20260829"
define config.default_fullscreen = False
define config.game_menu_action = ShowMenu("pause_menu")

init python:
    config.keymap["game_menu"] = ["K_ESCAPE", "K_MENU", "K_PAUSE", "mouseup_3"]
    renpy.music.register_channel("ambience", "sfx", loop=True)
    renpy.music.register_channel("crowd", "sfx", loop=False)
    build.classify("design/**", None)
    build.classify("tests/**", None)
    build.classify("dist/**", None)
    build.classify("game/testcases.rpy", None)
    build.classify("game/testcases.rpyc", None)
    build.classify("log.txt", None)
    build.classify("test-*.txt", None)
    build.classify("test-*.log", None)
    build.classify("traceback.txt", None)
    build.classify("errors.txt", None)
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("game/**.rpy", "archive")
    build.classify("game/**.rpyc", "archive")
    build.classify("game/images/**", "archive")
    build.classify("game/audio/**", "archive")
    build.documentation("README.md")
