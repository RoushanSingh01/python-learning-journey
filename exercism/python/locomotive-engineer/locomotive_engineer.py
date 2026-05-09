"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons."""

    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons."""

    engine_index = each_wagons_id.index(1)

    return (
        [each_wagons_id[engine_index]]
        + missing_wagons
        + each_wagons_id[engine_index + 1:]
        + each_wagons_id[:engine_index]
    )


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict."""

    route["stops"] = list(kwargs.values())

    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information."""

    return {
        **route,
        **more_route_information,
    }


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons."""

    return [
        [
            wagons_rows[0][0],
            wagons_rows[1][0],
            wagons_rows[2][0],
        ],
        [
            wagons_rows[0][1],
            wagons_rows[1][1],
            wagons_rows[2][1],
        ],
        [
            wagons_rows[0][2],
            wagons_rows[1][2],
            wagons_rows[2][2],
        ],
    ]