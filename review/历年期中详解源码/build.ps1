param(
    [string]$Python = "python",
    [string]$XeLaTeX = "xelatex"
)
$ErrorActionPreference = "Stop"
$repoRoot = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$outDir = Join-Path $repoRoot "output/pdf/历年期中详解"
New-Item -ItemType Directory -Path $outDir -Force | Out-Null
Push-Location $PSScriptRoot
try {
    & $Python -X utf8 draw_function.py
    if ($LASTEXITCODE -ne 0) { throw "Figure generation failed." }
    foreach ($year in @("23-24", "24-25")) {
        foreach ($pass in @(1, 2)) {
            $buildOutput = & $XeLaTeX -interaction=nonstopmode -halt-on-error "-output-directory=$outDir" "$year-answers.tex" 2>&1
            if ($LASTEXITCODE -ne 0) {
                $buildOutput | Write-Output
                throw "XeLaTeX failed: $year, pass $pass."
            }
        }
        $name = "$year-高数1期中_参考答案与详解.pdf"
        Copy-Item -LiteralPath (Join-Path $outDir "$year-answers.pdf") -Destination (Join-Path $outDir $name) -Force
        Copy-Item -LiteralPath (Join-Path $outDir $name) -Destination (Join-Path $repoRoot "review/$name") -Force
        Write-Output "Built review/$name"
    }
} finally {
    Pop-Location
}
