label town_route_start:
    stop music fadeout 0.8
    stop ambience fadeout 0.8
    $ origin_route = "town"
    $ town_outfit = False
    $ town_permit = False
    $ town_cover_story = ""
    $ town_work_choice = ""
    $ caravan_trust = 0
    $ lan_affinity = 0
    $ old_world_exposure = 0
    $ town_money = 0
    $ town_bed = ""
    $ town_permit_id = "GC-21-0307"

    scene black with fade
    centered "第一章　借名入城"
    jump town_t01_tracks


label town_t01_tracks:
    scene town road day with Fade(0.8, 0.3, 1.0)
    play ambience "audio/ambience/old_kingdom_road_wind.ogg" fadein 2.0 volume 0.16
    "我没有立刻走上公路。"
    "林缘还能替我遮住身形；一旦踏进开阔地，先开口的人便未必是我。"
    "断裂护栏外的泥土里留着三组新车辙。轮距接近，深浅不同，说明车队载重不一；最外侧还混着成排脚印。"
    "车辙沿旧高速留下的笔直路基向东北延伸。杂草一层压着一层——这条路从未真正荒废。"
    "风从路那头送来人声。发音已经陌生，句子的骨架却仍旧熟悉，像一封隔了太久才送到的信。"
    unknown "……西门……落锁以前……后车……"
    "我只能辨清七成。他们在赶路；至于我该不该被他们看见，还需要再等一会儿。"

    menu:
        "保持距离，先数清人数":
            $ caution += 1
            "我沿树影平行移动。篷车三辆，能看见的成年成员六名。"
            "走在最前的是一名宽角牦牛；后车旁的野猪明显把重心避开左脚；赤狐少年抱着一叠木签，在车与车之间来回核对。"
            "领队、车把式、记账员。每个人都有固定的位置，武器也都收在便于取用、却不会随时出鞘的地方。"

        "靠近断裂护栏，听清他们的谈话":
            $ lan_affinity += 1
            "我借护栏与高草遮住身体，靠近到能听清那个赤狐少年的声音。"
            lan "盐砖十二，蓝布六卷，药草箱两只。后车少一枚封签，不是少一箱货。"
            heng "你再念一遍，它也不会自己长回来。"
            lan "但进城以后，少一枚签就会被当成少一箱货。到时候是我挨骂。"
            "他说得很快，手指也一直压着那处空缺，却没有报错一个数。"

        "观察车辆和路面" if tech_insight >= 2:
            $ caravan_trust += 1
            "三辆车都在避让一段下沉路面。前两辆勉强通过，最后一辆的左轮却在每次受力时向外偏转。"
            "木制轮毂靠近轴帽的位置已经开裂。裂口不大，但下一次横向冲击会让它整片崩开。"
            "车轮还在转。裂纹却已经替它决定了还能走多远。"

    "商队的轮声越来越近。最后一辆篷车压上旧路基与泥地交界处的破损接缝。"
    jump town_t02_broken_axle


label town_t02_broken_axle:
    scene town cg axle
    with hpunch
    play sound "audio/sfx/wood_axle_crack.ogg" volume 0.78
    "木头裂开的声音比我预想得更脆。"
    "左轮突然外翻，车身向路肩倾斜。最上层货箱挣断绳结，直直滑向那个赤狐。"
    "我跨过护栏，双手抵住箱角，再用肩部顶住仍在下沉的车架。"
    "篇章-VI在后颈深处短促发热，我没有让它启动。救人以后若再让自己变成无法解释的威胁，这场相遇不会有好结果。"
    lan "先别松手！右边再垫一块——对，就是你脚边那块！"
    "他的口音比远处听起来更重。我慢了半拍才理解“垫”的意思。"
    ao "先固定另一侧。我一松手，它还会倒。"
    heng "听得懂。照他说的做。"
    "宽角牦牛把另外两人喝退到安全位置，又亲自检查了绳索与轮楔。"
    taosui "稳住。衡叔，先卸外侧两箱。岚，重记封签。"
    "命令很短。所有人都知道自己该做什么。"
    "等重量被移开，我才缓慢放下箱体。六双眼睛随即从货物转到我身上。"
    taosui "名字。"
    ao "[player_name]。"
    taosui "从哪来？"
    "这是第一个不能用真话回答的问题。"

    menu:
        "先把双手放在所有人看得见的地方":
            $ caravan_trust += 1
            $ caution += 1
            "我退开半步，把爪尖收起，双手停在视线能覆盖的位置。"
            ao "我没有武器，也不会碰剩下的货。刚才那只箱子会砸到人。"
            taosui "你知道我们为什么防着你，这就省事。"

        "指出轮毂还会继续裂开" if tech_insight >= 2:
            $ caravan_trust += 1
            ao "轴帽旁边的裂口已经吃进第二层木纹。只把轮子扶正，走不过下一个弯。"
            heng "你看得见？"
            ao "受力以后，木屑颜色会变浅。现在已经变了。"
            "衡叔蹲下看了几秒，再抬头时，敌意少了一半。"
            heng "他说得对。得把重量借给车架。"

        "只报姓名，不主动补充经历":
            $ lan_affinity += 1
            ao "我可以回答姓名。来处暂时不能。"
            lan "这回答不讨喜，但比随口编个村子强。"
            taosui "岚。"
            "岚闭上嘴，把散落的木签重新抱进怀里。"

    "陶穗没有继续审问。她先让衡叔确认损坏程度，再示意我到路边说话。"
    jump town_t03_cover_and_clothes


