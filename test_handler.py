from io import BytesIO

import pytest
from PIL import Image

from handler import handle
from store import InMemoryStore


def event(event_id="job-1"):
    return {"event_id": event_id, "source_path": "data/source.png", "width": 32, "height": 24}


def test_scale_and_duplicate():
    store = InMemoryStore()
    first = handle(event(), store)
    second = handle(event(), store)
    assert first["duplicate"] is False
    assert second["duplicate"] is True
    assert first["key"] == second["key"]
    assert store.count() == 1
    with Image.open(BytesIO(store.get(first["key"]))) as image:
        assert image.size == (32, 24)
        assert image.format == "PNG"


@pytest.mark.parametrize("change", [{"event_id": ""}, {"width": 0}, {"height": -1}, {"width": 1025}, {"source_path": ""}])
def test_invalid_events(change):
    request = event()
    request.update(change)
    with pytest.raises(ValueError):
        handle(request, InMemoryStore())


def test_distinct_event_ids_have_distinct_outputs():
    store = InMemoryStore()
    one = handle(event("job-1"), store)
    two = handle(event("job-2"), store)
    assert one["key"] != two["key"]
    assert store.count() == 2
