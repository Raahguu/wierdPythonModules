import inspect
import sys

global total_call_count
total_call_count = 0


def __trace(frame, event: str, args):
    global total_call_count
    if event == "call":
        total_call_count += 1

        code = frame.f_code
        func_name = code.co_qualname
        module = frame.f_globals.get("__name__", "?")

        arginfo = inspect.getargvalues(frame)
        # normal arguments
        func_args = {}
        for name in arginfo.args:
            value = arginfo.locals.get(name)
            func_args[name] = (type(value).__name__, value)

        # *args
        if arginfo.varargs:
            value = arginfo.locals.get(arginfo.varargs)
            func_args[f"*{arginfo.varargs}"] = (type(value).__name__, value)

        # **kwargs
        if arginfo.keywords:
            value = arginfo.locals.get(arginfo.keywords)
            func_args[f"**{arginfo.keywords}"] = (type(value).__name__, value)

        print(
            f"\033[1;32m{event.upper()}\033[0m \033[3m{module}.{func_name}\033[0m",
            end="",
        )
        if func_args == {}:
            print("()")
            return

        print("(")
        for name, (t, v) in func_args.items():
            try:
                v = repr(v)
            except AttributeError:
                v = f"<Unreprable object at 0x{id(v):x}>"
            print(f"\t{name}: {t} = {v}")
        print(")")
    elif event == "return":
        code = frame.f_code
        func_name = code.co_qualname
        module = frame.f_globals.get("__name__", "?")
        print(
            f"\033[1;34m{event.upper()}\033[0m \033[3m{module}.{func_name}\033[0m {args}"
        )
    elif event == "c_call":
        total_call_count += 1

        func = args

        owner_name = func.__module__
        end = func
        if func.__module__ is None and func.__self__ is not None:
            owner_name = (
                f"{type(func.__self__).__module__}.{type(func.__self__).__name__}"
            )
            end = f"on {func.__self__}"

        print(
            f"\033[1;32m{event.upper()}\033[0m \033[3m{owner_name}.{func.__name__}\033[0m {end}"
        )
    elif event == "c_return":
        func = args

        owner_name = func.__module__
        if func.__module__ is None and func.__self__ is not None:
            owner_name = (
                f"{type(func.__self__).__module__}.{type(func.__self__).__name__}"
            )

        print(
            f"\033[1;34m{event.upper()}\033[0m \033[3m{owner_name}.{func.__name__}\033[0m"
        )
    elif event in ("c_exception", "exception"):
        print(f"\033[1;31m{event.upper()}\033[0m \033[3m{args}\033[0m")


def enable():
    sys.setprofile(__trace)


def disable():
    sys.setprofile(None)