label town_t03_cover_and_clothes:
    scene town cg roadside_map with dissolve
    taosui "后车需要加固。衡叔的脚昨天扭了，今天少一个能稳车和搬货的人。"
    taosui "城门日落后关闭。我们没有时间回驿站找脚夫。"
    taosui "你从哪里来，我现在不问。你替我们把车送进灰桥，我给你饭、衣服和今天的工钱，再把名字写进雇签。"
    taosui "进门以后，各走各的路。只要别把旧麻烦带到商队头上。"
    ao "可以。"
    lan "先别答这么快。她说的工钱是二十七枚小铜，不包明天。"
    taosui "现在二十五了。"
    "岚抿住嘴，抱着木签退开一步。"
    "陶穗看着我，显然在等我理解的不只是价钱。"
    ao "我把车送进城。你给我雇签、衣食和二十五枚小铜。"
    taosui "进门前一半，进门后一半。车到，钱到。"
    ao "成交。"
    $ caravan_trust += 1

    window hide
    play music "audio/music/greybridge_road_sample.mp3" fadein 2.5 volume 0.42
    play sound "audio/sfx/map_unfold.ogg" volume 0.62
    scene town_map base with fade
    show town_paw pointer at town_paw_enter_city
    play sound "audio/sfx/paw_map_tap.ogg" volume 0.48
    pause 0.7
    window show
    lan "先让你知道我们要去哪里。这里是灰桥城，荟屿国的首都。"

    show town_map route with Dissolve(0.8)
    show town_paw pointer at town_paw_to_road
    play sound "audio/sfx/paw_map_tap.ogg" volume 0.45
    pause 0.9
    lan "我们现在在第 21 号王国公路上。沿这条旧路再走半日，就是西关道。"

    show town_paw pointer at town_paw_back_to_city
    play sound "audio/sfx/paw_map_tap.ogg" volume 0.45
    pause 1.1
    lan "我们此行正是前往灰桥城进行贸易。眼下正值国王庆典，进城的货队比平日多一倍。"
    lan "庆典期间，验籍门会把临时雇工一个个核对。日落后，他们连争辩的机会都不给。"
    window hide
    hide town_paw pointer with dissolve
    scene town cg roadside_map with fade
    window show

    lan "你的口音像北边，但你没有行脚牌。最省事的说法是北岭旧道塌方，和同行者、行李、文书一起失散。"
    ao "他们查不出来？"
    lan "塌方以后，北岭那边几个月都未必送得来一封信。更重要的是，这个说法不会把商队拖进你的过去。"
    lan "进门时别慌，也别前后说成两件事。"

    menu:
        "尽量少说，只保证能工作":
            $ town_cover_story = "minimal"
            ao "来处由保人说。我只回答姓名和今天做过的事。"
            taosui "好。问到你再答，没问就别补。"

        "把塌方、失散和行程整理成完整顺序":
            $ town_cover_story = "ordered"
            ao "北岭旧道，三日前塌方；与同行者失散，文书和行李都在另一侧；沿旧路向南寻找工作。"
            lan "别说“三日”这么准。真正逃出来的人通常记不清。"
            ao "那就改成“前几日”。"
            $ caravan_trust += 1

        "先让岚解释每个证件词的含义":
            $ town_cover_story = "learned"
            $ lan_affinity += 1
            ao "先告诉我这些证件各自管什么。我不想到了城门前才发现自己答错。"
            lan "行脚牌证明商队能跨城做买卖；保人证明出了事有人能被找到；短籍让外来人暂时住下和工作。"
            lan "你现在三个都没有。所以陶姐把你写进雇签，她当保人，进城以后再办短籍。"
            "每一项凭证都指向来处、亲族和曾经做过的事。偏偏这些，我一样也拿不出来。"
            lan "你今天替商队做过事。先从今天写起。"

    "岚从备用箱里找出米白内衫、蓝灰工作长衣和一卷前臂绑带。"
    "我躲到篷车与帆布之间，把旧实验服折好，压进应急袋最底层。它不能被看见，也不能丢。"
    lan "你的尾巴……这件衣服没有给它留地方。"
    "我低头看了看被顶起的后腰。一路上只顾着不被自己绊倒，确实没有想过衣服也需要适应这具身体。"
    ao "能改吗？"
    lan "能。别乱动。"
    "他拿走工作衣，把后背朝上摊平，在后腰中央剪开一道缝，又沿边缘补了几针。"
    "剪刀靠近尾根时，我本能地向前挪了半步。"
    lan "我还没碰到你。"
    ao "身体自己躲的。"
    "岚看了我一眼，没有追问，只把剪刀换到另一只手。"
    scene town cg clothes with dissolve
    "尾巴从背后的开口穿出，衣摆终于落回正确位置。岚又替我收紧前臂绑带，灰蓝布条盖住米白袖口，也遮住了手臂上最显眼的接口痕迹。"
    $ town_outfit = True
    lan "转一圈。"
    "我照做。尾巴扫过帆布，却没有再掀起衣摆。"
    lan "行。进城以前别把线扯开。"
    "他说完才收起针线，像是直到这时才肯承认，这个突然从林子里出现的人真的会跟他们走。"
    jump town_t04_road_work


