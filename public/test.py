




__fibo_recursive_cache = {}

def fibo_cache(n):
    if n in __fibo_recursive_cache:
        return __fibo_recursive_cache[n]
    else:
        result = n if n < 2 else fibo_recur(n - 1) + fibo_recur(n - 2)
        __fibo_recursive_cache[n] = result
        return result

print(fibo_cache(10))


def memoize(func):
    __cache = {}
    def wrapper(*args):
        print(__cache)
        if args in __cache:
            return __cache[args]
        else:
            __cache[args]= func(*args)
            return __cache[args]
    return wrapper


@memoize
def fibo_recur(n):
    return n if n < 2 else fibo_recur(n-1)+fibo_recur(n-2)

print(fibo_recur(10))








# memo = [0, 1, 1, 2, 3, 5 ...]
# cache = {}










