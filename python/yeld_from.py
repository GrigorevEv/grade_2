def chain(*iterable):
    for it in iterable:
        for i in it:
            yield i


s = 'ABC'
t = (1, 2, 3)
print(list(chain(s, t)))


def chain(*iterable):
    for i in iterable:
        yield from i

print(list(chain(s, t)))
