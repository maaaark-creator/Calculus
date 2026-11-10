# 历年期中详解源码

两份参考答案均按仓库内原卷独立解答。2023—2024 学年 17 题、110 分；2024—2025 学年 18 题、110 分。2024 年平均分 58.32、中位分 57.5 由用户提供，直接记录原分数。

源文件：`23-24-answers.tex`、`24-25-answers.tex`；共享排版：`common.tex`。`draw_function.py` 使用 ReportLab 生成第 14 题的矢量草图 `function-24-q14.pdf`。

在 Windows 上使用 XeLaTeX（需要 `ctex` 及 Windows 中文字体）和带有 `reportlab` 的 Python，可从本目录运行：

```powershell
./build.ps1 -Python "你的Python可执行文件绝对路径"
```

脚本每份编译两遍，生成文件放在仓库 `output/pdf/历年期中详解/`（已忽略），并复制两份成品 PDF 到 `review/`。源码和草图可用于后续修订。

当前课程范围的跳题清单及选做说明见 [复习资料目录](../README.md)。完整解答保留了原卷中的范围外题目。
