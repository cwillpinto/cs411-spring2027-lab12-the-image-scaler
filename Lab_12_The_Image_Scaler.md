# Lab 12: The Image Scaler

**CS 411: Computing Paradigms - Spring 2027**  
**Week 15: April 19-25, 2027**  
**Due:** April 25, 2027  
**Value:** 100 points

**Starter repository:** [Open the Spring 2027 starter](https://github.com/cwillpinto/cs411-spring2027-lab12-the-image-scaler)

## Purpose

Implement an event-driven image-scaling function. Measure cold and warm invocations separately, tolerate duplicate delivery, and explain which latency belongs to startup versus handler work.

## Learning objectives

- Trace an event through a FaaS invocation
- Measure cold and warm latency
- Protect a side effect from duplicate delivery

## Before you begin

1. Review the Week 15 slide deck and assigned VoiceThread or reading.
2. Create your own repository from the Spring 2027 template linked in Blackboard. It includes a 64 × 48 PNG input, an atomic in-memory object-store stand-in, public tests, and a timing driver.
3. Install dependencies with `python -m pip install -r requirements.txt`, then run `python -m pytest -q` before editing. Save the initial handler-TODO failures in `Lab12_Terminal.txt`.

## Part A Handler (35 points)

Implement the event contract.

- Complete `handle(event, store)` in `handler.py`. Require nonempty `event_id` and `source_path`, and integer width/height in the range 1–1024. Reject invalid events with `ValueError`.
- Open the supplied source image, resize to the requested dimensions, and encode PNG bytes. Return key, duplicate flag, width, height, handler time, and storage time as described in the function docstring.
- Choose a deterministic key from the stable event ID and requested dimensions. Use the supplied atomic `store.put_if_absent` so delivering the same event twice creates one logical output. Explain the assumption that one event ID refers to one logical request.

## Part B Timing (35 points)

Measure distinct invocation paths.

- Run `python benchmark.py` from a fresh Python process and save its CSV output as `Lab12_Timing.csv`. It measures one module import and first invocation, then five invocations in the same process using the same source image and dimensions but distinct event IDs.
- Report initialization, handler, storage, and total times separately. Compare the first row with the median warm row; state which time changed most.
- Explain the limit of this **local proxy**: module import and reused-process timing are observable here, but cloud scheduling, network, billing, and platform cold start are not measured.

## Part C Duplicate delivery (30 points)

Deliver the same event twice.

- In `Lab12_Analysis.md` or PDF, show the two public-test deliveries with the same event ID, output key, duplicate flag, and final store count of one.
- Explain why the conditional write is atomic in the supplied store and how a real object store would need an equivalent conditional operation.
- Recommend one suitable image-processing workload and one cold-start mitigation, using the timing evidence rather than a generic claim.

## Verification

- `python -m pytest -q` passes all public tests; save the complete output in `Lab12_Terminal.txt`.
- The CSV has one cold and five warm rows for the same input file and dimensions.
- Duplicate delivery produces one logical output with the same deterministic key.

## What to submit

Submit your own repository URL and:

1. Your own repository URL (created from the Spring 2027 template).
2. `handler.py` and the unchanged public `test_handler.py` in that repository.
3. `Lab12_Timing.csv` and `Lab12_Terminal.txt`.
4. `Lab12_Analysis.pdf` or `Lab12_Analysis.md`.

## Rubric

| Criterion | Points |
| --- | ---: |
| Handler correctness | 25 |
| Event validation and idempotency | 25 |
| Cold and warm measurements | 25 |
| Duplicate-delivery evidence | 15 |
| Recommendation | 10 |
| **Total** | **100** |

## AI usage and academic integrity

Add an **AI Usage** section to the required analysis file. Name each tool and list the prompts or interactions that affected the work. If you did not use AI, write `AI Usage: None.` You must be able to explain and defend every submitted design and line of code.

## Late work

Late work may be accepted for up to three calendar days with a 25 percent deduction per day, following the course syllabus.
