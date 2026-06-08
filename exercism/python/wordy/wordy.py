def answer(question):
    if not question.startswith("What is"):
        raise ValueError("unknown operation")

    problem = question.removeprefix("What is").strip()

    if not problem.endswith("?"):
        raise ValueError("syntax error")

    problem = problem[:-1].strip()

    if not problem:
        raise ValueError("syntax error")

    problem = (
        problem.replace("multiplied by", "multiplied_by")
        .replace("divided by", "divided_by")
    )

    tokens = problem.split()

    try:
        result = int(tokens[0])
    except (IndexError, ValueError):
        raise ValueError("syntax error")

    i = 1

    while i < len(tokens):
        op = tokens[i]

        if op not in {"plus", "minus", "multiplied_by", "divided_by"}:
            try:
                int(op)
                raise ValueError("syntax error")
            except ValueError as error:
                if "syntax error" in str(error):
                    raise
                raise ValueError("unknown operation")

        if i + 1 >= len(tokens):
            raise ValueError("syntax error")

        try:
            value = int(tokens[i + 1])
        except ValueError:
            raise ValueError("syntax error")

        if op == "plus":
            result += value
        elif op == "minus":
            result -= value
        elif op == "multiplied_by":
            result *= value
        elif op == "divided_by":
            result //= value

        i += 2

    return result