# GitHub 写作 Skill：本作采用情况

2026-09-05。本文件记录筛选后的采用判断，不把社交平台的榜单排名当作效果证据。不安装整套外部 Skill，不执行其脚本，不增加哈希流程。规则为针对本项目独立编写的表述。

| 来源 | 采用的思路 | 未采用的部分 |
| --- | --- | --- |
| [Anbeeld/WRITING.md](https://github.com/Anbeeld/WRITING.md) | 体裁区分、整段重复模式、朴素复述诊断 | 把所有正式文本改成随意口语 |
| [LifelongLazyLearner/qu-ai-wei](https://github.com/LifelongLazyLearner/qu-ai-wei) | 中文改写保护语义、立场、条件，修改前后互查 | 全套门检、固定报告模板 |
| [MrGeDiao/shuorenhua](https://github.com/MrGeDiao/shuorenhua) | 问题严重度与授权修改范围分开 | 将发布文案规范直接套进角色对白 |
| [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode) | 作者偏好与设定分离，人物知识与章节状态连续 | 整套长篇事务、状态文件和代理流水线 |
| [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | 从处境、冲突需求和决策刻画角色 | 名人语气蒸馏、固定口头特征 |
| [jzOcb/writing-style-skill](https://github.com/jzOcb/writing-style-skill) | 仅将反馈前后对照作为独立设计启发 | 审阅时未找到许可证，不复制正文、脚本或模板 |

前五项审阅时标明 MIT；原先借鉴的 haowjy Creative Writing Craft / Prose Writing 归属仍保留在 Skill 中。以上链接用于追溯，不代表同意或加载上游全部规则。

humanizer、Humanizer-zh、stop-slop 一类的模式清单只适合辅助发现症状；不把其禁词、固定口语替换或“为虚构添细节”的宽泛许可纳入既有剧情改写。检测器不是文学评审，也不应成为本作的验收目标。

## 落地结构

- `SKILL.md`：保留通用主流程，只增加条件入口及语义双向检查。
- `references/chinese-revision.md`：中文改句，既有“改”也有“留”的示例。
- `references/route-continuity.md`：四层知识、可选经历、物理和经济连续性。
- `references/author-calibration.md`：真实作者认可、候选稿、设定与偏好的边界。

本轮收益的证据是实际发现并修补前文的连续性问题，详见 `SCRIPT_REVIEW_20260905.md`。没有做独立模型 A/B 实验，不声称提升百分比。
