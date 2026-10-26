"""Local FaaS proxy: module import once, then six same-input invocations."""
import importlib
from pathlib import Path
from time import perf_counter

from store import InMemoryStore

started = perf_counter()
handler = importlib.import_module("handler")
initialization_ms = (perf_counter() - started) * 1000
store = InMemoryStore()
source = str(Path("data/source.png"))
print("mode,invocation,initialization_ms,handler_ms,storage_ms,total_ms")
for index in range(6):
    event = {"event_id": f"run-{index}", "source_path": source, "width": 32, "height": 24}
    began = perf_counter()
    result = handler.handle(event, store)
    total_ms = (perf_counter() - began) * 1000
    print(f"{'cold' if index == 0 else 'warm'},{index},{initialization_ms if index == 0 else 0:.3f},{result['handler_ms']:.3f},{result['storage_ms']:.3f},{total_ms:.3f}")
assert store.count() == 6
