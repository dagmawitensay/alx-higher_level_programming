#!/urs/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a:
        return tuple_b
    elif not tuple_b:
        return tuple_a
    else:
        a0 = tuple_a[0]
        a1 = tuple_a[1] if len(tuple_a) >= 2 else 0
        b0 = tuple_b[0]
        b1 = tuple_b[1] if len(tuple_b) >= 2 else 0
    return (a0 + b0, a1 + b1)
