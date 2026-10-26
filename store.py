from threading import Lock


class InMemoryStore:
    """Supplied local stand-in for an atomic object-store conditional put."""

    def __init__(self):
        self._items = {}
        self._lock = Lock()

    def put_if_absent(self, key: str, payload: bytes) -> bool:
        with self._lock:
            if key in self._items:
                return False
            self._items[key] = payload
            return True

    def get(self, key: str) -> bytes:
        return self._items[key]

    def count(self) -> int:
        return len(self._items)
