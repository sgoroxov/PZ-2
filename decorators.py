import time
from functools import wraps


def measure_time(func):
    """Измеряет время выполнения функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        print(f"[TIME] {func.__name__}: {time.time() - t0:.4f} сек")
        return result
    return wrapper


def log_call(func):
    """Логирует вызов функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[CALL] {func.__name__} -> {args} {kwargs}")
        res = func(*args, **kwargs)
        print(f"[DONE] {func.__name__}")
        return res
    return wrapper


def repeat(times=1):
    """Повторяет выполнение функции несколько раз."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = None
            for n in range(1, times + 1):
                print(f"Повтор {n}/{times}")
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator
