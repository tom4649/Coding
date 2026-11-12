import collections

def evaluate(expressions: list[str]) -> dict[str, int]:
    dependency = collections.defaultdict(list)
    in_degree = collections.defaultdict(int)
    variable_to_expression = {}
    evaluated = {}
    for expression in expressions:
        lhs, rhs = expression.split("=")
        rhs = rhs.strip()
        left_variable = lhs.strip()

        if "+" in rhs or "-" in rhs:
            if "+" in rhs:
                op1, op2 = rhs.split("+")
            else:
                op1, op2 = rhs.split("-")
            for op in (op1, op2):
                op = op.strip()
                if not op.isdecimal():
                    dependency[op].append(left_variable)
                    in_degree[left_variable] += 1
                variable_to_expression[left_variable] = rhs
        elif rhs.isdecimal():
            evaluated[left_variable] = int(rhs)
            variable_to_expression[left_variable] = rhs
        else:
            right_valiable = rhs.strip()
            dependency[right_valiable].append(left_variable)
            in_degree[left_variable] += 1
            variable_to_expression[left_variable] = right_valiable

    for variable in dependency:
        if variable not in variable_to_expression:
            raise ValueError("Unresolvable equations")

    evaluated_variables = collections.deque([variable for variable in variable_to_expression if in_degree[variable] == 0])
    while evaluated_variables:
        variable = evaluated_variables.pop()
        expression = variable_to_expression[variable]
        if variable in evaluated:
            pass
        elif "+" in expression or "-" in expression:
            if "+" in expression:
                op1, op2 = expression.split("+")
            else:
                op1, op2 = expression.split("-")
            evaluated_ops = []
            for op in (op1, op2):
                op = op.strip()
                if op.isdecimal():
                    evaluated_ops.append(int(op))
                elif op not in variable_to_expression:
                    raise ValueError("Unresolvable equations")
                else:
                    evaluated_ops.append(evaluated[op])
            if "+" in expression:
                evaluated_expression = evaluated_ops[0] + evaluated_ops[1]
            else:
                evaluated_expression = evaluated_ops[0] - evaluated_ops[1]
            evaluated[variable] = evaluated_expression
        elif expression.isdecimal():
            evaluated[variable] = int(expression)
        else:
            right_valiable = expression.strip()
            evaluated[variable] = evaluated[right_valiable]

        for depended_variable in dependency[variable]:
            in_degree[depended_variable] -= 1
            if in_degree[depended_variable] == 0:
                evaluated_variables.append(depended_variable)

    if len(evaluated) != len(variable_to_expression):
        raise ValueError("Cyclic Dependency")

    return evaluated


expressions1 = [
    "a = 3",
    "b = a + 1"
]
print(evaluate(expressions1))

expressions2 = [
    "a = b + 1",
    "c = 3"
]
evaluate(expressions2)
