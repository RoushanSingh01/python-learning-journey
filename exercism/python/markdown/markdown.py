"""Exercism solution for 'markdown'."""

import re


def parse(markdown: str) -> str:
    """Parse Markdown and return HTML."""

    lines = markdown.split("\n")
    result = ""
    in_list = False

    for line in lines:
        if in_list and not re.match(r"\* ", line):
            result += "</ul>"
            in_list = False

        line = check_header(line)
        line, in_list = check_list(line, in_list)
        line = check_bold(line)
        line = check_italic(line)
        line = check_paragraph(line)
        result += line

    if in_list:
        result += "</ul>"

    return result


def check_header(text: str) -> str:
    """Convert Markdown headers to HTML headers."""

    match = re.match(r"^(#{1,6}) (.*)", text)
    if match:
        level = len(match.group(1))
        text = f"<h{level}>{match.group(2)}</h{level}>"

    return text


def check_list(text: str, in_list: bool) -> tuple[str, bool]:
    """Convert Markdown list items to HTML list items."""

    match = re.match(r"\* (.*)", text)
    if match:
        text = f"<li>{match.group(1)}</li>"
        if not in_list:
            in_list = True
            text = f"<ul>{text}"

    return text, in_list


def check_paragraph(text: str) -> str:
    """Wrap plain text in paragraph tags."""

    if not re.match(r"<h|<ul|<li", text):
        text = f"<p>{text}</p>"

    return text


def check_bold(text: str) -> str:
    """Convert Markdown bold syntax to HTML."""

    match = re.match(r"(.*)__(.*)__(.*)", text)
    if match:
        text = (
            f"{match.group(1)}"
            f"<strong>{match.group(2)}</strong>"
            f"{match.group(3)}"
        )

    return text


def check_italic(text: str) -> str:
    """Convert Markdown italic syntax to HTML."""

    match = re.match(r"(.*)_(.*)_(.*)", text)
    if match:
        text = (
            f"{match.group(1)}"
            f"<em>{match.group(2)}</em>"
            f"{match.group(3)}"
        )

    return text