label town_t04_road_work:
    scene town cg road with Fade(0.6, 0.2, 0.8)
    "车轮重新上路时，太阳已经压到旧高架的断面后方。"
    "陶穗把临时木签挂上我的腰带。薄薄一片木头，不能证明我是谁，却足以让城门相信今天有人见过我。"
    taosui "选一件事做。别逞强，别碰没有报给你的货。"

    menu:
        "协助衡叔加固车轴":
            $ town_work_choice = "axle"
            $ caravan_trust += 1
            "衡叔让我托住纵梁，他把两根木撑削成楔形，再用浸水绳索绕过车架。"
            if tech_insight >= 2:
                ao "别让裂口继续吃力。把重量借给中间那根梁，轮毂只负责保持方向。"
                heng "“借给梁”……这话能听懂。就这么垫。"
                $ caravan_trust += 1
            else:
                heng "你只管稳住。手指别伸进绳圈，车一沉就能把爪子全带走。"
                ao "明白。我听你的口令。"
            heng "明天要是还在南市，来修理铺找我。你不一定会木工，但看东西挺准。"

        "和岚一起复核货签":
            $ town_work_choice = "tags"
            $ lan_affinity += 1
            $ old_world_exposure += 1
            lan "我念货名，你按颜色、重量和封蜡排。别看字，旧字有时候会骗人。"
            "我先按他的规则排完一轮，又在一枚磨损木签背面认出近似旧汉字的“药”。"
            ao "这箱应该避水。背面原本标的是药材。"
            lan "你刚才不是说只听得懂七成？"
            ao "话音变得快，字留下得久。"
            lan "北岭旧道还教这个？"
            "我没有立刻回答。岚把那枚木签翻回正面，也没有继续逼问。"
            lan "这件事先记着。"

        "走在后车外侧观察路况":
            $ town_work_choice = "road"
            $ caution += 1
            $ caravan_trust += 1
            "我走在受损车轮外侧，提前观察泥地颜色和车辙边缘。"
            "一处路肩看似干燥，草根下却有积水。后轮一旦陷入，临时木撑会从相反方向折断。"
            ao "前方靠左。右侧地面承不住后车。"
            taosui "全队靠左，轮距别乱。"
            if tested_accelerator:
                "车轮接近软土时，后颈深处的篇章-VI自行进入预备。"
                "我压下启动冲动。陶穗已经听见提醒，车队也开始转向，没有必要让他们再看见一件无法解释的事。"

    if gathered_supplies:
        "休息时，衡叔重新缠脚踝。旧布已经被汗水浸透。"
        "我从应急袋里取出一小段复合绷带，剪下足够固定关节的长度。"
        heng "这是什么布？"
        ao "很久以前的医疗用品。药已经不能信了，布还能用。"
        heng "能当布用就行。我欠你一段新的。"
        $ caravan_trust += 1

    if inspected_prototypes:
        "陶穗在重新出发前按名字点了一遍人数。每个人都应了一声。"
        "那三个只剩编号的人忽然从记忆里浮上来。我慢了一拍，才在“[player_name]”后回答。"
        lan "累了？"
        ao "……没有。只是很久没人这样叫我的名字。"

    "旧高架从山谷一侧跨向另一侧，桥墩外包着后世加建的石块与木台。"
    if tech_insight >= 2:
        "我认得那种承重结构。两千年前，车辆会以远超这支商队的速度从上面通过。"
        "但我没有说出“高速公路”。现在的语言里，那只是一条由先民留下的王国大道。"
    "天色继续下沉。队伍前方终于传来城门链条与人群混在一起的回声。"
    jump town_t05_gate


