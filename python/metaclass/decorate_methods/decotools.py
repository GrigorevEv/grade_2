import time


def tracer(func):
    calls = 0

    def on_call(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f'call {calls} to {func.__name__}')
        return func(*args, **kwargs)
    return on_call


def timer(label='--> ', trace=True):
    def on_decorator(func):
        def on_call(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            on_call.alltime += elapsed
            if trace:
                fmt = '%s%s: %.9f, %.9f'
                values = (label, func.__name__, elapsed, on_call.alltime)
                print(fmt % values)
            return result
        on_call.alltime = 0
        return on_call
    return on_decorator
