# cache simples em memória (process-local)
import time

_cache = {}

def get(key):
    item = _cache.get(key)
    if not item:
        return None
    timestamp, value = item
    return (timestamp, value)

def set(key, value):
    _cache[key] = (time.time(), value)

def get_value(key):
    item = get(key)
    if not item:
        return None
    return item[1]
