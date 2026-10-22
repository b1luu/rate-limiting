# rate-limiting

Rate limiting algorithms built from scratch in Python, growing from a single in-memory class into a distributed limiter backed by Redis.

## Roadmap

- [ ] 1. Fixed window (in memory)
- [ ] 2. Tests with a fake clock
- [ ] 3. Sliding window log
- [ ] 4. Token bucket
- [ ] 5. Common interface for all algorithms
- [ ] 6. Thread safety
- [ ] 7. FastAPI middleware (HTTP 429 + `Retry-After`)
- [ ] 8. Redis backend (shared limit across servers)
- [ ] 9. Atomic updates with Redis Lua scripts
- [ ] 10. Load testing and benchmarks

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Design notes

See [DECISIONS.md](DECISIONS.md).
