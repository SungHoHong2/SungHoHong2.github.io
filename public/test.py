__cache = {}

def memoize(func):
    return lambda *args: __cache[args] if args in __cache else __cache.update({args: func(*args)}) or __cache[args]

@memoize
def fibo_recur(n):
    return n if n<2 else fibo_recur(n-1)+fibo_recur(n-2)

print(fibo_recur(10))

print(__cache)




