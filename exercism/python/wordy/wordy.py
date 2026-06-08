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
    except (IndexError, ValueError) as exc:
        raise ValueError("syntax error") from exc

    token_index = 1

    while token_index < len(tokens):
        operator = tokens[token_index]

        if operator not in {
            "plus",
            "minus",
            "multiplied_by",
            "divided_by",
        }:
            try:
                int(operator)
                raise ValueError("syntax error")
            except ValueError as error:
                if "syntax error" in str(error):
                    raise
                raise ValueError("unknown operation") from error

        if token_index + 1 >= len(tokens):
            raise ValueError("syntax error")

        try:
            value = int(tokens[token_index + 1])
        except ValueError as exc:
            raise ValueError("syntax error") from exc

        if operator == "plus":
            result += value
        elif operator == "minus":
            result -= value
        elif operator == "multiplied_by":
            result *= value
        elif operator == "divided_by":
            result //= value

        token_index += 2

    return result