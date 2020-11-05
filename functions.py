


def add_digit(label, digit_str):
    if label.get() != '0':
        new_string = label.get() + digit_str
    else:
        new_string = digit_str

    label.set(new_string)

def add_dot(self):
    pass

def display_result(self, label):
    label.set(str(self.storage))


def clear(self):
    pass

def delete(self):
    pass