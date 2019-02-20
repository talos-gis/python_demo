def aggregate(start, *parts, mutater, kw_mutater=lambda k, v: str(k) * v, **kwparts):
    # parts is a tuple
    # kwparts is a dict with str keys
    ret = start
    for p in parts:
        ret += mutater(p)
    for key, value in kwparts.items():
        ret += kw_mutater(key, value)

    return ret


print(aggregate('', 'a', 'b', 'c', mutater=str, d=3, x=2))
print(aggregate((), 3, 'hi', None,
                mutater=lambda x: (x,),
                kw_mutater=lambda k, v: (k,)*v, d=3, x=2))
