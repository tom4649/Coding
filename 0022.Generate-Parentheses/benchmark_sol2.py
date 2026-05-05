import timeit
from pathlib import Path
from typing import List

DIR = Path(__file__).resolve().parent


def load_solution_class(path: Path) -> type:
    src = path.read_text()
    if "from typing" not in src.split("\n", 5)[:5]:
        src = "from typing import List\n" + src
    ns: dict = {"__name__": f"bench_{path.stem}", "List": List}
    exec(compile(src, str(path), "exec"), ns)
    return ns["Solution"]


def main() -> None:
    Sol2 = load_solution_class(DIR / "sol2.py")
    Sol2Revised = load_solution_class(DIR / "sol2_revised.py")

    cases = [8, 10, 12, 13]
    print("-" * 60)

    for n in cases:
        number = 5 if n <= 10 else 2 if n == 12 else 1
        stmt1 = f"Solution().generateParenthesis({n})"
        t1 = timeit.timeit(
            stmt1,
            number=number,
            globals={"Solution": Sol2},
        )
        t2 = timeit.timeit(
            stmt1,
            number=number,
            globals={"Solution": Sol2Revised},
        )
        ratio = t2 / t1 if t1 > 0 else float("inf")

        print(
            f"n={n:2d}  number={number:2d}  "
            f"sol2: {t1 * 1000:8.2f} ms  sol2_revised: {t2 * 1000:8.2f} ms  "
            f"(revised / sol2 = {ratio:.3f})"
        )


if __name__ == "__main__":
    main()