label town_t05_gate:
    scene town cg city with dissolve
    "西关道塞满等待验货的车。旧混凝土桥墩撑起外层门洞，木石吊门和盖章台则紧贴在它后来裂开的缝隙里。"
    "这里不是纯粹的古城，也不是仍在运行的旧设施。两套时代把彼此当作地基，勉强站在一起。"
    wence "河谷商队。行脚牌、货单、人数。临时雇工单独站到黄线后。"
    "黑背犬副官逐项核对木签与封蜡，没有故意拖延，也没有漏掉任何一项。"
    "轮到我时，他先看临时雇签，再看我的手。"
    wence "名字。"
    ao "[player_name]。"
    wence "籍贯。"
    "我知道这两个字的意思。可在这个时代，籍贯是一条能回溯的路，而我的路在地下断了两千年。"

    if town_cover_story == "minimal":
        "我看向陶穗，没有抢在保人前补充。"
        taosui "北边旧道来的散籍。前几日遇塌方，文书与同行者失散。今天在二十一号路替我们稳车，有劳务事实。"
        wence "知道什么时候闭嘴不算坏事。但进城以后，保人不能替你回答每一个问题。"
        ao "明白。"
    elif town_cover_story == "ordered":
        ao "北岭旧道。前几日遇到塌方，与同行者失散，文书和行李留在断路另一侧。我沿旧路向南寻找工作。"
        wence "先遇塌方，还是先与同行者分开？"
        ao "塌方以后。绕行时失散。"
        "顺序与雇签一致。闻策没有表示相信，只在下一栏画了一道短线。"
    else:
        ao "北岭旧道来的旧道散籍。今天由河谷商队担保，以临时脚夫身份入城。"
        "身后传来货签盒被轻敲两下的声音。岚在提醒我：术语没有说错。"
        wence "词倒是学得快。是谁教你的？"
        ao "负责写雇签的人。"
        lan "是我。签上有我的印。"

    wence "手伸出来。"
    "他翻看我的掌心。那里有新留下的绳索压痕，却没有长期搬运形成的厚茧。"
    wence "不像常年脚夫。"
    ao "过去做的不是搬运工作。"
    wence "做什么？"
    ao "说了也没有人能替我作证。"
    "闻策看了我几秒。"
    if old_world_exposure >= 1:
        "他在雇签背面做了一个很小的记号。那不是拒绝，更像把一处不一致留给以后。"
        wence "认得旧字，却没有文书。进去后别拿这点本事替人乱解碑文。"
    heng "断轴是他帮着稳的。车上的新撑也是他一起装的。今天的活，我作证。"
    taosui "南栈院还有床位。我担保三十日。"
    wence "短籍只能在南市活动。三十日内没有续签，也没有离城记录，保人和你一起担责。"
    ao "明白。"
    wence "进去以后再让人给你念一遍。听懂和记住不是一回事。"
    play sound "audio/ui_ping.wav"
    "印章落在雇签上。吊门没有为我单独开启；它只是恰好在下一支车队到来时继续升高。"
    $ caravan_trust += 1

    scene town cg city with Fade(0.8, 0.3, 1.1)
    play crowd "<from 2.0 to 8.5>audio/ambience/greybridge_gate_crowd_cc0.ogg" volume 0.16
    "穿过冷暗门洞的一瞬间，晚霞、灯火和几百种声音同时涌进视野。"
    "岚走出几步，又回头确认我是否跟上。陶穗已经领着货车进入外市的人流。"
    "我握紧刚盖过章的木牌。掌心能完全遮住它，可就是这样一件轻得几乎没有分量的东西，第一次让这个时代承认我暂时存在。"
    stop ambience fadeout 1.5
    stop music fadeout 2.0
    stop crowd fadeout 0.8
    jump town_t06_south_yard


