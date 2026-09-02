# 第三方声音素材记录

本文件记录游戏实际接入的第三方声音。即使素材采用 CC0、无需署名，项目仍主动保留作者、来源和处理信息，方便后续替换、发布与审计。

## 当前试听小样（旧王国公路—验籍门）

| 游戏内文件 | 原作 / 作者 | 来源 | 许可证 | 下载日期 | 本项目处理 |
|---|---|---|---|---|---|
| `game/audio/music/greybridge_road_sample.mp3` | *Town Theme RPG* / cynicmusic | [OpenGameArt](https://opengameart.org/node/20593) | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | 2026-09-03 | 保留原编码；重命名；在 Ren’Py 中以 42% 音量、2.5 秒淡入播放。当前是路线试听曲，未锁定为最终曲目。 |
| `game/audio/ambience/old_kingdom_road_wind.ogg` | `wind.ogg`（*Icy Heights* 附件）/ Écrivain | [OpenGameArt](https://opengameart.org/content/icy-heights) | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | 2026-09-03 | 保留原编码；重命名；作为独立环境轨循环，以 16% 音量淡入。 |
| `game/audio/sfx/wood_axle_crack.ogg` | `chop.ogg` / Kenney, *RPG Audio* | [Kenney](https://kenney.nl/assets/rpg-audio) | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | 2026-09-03 | 从素材包中选取并重命名；用作断轴瞬间的木裂声。 |
| `game/audio/sfx/map_unfold.ogg` | `bookOpen.ogg` / Kenney, *RPG Audio* | [Kenney](https://kenney.nl/assets/rpg-audio) | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | 2026-09-03 | 从素材包中选取并重命名；用作羊皮地图展开声。 |
| `game/audio/sfx/paw_map_tap.ogg` | `bookPlace2.ogg` / Kenney, *RPG Audio* | [Kenney](https://kenney.nl/assets/rpg-audio) | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | 2026-09-03 | 从素材包中选取并重命名；以不同运行时音量用于三次兽爪落点。 |
| `game/audio/ambience/greybridge_gate_crowd_cc0.ogg` | *Crowd Shouting/Speaking Ambience* / StarNinjas | [OpenGameArt](https://opengameart.org/content/crowd-shoutingspeaking-ambience) | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | 2026-09-03 | 保留原 OGG；仅播放 2.0–8.5 秒片段，以 16% 音量作为首次穿过验籍门时短暂涌入的人声层，随后淡出且不循环。 |

## 备注

- 仓库只收录游戏实际调用的文件，不收录下载得到的完整素材包。
- 当前行路音乐是供用户试听空间关系、转场与对白可读性的候选曲，不代表最终选曲。
- 所有素材均允许商业与非商业项目使用；本轮未接入 NC（禁止商业使用）素材。
