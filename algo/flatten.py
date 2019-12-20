def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


S = [2, 5, 6, [1, [[2]], [[[3]]]], [['4'], {5: 5}]]

print(flatten(S))

# ---------------2nd process----------------------------

from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)  # form use bcz of recurtion
        else:
            yield x


S = [2, 5, 6, [1, [[2]], [[[3]]]], [['4'], {5: 5}]]
for x in flatten(S):
    print(x)

