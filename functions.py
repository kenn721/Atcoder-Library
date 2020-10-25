#n,m = map(int,input().split())

#! メモ化
def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)
from functools import lru_cache
@lru_cache(maxsize=1000)
def fib_memoized(n):
    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)

import bisect

array = []
bisect.insort_left(array,9)
bisect.insort_left(array,1)
bisect.insort_left(array,7)
bisect.insort_left(array,3)
bisect.insort_left(array,11)
bisect.insort_left(array,5)
print(array)
print(bisect.bisect_left(array,8))