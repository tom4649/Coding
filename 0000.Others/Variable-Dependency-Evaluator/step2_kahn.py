import collections
import re


def evaluate(expressions: list[str]) -> dict[str, int]:
    dependency = collections.defaultdict(list)
    in_degree = collections.defaultdict(int)
    variable_to_expression = {}
    evaluated = {}

    # 1. Parse expressions and build dependency graph
    for expression in expressions:
        lhs, rhs = expression.split("=")
        variable = lhs.strip()

        # Parse terms with their signs
        # Example: "a - 3 + b" -> [(1, "a"), (-1, "3"), (1, "b")]
        rhs = re.sub(r"\s+", "", rhs)
        terms = re.findall(r"([+-]?)([A-Za-z][A-Za-z0-9_]*|\d+)", rhs)

        parsed_terms = []
        for sign, term in terms:
            coefficient = -1 if sign == "-" else 1
            parsed_terms.append((coefficient, term))

            if not term.isdecimal():
                dependency[term].append(variable)
                in_degree[variable] += 1

        variable_to_expression[variable] = parsed_terms

    # 2. Check undefined variables
    for variable in dependency:
        if variable not in variable_to_expression:
            raise ValueError("Unresolvable equations")

    # 3. Topological sort
    queue = collections.deque(
        variable
        for variable in variable_to_expression
        if in_degree[variable] == 0
    )

    while queue:
        variable = queue.popleft()

        # Evaluate expression
        value = 0
        for coefficient, term in variable_to_expression[variable]:
            if term.isdecimal():
                value += coefficient * int(term)
            else:
                value += coefficient * evaluated[term]

        evaluated[variable] = value

        # Update dependencies
        for next_variable in dependency[variable]:
            in_degree[next_variable] -= 1
            if in_degree[next_variable] == 0:
                queue.append(next_variable)

    # 4. Detect cycles
    if len(evaluated) != len(variable_to_expression):
        raise ValueError("Cyclic Dependency")

    return evaluated
