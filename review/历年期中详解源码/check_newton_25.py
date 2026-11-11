"""Generate a high-precision observation table for 2025 Q17 (standard library only).

The PDF contains an analytic error proof. This table is supporting numerical
evidence and does not replace that proof. Run from any working directory.
"""
from decimal import Decimal, localcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def step(x):
    return (2 * x**3 + 1) / (3 * x**2 + 1)


with localcontext() as ctx:
    ctx.prec = 2400
    alpha = Decimal("0.7")
    for _ in range(30):
        alpha = step(alpha)
    assert abs(alpha**3 + alpha - 1) < Decimal("1e-2390")

    rows = []
    x = Decimal(1)
    prev_error = None
    for n in range(12):
        error = x - alpha
        assert error > 0
        if prev_error is not None:
            assert error < prev_error**2
        if n in (10, 11):
            assert error < Decimal("1e-100")
        if n in (0, 1, 2, 3, 4, 5, 8, 10, 11):
            mantissa, exponent = f"{error:.3E}".split("E")
            error_tex = f"{mantissa}\\times10^{{{int(exponent)}}}"
            # Fixed decimals in a table must not be read as high-precision output.
            x_text = f"{x:.12f}"
            rows.append(f"{n} & ${x_text}$ & ${error_tex}$ \\\\")
        print(f"n={n:2d}  x_n={x:.18f}  error={error:.6E}")
        prev_error = error
        x = step(x)

table = "\n".join([
    r"\begin{tabular}{ccc}",
    r"\toprule $n$ & $x_n$（保留 12 位小数） & $|x_n-\alpha|$（约值）\\\midrule",
    *rows,
    r"\bottomrule",
    r"\end{tabular}",
    "",
])
(ROOT / "newton-25-table.tex").write_text(table, encoding="utf-8")
print("Saved", ROOT / "newton-25-table.tex")
