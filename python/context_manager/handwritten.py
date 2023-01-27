# Предложение with служит для упрощения конструкции try/finally
# Вначале блока with вызывается метод __enter__
# Роль части finally играет обращение к методу __exit__

from unittest.mock import patch
class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Пожалуйста, не надо делить на нуль!')
            return True


with LookingGlass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)
    raise ZeroDivisionError

print(what)
print('Alice, Kitty and Snowdrop')
