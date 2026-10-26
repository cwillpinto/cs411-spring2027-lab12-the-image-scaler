"""Event-driven image-scaling handler. Complete the TODOs, preserve the API."""

from io import BytesIO
from time import perf_counter

from PIL import Image

from store import InMemoryStore


def handle(event: dict, store: InMemoryStore) -> dict:
    """Return key, duplicate, width, height, handler_ms, and storage_ms."""
    start = perf_counter()
    # TODO: require nonempty event_id, source_path, and positive integer
    # width/height; reject dimensions above 1024. Open the source image,
    # resize it, encode PNG bytes, and choose a deterministic key using the
    # event ID and dimensions. Use store.put_if_absent so a retry with the
    # same event cannot create another object. Report separate times for
    # handler work and the conditional storage write.
    _ = (event, store, BytesIO, Image, start)
    raise NotImplementedError("complete the image-scaling handler")
