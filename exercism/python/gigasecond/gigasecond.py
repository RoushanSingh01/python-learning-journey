"""Calculate the date after a gigasecond."""


from datetime import timedelta


def add(moment):
    """Return the datetime one gigasecond after the given moment."""

    return moment + timedelta(seconds=10**9)