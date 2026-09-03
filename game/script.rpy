define judge = Character("审判长", color="#d6c1a7", ctc=ctc_paw, ctc_position="fixed")
define prosecutor = Character("公诉人", color="#c0c8d0", ctc=ctc_paw, ctc_position="fixed")
define researcher = Character("研究员", color="#b9eaff", ctc=ctc_paw, ctc_position="fixed")
define system = Character("设施系统", color="#ff7770", ctc=ctc_paw, ctc_position="fixed")
define unknown = Character("？？？", color="#aeb7bf", ctc=ctc_paw, ctc_position="fixed")
define ao = DynamicCharacter("player_name", color="#58dcff", ctc=ctc_paw, ctc_position="fixed")

default player_name = "ALPHA-01"
default court_response = ""
default resolve = 0
default caution = 0
default empathy = 0
default tech_insight = 0
default memory_fragments = 0
default inspected_terminal = False
default inspected_prototypes = False
default gathered_supplies = False
default tested_accelerator = False
default surface_plan = ""

label start:
    $ player_name = "ALPHA-01"
    $ court_response = ""
    $ resolve = 0
    $ caution = 0
    $ empathy = 0
    $ tech_insight = 0
    $ memory_fragments = 0
    $ inspected_terminal = False
    $ inspected_prototypes = False
    $ gathered_supplies = False
    $ tested_accelerator = False
    $ surface_plan = ""

    stop music fadeout 1.0
    stop ambience fadeout 1.0
    scene black with fade
    centered "旧纪元末期\n中华人民共和国\n某中级人民法院"

    scene bg defendant with dissolve
    show screen defendant_plaque_overlay
    play sound "audio/ui_ping.wav"

    prosecutor "被告人，法庭调查已经结束。"
    prosecutor "在宣判前，你是否还有最后陈述？"
    hide screen defendant_plaque_overlay with dissolve

    menu:
        "抗辩":
            $ court_response = "argue"
            $ resolve += 1
            "我抬起头。审判席上的三张脸背着光，只剩下端正而模糊的轮廓。"
            "我" "我承认已经发生的后果。但公诉人描述的动机，不是我的。"
            "我" "监控记录缺失了十二分钟。那不是空白，是你们至今没有回答的部分。"
            judge "你的异议已记录。现有证据足以形成完整证据链。"
            "审判长垂眼翻过一页。纸张擦过桌面的声音很轻，我知道这件事已经结束了。"

        "沉默":
            $ court_response = "silent"
            $ caution += 1
            "我看着桌前的名牌，没有开口。"
            "能说的话在此前的每一次讯问里都说尽了。剩下那些，他们不会听，我也不愿再交出去。"
            judge "法庭视为被告人放弃最后陈述。"

    judge "本院依法判决：数罪并罚，判处死刑，剥夺政治权利终身。"
    judge "判决宣告完毕。"

    hide screen defendant_plaque_overlay
    scene black with fade
    "脚镣被打开时，我以为他们终于准备执行。"
    "蒙眼布却没有摘下。车门合拢以后，轮胎驶过的也不是通往刑场的那段碎石路。"
    unknown "编号确认。原姓名从此停止使用。"
    "我" "这不在判决书里。"
    unknown "判决书处理的是一个死人。我们接收的是一批材料。"

    scene bg laboratory with dissolve
    researcher "ALPHA 批次共四名。神经结构耐受性筛选完成。"
    researcher "体态重构、感官扩展、尾部平衡反射……进入不可逆阶段。"
    researcher "ALPHA-01 的斯安威斯坦兼容框架接入成功。军用科技，篇章-VI。"
    researcher "灵力适配项目仍为空。"
    unknown "那不是本阶段的指标。先让他们活下来。"

    if court_response == "argue":
        "麻醉沿着手臂向上漫。我最后守住的，仍是那十二分钟——像一扇没有来得及推开的门。"
    else:
        "麻醉覆盖意识以前，我记住了最后离开的脚步声。那个人在门口停过一次，却没有回头。"

    scene bg cryo intact with fade
    researcher "四具原型体进入长期休眠。等待战争部署指令。"
    researcher "ALPHA-01 状态稳定。"
    system "休眠程序启动。"
    scene black with dissolve

    centered "人类没有等到部署指令。"
    centered "第 0 年\n全球指挥网络终止响应。最后一座人类城市熄灭。"
    centered "第 147 年\n一种后来被称作“灵力”的现象开始改变生态。"
    centered "第 311 年\n走兽第一次用完整的语言记录自己的名字。"
    centered "第 684 年\n聚落越过旧高速公路，在人类废墟之外建立城墙。"
    centered "第 1260 年\n王国、商路与新的历史相继诞生。"
    centered "第 2003 年\n地下七百二十米，一套早已无人维护的系统收到错误的生还授权。"

    scene bg cryo damaged
    with hpunch
    play sound "audio/ui_ping.wav"
    show screen facility_warning_overlay
    system "警告。主承重结构发生连续位移。"
    system "管理人员生命信号：零。"
    system "远程授权：未知。校验失败。"
    system "最终预案自授权通过。正在强制唤醒唯一可响应原型体。"
    hide screen facility_warning_overlay

    scene cg awakening with dissolve
    "冷先回到身体里。"
    "随后才是疼。它从后颈钻进脊柱，像一根烧红的针，被人沿着每一节骨缝缓慢推下去。"
    "我呛出第一口气，肺里全是药水和铁锈的味道。"
    system "ALPHA-01，苏醒程序已完成。"
    ao "……听得见。这里是哪？"
    "声音从我喉咙里出来，清亮、沙哑，又陌生得像隔着一堵墙传来。"
    "没有人回答。我扶住舱门站起，爪尖在金属表面刮出一道短促的锐响。"
    "那只手稳稳撑住了身体——至少，它听从我的意志。"
    ao "灯还亮着，空气能呼吸。先找出口。"

    scene bg corridor with dissolve
    "走廊尽头仍有一扇门亮着。两侧支路半掩在坍塌的墙板后。"
    "我朝最近的墙板敲了两下。回声沿空走廊滚远，除此以外，什么也没有回来。"
    ao "没人来接我。"
    "地面积了厚厚一层灰，只有我刚刚踩出的足迹。这里已经很久没有活人走动。"

    jump facility_explore

