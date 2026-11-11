# 历年期中详解源码

三份参考答案均按仓库内原卷独立解答。2023—2024 学年 17 题、110 分；2024—2025 学年 18 题、110 分；2025—2026 学年 17 题、100 分。2024 年平均分 58.32、中位分 57.5 沿用已有记录。

源文件：`23-24-answers.tex`、`24-25-answers.tex`、`25-26-answers.tex`；共享排版：`common.tex`。`draw_function.py` 使用 ReportLab 生成 2024 年第 14 题的矢量草图 `function-24-q14.pdf`。`check_newton_25.py` 使用 Python 标准库 Decimal 的 2400 位精度核对 2025 年第 17 题，生成数值观察表 `newton-25-table.tex`；严格误差证明见正文。

在 Windows 上使用 XeLaTeX（需要 `ctex` 及 Windows 中文字体）和带有 `reportlab` 的 Python，可从本目录运行：

```powershell
./build.ps1 -Python "你的Python可执行文件绝对路径"
```

脚本每份编译两遍，生成文件放在仓库 `output/pdf/历年期中详解/`（已忽略），并复制成品 PDF 到 `review/`。仅编译 2025 年卷时，可运行 `./build.ps1 -Years 25-26 -Python "你的Python可执行文件绝对路径"`，无需 ReportLab。源码、草图和生成的数值表可用于后续修订。

当前课程范围的跳题清单及选做说明见 [复习资料目录](../README.md)。完整解答保留了原卷中的范围外题目。
