import re
import collections

def evaluate(expressions: list[str]) -> dict[str, int]:
    variable_to_expression = collections.defaultdict(list)

    for expression in expressions:
        lhs, rhs = expression.split("=")
        variable = lhs.strip()
        rhs = re.sub(r"\s+", "", rhs)
        terms = re.findall(r"([+-]?)([A-Za-z][A-Za-z0-9_]*|\d+)", rhs)

        for sign, term in terms:
            variable_to_expression[variable].append((
                -1 if sign == "-" else 1, term
            ))

    evaluated = {}
    visiting = set()

    def evaluate_variable(variable):
        if variable in evaluated:
            return evaluated[variable]

        if variable in visiting:
            raise ValueError("Cyclic Dependency")

        if variable not in variable_to_expression:
            raise ValueError("Unresolvable equations")

        visiting.add(variable)

        value = 0
        for sign, term in variable_to_expression[variable]:
            if term.isdecimal():
                value += sign * int(term)
            else:
                value += sign * evaluate_variable(term)

        visiting.remove(variable)
        evaluated[variable] = value

        return value

    for variable in variable_to_expression:
        evaluate_variable(variable)

    return evaluated


def check_error(expressions):
    try:
        print(evaluate(expressions))
    except ValueError as e:
        print(e)

expressions_normal = [
    "a = 3",
    "b = a + 1"
]
print("case 1")
check_error(expressions_normal)

expressions_normal2 = [
    "a = b + 1",
    "b = 2"
]
print("case 2")
check_error(expressions_normal2)

expressions_normal3 = [
    "a = b + 1",
    "b = 2",
    "c = b"
]
print("case 3")
check_error(expressions_normal3)

expressions_cyclic = [
    "a = b + 1",
    "b = a"
]
print("case 4")
check_error(expressions_cyclic)

expressions_cyclic2 = [
    "a = a + 1",
]
print("case 5")
check_error(expressions_cyclic2)

expressions_unresolved = [
    "a = b + 1",
    "c = 3"
]
print("case 6")
check_error(expressions_unresolved)