label facility_explore:
    scene bg corridor

    if inspected_terminal and (inspected_prototypes or gathered_supplies):
        ao "主控资料已经拿到。再看一处，我就离开。"
    else:
        "头顶的灯忽明忽暗。每多停一分钟，身后的门都可能再也打不开。"

    menu:
        "前往中央控制室" if not inspected_terminal:
            jump inspect_terminal

        "返回休眠舱，检查其余原型体" if not inspected_prototypes:
            jump inspect_prototypes

        "搜索医疗与应急物资" if not gathered_supplies:
            jump inspect_supplies

        "沿主通道前往出口" if inspected_terminal and (inspected_prototypes or gathered_supplies):
            jump approach_exit

label inspect_terminal:
    $ inspected_terminal = True
    $ tech_insight += 1
    scene bg control room with dissolve
    show screen facility_terminal_overlay
    system "本地恢复界面已解锁。"
    "屏幕只剩下最底层的维护页面。日期字段已经溢出，日志停在两千多年前。"
    "我把系统时间读了三遍。不是看不懂那些数字，只是不知道该把它们放进怎样的现实里。"
    ao "两千零三年……"
    "存活人员一栏是零。ALPHA-02、03、04 的生命信号，也都在漫长的记录中先后消失。"
    "如果时钟没有坏，那么这世上早已没有人记得我来过。"
    "出口图上，通往地表的维护通道仍显示微弱供电。"
    "我记下路线，把那串日期留在身后。眼下，出口比答案更要紧。"
    hide screen facility_terminal_overlay
    jump facility_explore

label inspect_prototypes:
    $ inspected_prototypes = True
    $ empathy += 1
    $ memory_fragments += 1
    scene bg cryo damaged with dissolve
    "三座后舱被同一段塌落的横梁压穿。监测灯早已熄灭。"
    "断裂的顶板还在细微作响。我停在安全线外，一一读出舱门上的编号。"
    ao "ALPHA-02。ALPHA-03。ALPHA-04。"
    "没有回答。我们躺得这样近，却连彼此的名字都没来得及知道。"
    "我伸手关掉反复报警的生命监测。红灯一盏接一盏熄灭，房间终于安静下来。"
    jump facility_explore

label inspect_supplies:
    $ gathered_supplies = True
    $ caution += 1
    scene bg medical storage with dissolve
    "医疗柜的密封条已经脆化。能使用的只剩止血凝胶、净水片和一卷复合绷带。"
    ao "药物不能信。绷带能用，水必须带走。"
    "我把能确认安全的物资装进旧应急袋。"
    if court_response == "silent":
        "墙后忽然传来一阵脚步似的闷响。我的手已经扣住柜门，身体先于意识屏住了呼吸。"
        "三秒以后，锈蚀的管道又震了一次。我才慢慢松开手。"
        $ memory_fragments += 1
    jump facility_explore

