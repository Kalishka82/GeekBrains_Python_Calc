x = 0
y = 0


def init(a, b, c, d):
    global x, y
    x = complex(a, b)
    y = complex(c, d)


def return_x():
    return x


def return_y():
    return y


def do_sum():
    return round_complex(x + y)


def do_sub():
    return round_complex(x - y)


def do_mult():
    return round_complex(x * y)


def do_div():
    return round_complex(x / y)


def do_it(action):
    if action == '+':
        return do_sum()
    elif action == '-':
        return do_sub()
    elif action == '*':
        return do_mult()
    elif action == '/':
        return do_div()
    else:
        return "Error!"


def round_complex(z):
    return complex(round(z.real, 5), round(z.imag, 5))
