"""Count rectangles in an ASCII diagram."""

from itertools import combinations


def rectangles(strings):
    """Return the number of rectangles."""
    return sum(
        1
        for verts in combinations(vertices(strings), 4)
        if is_rectangle(strings, verts)
    )


def vertices(strings):
    """Return all corner vertices."""
    return [
        (x, y)
        for y, row in enumerate(strings)
        for x, char in enumerate(row)
        if char == "+"
    ]


def is_rectangle(strings, verts):
    """Check whether four vertices form a rectangle."""
    top_left, bottom_left, top_right, bottom_right = sorted(verts)

    return all(
        (
            h_edge(strings, top_left, top_right),
            h_edge(strings, bottom_left, bottom_right),
            v_edge(strings, top_left, bottom_left),
            v_edge(strings, top_right, bottom_right),
        )
    )


def v_edge(strings, vertex_1, vertex_2):
    """Check a vertical edge."""
    x1, y1 = vertex_1
    x2, y2 = vertex_2

    return (
        x1 == x2
        and y1 < y2
        and all(
            strings[row][x1] in "+|"
            for row in range(y1, y2 + 1)
        )
    )


def h_edge(strings, vertex_1, vertex_2):
    """Check a horizontal edge."""
    x1, y1 = vertex_1
    x2, y2 = vertex_2

    return (
        y1 == y2
        and x1 < x2
        and all(
            strings[y1][column] in "+-"
            for column in range(x1, x2 + 1)
        )
    )