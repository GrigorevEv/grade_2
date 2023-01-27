def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count
    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
print('-' * 50)

# имена локальных и свободных переменных хранятся в атрибуте __code__
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print('-' * 50)

# сами переменные хранятся в ячейках cell атрибута __closure__
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)
print(avg.__closure__[1].cell_contents)

# Замыкание это функция, которая запоминает привязки свободных переменных
# существовавшие на момент определения функции, так что их можно использовать
# впоследствии при вызове функции, когда область видимости, в которой она
# была определена, уже не существует.
