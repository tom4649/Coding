from functools import wraps


def tail_recursive(func):
    firstcall = True
    params = ((), {})
    result = func

    @wraps(func)
    def wrapper(*args, **kwd):
        nonlocal firstcall, params, result
        params = args, kwd
        if firstcall:
            firstcall = False
            try:
                result = func
                while result is func:
                    result = func(*args, **kwd)  # call fact
                    args, kwd = params
            finally:
                firstcall = True
                return result
        else:
            return func

    return wrapper


class Solution:
    @tail_recursive
    def myPowHelper(self, base: float, exp: int, acc: float) -> float:
        if exp == 0:
            return acc
        if exp % 2 == 1:
            return self.myPowHelper(base, exp - 1, acc * base)
        return self.myPowHelper(base * base, exp // 2, acc)

    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.myPowHelper(x, n, 1.0)
        return 1 / self.myPowHelper(x, -n, 1.0)


if __name__ == "__main__":
    import sys

    _saved_limit = sys.getrecursionlimit()

    try:
        sys.setrecursionlimit(10)
        x, n = 1.0001, 2**31 - 1
        sol = Solution()
        sol.myPow(x, n)
    finally:
        sys.setrecursionlimit(_saved_limit)
