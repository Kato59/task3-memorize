from memoize import memoize
import time

@memoize(max_size=3, policy='LFU')
def slow_square(n):
    time.sleep(1)
    return n * n

for i in [2, 3, 2, 4, 5, 2, 3]:
    print(f"slow_square({i}) = {slow_square(i)}")
