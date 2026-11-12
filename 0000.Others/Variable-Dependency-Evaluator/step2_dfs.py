import re


def evaluate(expressions: list[str]) -> dict[str, int]:
    variable_to_expression = {}

    # 1. Parse expressions
    for expression in expressions:
        lhs, rhs = expression.split("=")
        variable = lhs.strip()

        rhs = re.sub(r"\s+", "", rhs)
        terms = re.findall(
            r"([+-]?)([A-Za-z][A-Za-z0-9_]*|\d+)", rhs
        )

        variable_to_expression[variable] = [
            (-1 if sign == "-" else 1, term)
            for sign, term in terms
        ]

    evaluated = {}
    visiting = set()

    # 2. DFS
    def dfs(variable: str) -> int:
        if variable in evaluated:
            return evaluated[variable]

        if variable not in variable_to_expression:
            raise ValueError("Unresolvable equations")

        if variable in visiting:
            raise ValueError("Cyclic Dependency")

        visiting.add(variable)

        value = 0
        for coefficient, term in variable_to_expression[variable]:
            if term.isdecimal():
                value += coefficient * int(term)
            else:
                value += coefficient * dfs(term)

        visiting.remove(variable)
        evaluated[variable] = value
        return value

    # 3. Evaluate all variables
    for variable in variable_to_expression:
        dfs(variable)

    return evaluated
