import itertools


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        reversed_result = []
        carry = False
        for c_a, c_b in itertools.zip_longest(a[::-1], b[::-1], fillvalue="0"):
            if c_a == "0" and c_b == "0" and carry:
                reversed_result.append("1")
                carry = False
            elif c_a == "0" and c_b == "0" and not carry:
                reversed_result.append("0")
                carry = False
            elif c_a == "1" and c_b == "1" and carry:
                reversed_result.append("1")
                carry = True
            elif c_a == "1" and c_b == "1" and not carry:
                reversed_result.append("0")
                carry = True
            elif carry:
                reversed_result.append("0")
                carry = True
            else:
                reversed_result.append("1")
                carry = False
        if carry:
            reversed_result.append("1")
        return "".join(reversed(reversed_result))


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        reversed_result = []
        while i >= 0 or j >= 0 or carry == 1:
            total = carry
            if i >= 0:
                total += int(a[i])
            if j >= 0:
                total += int(b[j])
            reversed_result.append(str(total % 2))
            carry = total // 2
            i -= 1
            j -= 1
        return "".join(reversed(reversed_result))


from collections import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        padded_a = a.zfill(n)
        padded_b = b.zfill(n)
        result = deque()
        carry = 0
        for i in range(n - 1, -1, -1):
            total = int(padded_a[i]) + int(padded_b[i]) + carry
            result.appendleft(str(total % 2))
            carry = total // 2
        if carry == 1:
            result.appendleft("1")
        return "".join(result)
