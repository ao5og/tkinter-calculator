


def add_digit(label, digit_str):
    if label.get() != '0':
        new_string = label.get() + digit_str
    else:
        new_string = digit_str

    label.set(new_string)


