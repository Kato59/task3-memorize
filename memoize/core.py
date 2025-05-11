from collections import OrderedDict, defaultdict
import time

def memoize(func, max_size=None, policy='LRU', timeout=None, custom_policy=None):
    cache = OrderedDict()
    usage_count = defaultdict(int)
    timestamps = {}

    def wrapper(*args):
        now = time.time()
        if args in cache:
            if timeout and now - timestamps[args] > timeout:
                del cache[args]
                del timestamps[args]
                if args in usage_count:
                    del usage_count[args]
            else:
                usage_count[args] += 1
                cache.move_to_end(args)
                return cache[args]

        result = func(*args)
        cache[args] = result
        usage_count[args] = 1
        timestamps[args] = now

        if max_size and len(cache) > max_size:
            if policy == 'LFU':
                least_used = min(usage_count, key=usage_count.get)
                del cache[least_used]
                del usage_count[least_used]
                del timestamps[least_used]
            elif policy == 'custom' and custom_policy:
                to_remove = custom_policy(cache)
                del cache[to_remove]
                if to_remove in usage_count: del usage_count[to_remove]
                if to_remove in timestamps: del timestamps[to_remove]
            else:
                oldest = next(iter(cache))
                del cache[oldest]
                if oldest in usage_count: del usage_count[oldest]
                if oldest in timestamps: del timestamps[oldest]
        return result

    return wrapper
