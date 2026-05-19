from __future__ import annotations

import sys
import timeit


def main() -> None:
    n = 200000
    number = 200
    repeat = 7

    list_data = list(range(n))
    tuple_data = tuple(list_data)

    def loop_list() -> int:
        s = 0
        for x in list_data:
            s += x
        return s

    def loop_tuple() -> int:
        s = 0
        for x in tuple_data:
            s += x
        return s

    assert loop_list() == loop_tuple()

    t_list = min(timeit.repeat(loop_list, number=number, repeat=repeat))
    t_tuple = min(timeit.repeat(loop_tuple, number=number, repeat=repeat))

    print(f"n={n} number={number} repeat={repeat} (best of repeat)")
    print(f"list : {t_list:.6f} s")
    print(f"tuple: {t_tuple:.6f} s")
    print(f"tuple/list: {t_tuple / t_list:.4f}x")


if __name__ == "__main__":
    main()
