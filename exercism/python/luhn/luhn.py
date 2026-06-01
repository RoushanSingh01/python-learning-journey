"""Implementation of the Luhn checksum algorithm."""


class Luhn:
    """Validate strings using the Luhn algorithm."""

    def __init__(self, card_num):
        """Store the card number without spaces."""
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        """Return whether the card number is valid."""
        if not self.card_num.isdigit() or len(self.card_num) <= 1:
            return False

        digits = [int(digit) for digit in self.card_num]

        for index in range(len(digits) - 2, -1, -2):
            digits[index] *= 2

            if digits[index] > 9:
                digits[index] -= 9

        return sum(digits) % 10 == 0