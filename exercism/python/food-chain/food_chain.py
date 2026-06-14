"""Exercism solution for 'food-chain'."""

from dataclasses import dataclass
from itertools import chain
from typing import Optional


@dataclass
class RhymeAnimal:
    """Represent an animal and its associated rhyme lines."""

    name: str
    second_line: Optional[str]
    suffix: str = ""


ANIMALS = [
    RhymeAnimal("fly", None),
    RhymeAnimal(
        "spider",
        "It wriggled and jiggled and tickled inside her.",
        " that wriggled and jiggled and tickled inside her",
    ),
    RhymeAnimal("bird", "How absurd to swallow a bird!"),
    RhymeAnimal("cat", "Imagine that, to swallow a cat!"),
    RhymeAnimal("dog", "What a hog, to swallow a dog!"),
    RhymeAnimal("goat", "Just opened her throat and swallowed a goat!"),
    RhymeAnimal("cow", "I don't know how she swallowed a cow!"),
]


def verse(number: int) -> list[str]:
    """Return a single verse of the rhyme."""

    if number == 8:
        return [
            "I know an old lady who swallowed a horse.",
            "She's dead, of course!",
        ]

    animal = ANIMALS[number - 1]
    lines = [
        f"I know an old lady who swallowed a {animal.name}.",
    ]

    if animal.second_line is not None:
        lines.append(animal.second_line)

    lines.extend(
        [
            (
                f"She swallowed the {ANIMALS[animal_index + 1].name} "
                f"to catch the {ANIMALS[animal_index].name}"
                f"{ANIMALS[animal_index].suffix}."
            )
            for animal_index in range(number - 2, -1, -1)
        ]
    )

    lines.append("I don't know why she swallowed the fly. Perhaps she'll die.")
    return lines


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Return the requested range of verses."""

    lines = [
        verse(verse_number) + [""]
        for verse_number in range(start_verse, end_verse + 1)
    ]
    lines = list(chain.from_iterable(lines))
    lines.pop()
    return lines