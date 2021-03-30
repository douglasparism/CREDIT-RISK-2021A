import functools
import time
from typing import Generic, TypeVar, Callable

A = TypeVar('A')
B = TypeVar('B')


def compose(this: Callable[..., A], and_then: Callable[[A], B]) -> Callable[..., B]:
    return lambda *x: and_then(this(*x))


def timeit(logger):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            output = func(*args, **kwargs)
            logger.warn("Execution time %s" % (time.time() - start))
            return output
        return wrapper
    return decorator


def caching(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = hash(frozenset(list(args) + list(kwargs.items())))
        if key in cache:
            return cache[key]
        cache[key] = func(*args, **kwargs)
        return wrapper(*args, **kwargs)
    return wrapper