label approach_exit:
    scene bg corridor with dissolve
    "主通道尽头，维护梯一路向上。门边的镜面检修板映出一个陌生轮廓。"
    "从醒来起，我一直避开所有能够反光的东西。可再往前，已经没有地方可躲。"
    ao "……还有一件事，我必须看清。"

    scene cg pov hands with dissolve
    "我抬起双手。白色绒毛、蓝色肉垫，还有能在金属上留下划痕的爪尖。"
    "我屈起手指，再一根根松开。它们听从得太顺利，反而让那份陌生无处可逃。"
    ao "能动。也有感觉。"
    "掌心贴上冰冷的镜面时，触感真切得不容否认。"

    scene cg pov mirror with dissolve
    "我缓慢抬头。"
    "蓝色的角、过大的耳朵、陌生的眼睛。那张脸没有保留多少旧日的轮廓，却会在我屏住呼吸时同样僵住。"
    "我试着从记忆里找回原来的自己，最后只想起法庭名牌上那几个冰冷的字。至于那张脸，竟已经模糊了。"
    ao "……这就是我。"
    "尾巴不安地碰上身后的栏杆。我花了几次呼吸，才让它慢慢安静下来。"
    "过去的姓名留在判决书里。两千年过去，连替我保管它的人也不在了。"

    menu:
        "采用名字“敖浔奕”":
            $ player_name = "敖浔奕"

        "自己取一个名字":
            $ entered_name = renpy.input("从今以后，我叫——", default="", length=12).strip()
            if entered_name:
                $ player_name = entered_name
            else:
                $ player_name = "敖浔奕"

    ao "[player_name]。"
    "这个名字落进空走廊，轻得几乎没有回声。"
    if court_response == "argue":
        ao "不是编号，也不需要谁批准。"
    else:
        "我又念了一遍。第二次听见时，它已经比刚才更像自己的。"
    ao "先用它活下去。"
    "镜子里的人没有笑。我也没有勉强他。"

    scene bg corridor with dissolve
    "维护梯前还有最后一道自检。后颈深处的义体保持沉默，像一枚没有拆除保险的弹药。"

    menu:
        "进行最低功率神经加速测试":
            $ tested_accelerator = True
            $ tech_insight += 1
            "我把输出限制在百分之三。"
            "世界骤然放慢。坠落的灰尘悬在半空，警示灯的闪烁被拉成长长的红线。"
            "下一瞬间，恶心和耳鸣同时袭来。我立即切断连接。"
            ao "能用，也会把我拖垮。够了。"

        "不在未知环境中启动义体":
            $ caution += 1
            ao "我连这具身体能走多远都不知道。它留到真正需要的时候。"
            "后颈深处的义体继续沉默。现在，这反而让人安心。"

    jump surface_reveal

label surface_reveal:
    scene black with fade
    "升降机爬行了很久。最后一段路，我只能徒手推开变形的维护门。"
    "风先涌进来。带着草木、泥土和某种陌生花粉的气味。"

    scene bg surface with Fade(1.0, 0.5, 1.2)
    "旧高速公路断在森林里。更远处，城墙、塔楼与农田铺满山谷。"
    "两道飞龙的影子从云层下掠过，朝远方的王国而去。"
    "我停在门外，许久没有迈出第二步。"
    "我曾想过门外只剩焦土，或者什么都没有。却从没想过，世界会在不需要人类的日子里继续生长。"
    ao "设施时钟没有坏。"
    ao "消失的是我们。"
    "山谷里传来遥远的钟声。鸟群受惊飞起，很快又落回林间。世界没有回答，也不需要回答。"

    menu:
        "先观察通往王国的道路":
            $ surface_plan = "observe"
            $ caution += 1
            "我留在树影里，记录车辙、炊烟和城门开启的间隔。"
            ao "先看清他们怎样生活，再决定该怎样让他们看见我。"

        "带走设施离线核心" if tech_insight >= 2:
            $ surface_plan = "core"
            "我把掌心大小的离线核心固定在应急袋内侧。"
            "它未必能解释这个时代，却还保存着我熟悉的文字和声音。眼下，这就够了。"

        "在出口为其他原型体留下标记" if inspected_prototypes:
            $ surface_plan = "memorial"
            $ empathy += 1
            "我在门侧刻下四条短线，只把第一条延伸到地表。"
            "没有墓碑，也没有名字。但至少从此以后，不会只有我记得这里曾经躺着四个人。"

    $ persistent.prologue_cleared = True
    $ persistent.last_player_name = player_name
    $ persistent.last_surface_plan = surface_plan
    $ persistent.last_court_response = court_response
    $ persistent.last_caution = caution
    $ persistent.last_tech_insight = tech_insight
    $ persistent.unlocked_core_route = (tech_insight >= 2)
    $ persistent.remembered_prototypes = inspected_prototypes

    show screen prologue_complete_overlay with dissolve
    pause 1.2
    "两千年前，他们替我决定了何时死。"
    "两千年后，我第一次可以自己决定，要往哪里去。"
    hide screen prologue_complete_overlay with dissolve

    jump origin_route_select

label show_route_summary:
    scene bg surface
    $ response_text = "抗辩" if court_response == "argue" else "沉默"
    $ prototype_text = "已确认" if inspected_prototypes else "未确认"
    $ accelerator_text = "已测试" if tested_accelerator else "未启动"
    centered "苏醒记录\n姓名：[player_name]\n法庭回应：[response_text]\n原型体记录：[prototype_text]\n篇章-VI：[accelerator_text]\n技术洞察：[tech_insight]　审慎：[caution]　共情：[empathy]"
    return
