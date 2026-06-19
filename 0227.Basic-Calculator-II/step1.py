class Solution:
    def calculate(self, s: str) -> int:
        def parse_number(left):
            number = 0
            right = left
            while right < len(s) and s[right].isdigit():
                right += 1

            return s[left:right], right

        operator_to_func = {
            "*": lambda ops: ops[0] * ops[1],
            "/": lambda ops: ops[0] // ops[1],
        }

        to_be_calculated = []
        i = 0
        result = 0
        sign = 1
        while i < len(s):
            if s[i] == " ":
                i += 1
            elif s[i].isdigit():
                number, i = parse_number(i)
                to_be_calculated.append(number)
            elif s[i] in ["*", "/"]:
                operator = s[i]
                op1 = to_be_calculated.pop()
                i += 1
                while s[i] == " ":
                    i += 1
                assert s[i].isdigit(), s[i]
                op2, i = parse_number(i)
                number = operator_to_func[operator]((int(op1), int(op2)))
                to_be_calculated.append(str(number))
            elif s[i] in ["+", "-"]:
                to_be_calculated.append(s[i])
                i += 1
            else:
                raise RuntimeError("invalid input")

        result = 0
        sign = 1
        number = 0
        i = 0
        print(to_be_calculated)
        while i < len(to_be_calculated):
            if to_be_calculated[i].isdigit():
                result += int(to_be_calculated[i]) * sign
                i += 1
            elif to_be_calculated[i] == "+":
                sign = 1
                i += 1
            elif to_be_calculated[i] == "-":
                sign = -1
                i += 1
            else:
                raise RuntimeError("invalid input")

        return result
