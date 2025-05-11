# Memoize Library (Task 3)

This library implements a configurable memoization decorator with the following features:

- ✅ LRU (Least Recently Used)
- ✅ LFU (Least Frequently Used)
- ✅ Time-Based Expiry
- ✅ Custom Eviction Policy

## Usage

```python
from memoize import memoize

@memoize(max_size=5, policy='LRU')
def add(a, b):
    return a + b
```
