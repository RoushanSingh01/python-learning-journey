"""Simple substitution cipher."""


class Cipher:
    """Encode and decode messages using a substitution cipher."""

    def __init__(self, key="aaaaaaaaaa"):
        """Store the cipher key."""
        self.key = key

    def encode(self, text):
        """Encode text."""
        return self._transform(text, 1)

    def decode(self, text):
        """Decode text."""
        return self._transform(text, -1)

    def _transform(self, text, direction):
        """Apply the cipher transformation."""
        result = []

        for index, character in enumerate(text):
            text_value = ord(character) - ord("a")

            key_value = (
                ord(
                    self.key[
                        index % len(self.key)
                    ]
                )
                - ord("a")
            )

            shifted = (
                text_value
                + direction * key_value
            ) % 26

            result.append(
                chr(
                    shifted
                    + ord("a")
                )
            )

        return "".join(result)