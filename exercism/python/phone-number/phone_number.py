"""Clean and validate North American phone numbers."""


class PhoneNumber:
    """Represent a validated phone number."""

    def __init__(self, number):
        """Initialize a validated phone number."""
        number = "".join(
            char for char in number if char not in "().- +"
        )

        length = len(number)

        if length < 10:
            raise ValueError("must not be fewer than 10 digits")

        if length > 11:
            raise ValueError("must not be greater than 11 digits")

        if length == 11:
            if number[0] != "1":
                raise ValueError("11 digits must start with 1")
            number = number[1:]

        for char in number:
            if char.isalpha():
                raise ValueError("letters not permitted")
            if not char.isdigit():
                raise ValueError("punctuations not permitted")

        if number[0] == "0":
            raise ValueError("area code cannot start with zero")

        if number[0] == "1":
            raise ValueError("area code cannot start with one")

        if number[3] == "0":
            raise ValueError("exchange code cannot start with zero")

        if number[3] == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = number
        self.area_code = number[:3]

    def pretty(self):
        """Return the formatted phone number."""
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"