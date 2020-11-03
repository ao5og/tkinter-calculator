


def add_digit(label, digit):
    current = label.get()
    if current != 'empty':
        new_string = current + digit
    else:
        new_string = digit

    label.set(new_string)