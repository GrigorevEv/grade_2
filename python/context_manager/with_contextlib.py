import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write

    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Пожалуйста, не надо делить на нуль!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


with looking_glass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)
    raise ZeroDivisionError

print(what)
print('Alice, Kitty and Snowdrop')
