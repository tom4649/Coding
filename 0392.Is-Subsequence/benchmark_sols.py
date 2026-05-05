import importlib.util
import random
import string
import time
from pathlib import Path

DIR = Path(__file__).resolve().parent


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def is_sub(sol, s: str, t: str) -> bool:
    return sol.isSubsequence(s, t)


def _ref_subsequence(s: str, t: str) -> bool:
    if not s:
        return True
    i = 0
    for c in t:
        if c == s[i]:
            i += 1
            if i == len(s):
                return True
    return False


def _random_string(n: int) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=n))


def main() -> None:
    mod1 = load_module("sol1_impl", DIR / "sol1.py")
    mod3 = load_module("sol3_impl", DIR / "sol3.py")
    sol1 = mod1.Solution()
    sol3 = mod3.Solution()

    random.seed(0)
    cases: list[tuple[str, str]] = [
        ("", "abc"),
        ("abc", ""),
        ("abc", "ahbgdc"),
        ("axc", "ahbgdc"),
        ("", ""),
        ("a" * 100, "a" * 200 + "b" * 200),
    ]
    for _ in range(200):
        la, lb = random.randint(0, 500), random.randint(0, 2000)
        cases.append((_random_string(la), _random_string(lb)))

    for s, t in cases:
        is_sub(sol1, s, t)
        is_sub(sol3, s, t)

    reps = 50
    t0 = time.perf_counter()
    for _ in range(reps):
        for s, t in cases:
            is_sub(sol1, s, t)
    t_sol1 = time.perf_counter() - t0

    t0 = time.perf_counter()
    for _ in range(reps):
        for s, t in cases:
            is_sub(sol3, s, t)
    t_sol3 = time.perf_counter() - t0

    print(f"sol1: {t_sol1 * 1000:.3f} ms")
    print(f"sol3: {t_sol3 * 1000:.3f} ms")
    ratio = t_sol3 / t_sol1
    print(f"(sol3 / sol1: {ratio:.3f})")


if __name__ == "__main__":
    main()
