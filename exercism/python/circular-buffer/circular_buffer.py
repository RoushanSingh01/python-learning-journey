"""Circular buffer implementation."""


class BufferFullException(BufferError):
    """Raised when the circular buffer is full."""


class BufferEmptyException(BufferError):
    """Raised when the circular buffer is empty."""


class CircularBuffer:
    """Fixed-capacity circular buffer."""

    def __init__(self, capacity):
        """Initialize an empty buffer."""
        self.buffer = []
        self.capacity = capacity

    def read(self):
        """Read and remove the oldest item."""
        if not self.buffer:
            raise BufferEmptyException(
                "Circular buffer is empty"
            )

        return self.buffer.pop(0)

    def write(self, data):
        """Write data to the buffer."""
        if len(self.buffer) >= self.capacity:
            raise BufferFullException(
                "Circular buffer is full"
            )

        self.buffer.append(data)

    def overwrite(self, data):
        """Overwrite oldest item if full."""
        if len(self.buffer) >= self.capacity:
            self.buffer.pop(0)

        self.buffer.append(data)

    def clear(self):
        """Remove all items."""
        self.buffer.clear()