from functools import partial

basetwo = partial(int, base=2)

print(basetwo)

print(basetwo('10010'))