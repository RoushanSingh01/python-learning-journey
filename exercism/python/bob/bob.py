"""Generate Bob's responses to conversational remarks."""


def response(remark):
    """Return Bob's response based on the remark type."""

    cleaned_remark = remark.strip()

    if cleaned_remark == "":
        return "Fine. Be that way!"

    is_question = cleaned_remark.endswith("?")
    is_yelling = (
        cleaned_remark.isupper()
        and any(character.isalpha() for character in cleaned_remark)
    )

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"

    if is_question:
        return "Sure."

    if is_yelling:
        return "Whoa, chill out!"

    return "Whatever."