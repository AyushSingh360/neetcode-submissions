from typing import List, Optional

class DynamicArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            capacity = 1
        self._capacity: int = capacity
        self._size: int = 0
        self._data: List[Optional[int]] = [None] * self._capacity

    def get(self, i: int) -> int:
        """Return element at index i. Raises IndexError if out of bounds."""
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds")
        return self._data[i]  # type: ignore[return-value]

    def set(self, i: int, n: int) -> None:
        """Set element at index i to n. Raises IndexError if out of bounds."""
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds")
        self._data[i] = n

    def pushback(self, n: int) -> None:
        """Append n to the end, resizing if necessary."""
        if self._size == self._capacity:
            self.resize()  # will grow capacity
        self._data[self._size] = n
        self._size += 1

    def popback(self) -> int:
        """Remove and return the last element. Raises IndexError if empty."""
        if self._size == 0:
            raise IndexError("Pop from empty DynamicArray")
        val = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return val  # type: ignore[return-value]

    def resize(self) -> None:
        """
        Adjust capacity:
        - Doubling the capacity.
        """
        new_capacity = max(1, self._capacity * 2)

        new_data: List[Optional[int]] = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def getSize(self) -> int:
        """Return current number of elements."""
        return self._size

    def getCapacity(self) -> int:
        """Return current underlying capacity."""
        return self._capacity