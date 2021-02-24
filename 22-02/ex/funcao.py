print('-=' * 6)


def g(x):
    x += 1

    def h(y):
        return x + y
    return h(6)


def z(x):
    x = x + 1
    return n(5)


def n(y):
    return x + y


x = int(input('Me da um número inteiro:'))
print(g(x))
print(z(x))
