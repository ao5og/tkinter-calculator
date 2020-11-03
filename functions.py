


def add_digit(label, digit):
    current = label.get()
    if current != 'empty':
        new_string = current + digit
    else:
        new_string = digit

    label.set(new_string)

def add_dot(self):
    pass

def display_result(self, label):
    label.set(str(self.storage))

def set_operation(self, operation):
    pass

def clear(self):
    pass

def delete(self):
    pass