"""Calculate Swift delivery dates."""

from calendar import FRIDAY, SATURDAY, SUNDAY, WEDNESDAY, monthrange
from datetime import datetime, timedelta


def at_hour(date_time, hour):
    """Return a datetime on the same date at the specified hour."""
    return datetime(
        date_time.year,
        date_time.month,
        date_time.day,
        hour,
    )


def delivery_date(start, description):
    """Calculate the delivery date for a scheduling code."""
    date_time = datetime.fromisoformat(start)

    match description:
        case "NOW":
            date_time += timedelta(hours=2)

        case "ASAP" if date_time.hour < 12:
            date_time = at_hour(date_time, 17)

        case "ASAP":
            date_time = at_hour(date_time + timedelta(days=1), 13)

        case "EOW" if date_time.weekday() <= WEDNESDAY:
            date_time = at_hour(
                date_time + timedelta(days=FRIDAY - date_time.weekday()),
                17,
            )

        case "EOW":
            date_time = at_hour(
                date_time + timedelta(days=SUNDAY - date_time.weekday()),
                20,
            )

        case "Q1":
            date_time = quarter_end(date_time, 1)

        case "Q2":
            date_time = quarter_end(date_time, 2)

        case "Q3":
            date_time = quarter_end(date_time, 3)

        case "Q4":
            date_time = quarter_end(date_time, 4)

        case _:
            month = int(description[:-1])

            date_time = datetime(
                date_time.year + (date_time.month >= month),
                month,
                1,
                8,
            )

            if date_time.weekday() >= SATURDAY:
                date_time += timedelta(days=7 - date_time.weekday())

    return date_time.isoformat()


def quarter_end(date_time, quarter_index):
    """Return the quarter-end delivery date."""
    month = 3 * quarter_index

    result = datetime(
        date_time.year,
        month,
        monthrange(date_time.year, month)[1],
        8,
    )

    if date_time >= result:
        result = datetime(
            date_time.year + 1,
            month,
            monthrange(date_time.year + 1, month)[1],
            8,
        )

    if result.weekday() >= SATURDAY:
        result -= timedelta(days=result.weekday() - FRIDAY)

    return result