label town_t06_south_yard:
    scene town cg south_market with dissolve
    "在远处观察一座城市，与被它包围是两回事。"
    "门洞比旧时代建筑更高；路边长椅没有统一靠背；摊位之间留着足够尾巴转身的距离。"
    "不同角型对应不同高度的门梁，饮水台旁甚至有专门让长吻种族使用的斜槽。"
    "这里的一切都不是为了迁就某个异类临时加上的。新的居民已经在这座城市里生活了太久，久到石头和木头都记住了他们身体的形状。"
    lan "三件事。别踩别人的尾巴，别在南市公开拔爪，买东西以前先问清楚他说的是枚、串还是袋。"
    ao "单位不统一？"
    lan "很不统一。买东西前先问清楚，不然你今天的工钱未必换得来一顿饭。"
    ao "我会先问。"
    lan "那就好。"

    scene town cg south_yard with Fade(0.7, 0.2, 0.8)
    "南栈院藏在外市两排货仓之间。院里堆着待卸的木箱、晾到一半的缰绳和按尾巴长度分开的通铺牌。"
    "獾兽人管事坐在登记桌后，先看陶穗的担保印，再看我。"
    mei "姓名。"
    ao "[player_name]。"
    mei "尾巴多长？"
    ao "这与短籍有关？"
    mei "与床位有关。长尾睡里侧，一翻身能把别人连被子一起扫下床。"
    lan "给他外侧吧。"
    mei "不用你替他长尾巴。"
    "她把姓名、雇签号和南栈院地址抄进册子，用一根沾得过饱的笔划掉了错误的一横。"
    mei "三十日短籍。活动范围南市。床七，靠墙外侧。热水在后院，过钟不添。"
    mei "热水和床具押金两枚小铜。坏东西照价赔，打架两个一起扔出去。"
    taosui "工钱二十五。门外给过一半，这是余下的。"
    "陶穗把铜币一枚不差地放在桌上。梅婶当面取走两枚押金，剩下的推给我。"
    $ town_permit = True
    $ town_money = 23
    $ town_bed = "south_yard_bunk_07"
    $ surface_plan = "town"
    show screen town_short_permit_overlay(player_name, town_permit_id) with dissolve
    play sound "audio/ui_ping.wav"
    pause 1.2
    mei "规矩看清了就收起来。木牌丢了，补办费比你今天工钱贵。"
    "我立刻把木牌收进贴身的内袋。梅婶看见了，满意地用笔杆点向后院。"
    mei "床七，靠墙外侧。热水快去，过钟真没有。"
    hide screen town_short_permit_overlay with dissolve
    "陶穗只说了明早卸货的时辰，便转身去核对入库数量。帮助到这里结束得和她承诺的一样明确。"
    taosui "明早愿意继续干活，就按南栈院的日价算。不愿意，短籍也仍然有效。"
    ao "我记住了。"
    taosui "你把车送进来，我们把你送进来。今天的账，到这里就平了。"
    "我喜欢这句话。没有恩情，也不必急着把一场交易说成信任；可当一个人身无所有时，公平本身已经足够难得。"
    jump town_t07_lamplight


