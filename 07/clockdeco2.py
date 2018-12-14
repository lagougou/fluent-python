import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(", ".join(repr(arg) for arg in args))
        if kwargs:
            pairs = ["%s=%r" %(k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(", ".join(pairs))
        print("[%0.8f] %s(%s) -> %r " %(elapsed,name,"".join(arg_lst),result))
        return result
    return clocked

            