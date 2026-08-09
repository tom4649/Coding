class Solution:
    def calculate(self, s: str) -> int:
        def calculate_helper(i):
            number = 0
            sign = 1
            result = 0
            while i < len(s):
                if s[i] == " ":
                    pass
                elif s[i].isdigit():
                    number = 10 * number + (ord(s[i]) - ord("0"))
                elif s[i] == "+":
                    result += sign * number
                    sign = 1
                    number = 0
                elif s[i] == "-":
                    result += sign * number
                    sign = -1
                    number = 0
                elif s[i] == "(":
                    result_in_parenthis, i = calculate_helper(i + 1)
                    result += sign * result_in_parenthis
                elif s[i] == ")":
                    result += sign * number
                    return result, i
                else:
                    raise RuntimeError(f"invalid char in input: {s[i]}")
                i += 1

            return result + sign * number, i

        return calculate_helper(0)[0]