label town_t07_lamplight:
    scene town cg bunk_room with Fade(0.8, 0.3, 1.0)
    "通铺房只亮着一盏低灯。其他人还在院里卸货，隔墙不断传来木轮、脚步和碗碟碰撞的声音。"
    "我把应急袋压到靠墙一侧。旧实验服和离线核心都藏在最底下，短籍牌则放在伸手就能摸到的位置。"
    "门被轻敲两下。岚抱着一卷布条和一张抄过的城内简图走进来。"
    lan "改衣服剩下的。尾孔要是夜里开线，先用这个绑，别穿着一半跑到院里找我。"
    ao "谢谢。"
    lan "先别谢。明天真开了线，我还是会笑你。"
    "他把简图放下，却没有立刻离开。"
    lan "你知道车架怎么受力，能看懂旧桥上的字，却不知道一枚大铜换多少小铜。"
    ao "听起来不像一个正常长大的人。"
    lan "你说话不像北边人。你看城门、椅子和每条尾巴让出来的空位，像第一次见这些东西。"
    ao "这不能证明我说的是假话。"
    lan "不能。所以我没准备现在揭穿你。"
    ao "这句话没有让我更放心。"
    lan "那就当交换。你不问我为什么没有本籍，我也不问你到底从哪座山里掉出来。"

    menu:
        "接受这个边界":
            $ lan_affinity += 1
            ao "可以。过去的事都不问，今天说过的话要算数。"
            lan "明早我去短籍所补登记。你跟我一起，路上先把大铜小铜认全。"
            ao "这也算交换？"
            lan "算我不想看你第一天就把工钱花光。"

        "告诉他一小部分真话":
            $ lan_affinity += 2
            ao "我醒来以后，能回去的地方已经不存在了。"
            "这是真话。只是省略了地下七百二十米和两千年。"
            lan "所以你不是在找同行者。"
            ao "我在找一条不需要过去也能开始的路。"
            lan "我那时也想找个地方重新开始。后来才知道，灰桥先问你住在哪里、谁肯担保，别的都得往后排。"
            ao "这些问题，我现在至少能答上一半。"

        "反问他为什么愿意担风险":
            ao "你先解释一件事。替一个来历不明的人写雇签，对你有什么好处？"
            lan "没有好处。写错了还要挨陶姐骂。"
            lan "我第一次到灰桥时也没有保人。在西关道外等了两天，所有人都说规矩就是规矩。"
            lan "后来陶姐缺一个识字的跑腿，才把我写进商队。"
            lan "我不觉得每个被挡在门外的人都值得放进来。但我知道，没人替你写第一行字时，你连证明自己值不值得的机会都没有。"
            "我看着桌上的短籍牌。今天以前，我也不相信一行字能替人打开一扇门。"
            ao "我明白了。谢谢你替我写第一行。"
            "岚愣了一下，把视线转向已经拨低的灯芯。"
            lan "以后值不值得，你自己证明。"

    "岚把灯芯拨低，走到门口时又停了一下。"
    lan "三十日不长。先把明天过完。"
    ao "我也是这么想的。"
    lan "那明早见。"
    "门关上以后，房间里仍有车轮、脚步和隔墙说话的声音。"
    "地下设施的安静意味着没有人活着。这里的吵闹却让人知道，墙外总有谁会在下一刻咳嗽、抱怨，或者喊出另一个人的名字。"
    "我把短籍牌放到枕边。三十日很短，却已经比醒来时那个只通向出口的明天更长。"
    jump town_route_complete


label town_route_complete:
    $ persistent.town_route_opened = True
    $ persistent.town_met_lan = True
    $ persistent.last_origin_route = "town"
    $ persistent.town_caravan_trust = caravan_trust
    $ persistent.town_lan_affinity = lan_affinity
    $ persistent.town_cover_story = town_cover_story
    $ persistent.town_work_choice = town_work_choice
    $ persistent.town_permit_id = town_permit_id
    $ persistent.town_permit = town_permit
    $ persistent.town_money = town_money
    $ persistent.town_bed = town_bed
    $ persistent.town_outfit = town_outfit

    show screen town_route_complete_overlay(player_name, caravan_trust, lan_affinity) with dissolve
    play sound "audio/ui_ping.wav"
    pause 1.4
    hide screen town_route_complete_overlay with dissolve
    centered "第一章　城镇路线第一部分完"
    return
