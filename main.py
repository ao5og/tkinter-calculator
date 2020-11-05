from tkinter import *
import functions as fn


class Calculator:
    def __init__(self, master):
        self.master = master
        self.button_side = 34
        self.font = ("Georgia", 15)

        # related to logic
        self.storage = 0
        self.current_operation = 'add'
        self.value = 0
        self.last_value = 0

        self.result = 0
        self.oper_funcs = ['add', 'sub', 'mul', 'div']
        self.opers_symbols = ['+', '-', 'x', '/']  #indeces 0,1,2,3


        # declaring and placing the main frame onto the master
        self.main_frame = Frame(self.master, bg="brown", relief=RAISED, bd=5)
        self.main_frame.pack()

        # the variable which displays on the display
        self.label_string = StringVar()
        self.label_string.set('0')

        # declaring all the frames and the label for display
        self.display_label = Label(self.main_frame,
                                   textvariable=self.label_string,
                                   bg="beige", font=self.font, padx=3, bd=10,
                                   relief=SUNKEN)
        self.digits_frame = Frame(self.main_frame, bg="beige")
        self.func_frame = Frame(self.main_frame, bg="beige")
        self.bottom_frame = Frame(self.main_frame, bg="beige")



        # placing each frame onto the main frame
        self.display_label.grid(row=0, column=0, columnspan=2, sticky='we')
        self.digits_frame.grid(row=1, column=0, padx=5, pady=5)
        self.func_frame.grid(row=1, column=1, padx=5, pady=5)
        self.bottom_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5,
                               sticky="we")

        #  buttons
        self.func_buttons = []
        self.bottom_buttons = []
        self.buttons = []

        self.add_main_digits_buttons(self.digits_frame)
        self.add_zero_button(self.digits_frame)
        self.add_dot_button(self.digits_frame)
        self.add_equal_button(self.digits_frame)

        self.add_function_buttons(self.func_frame)
        self.add_bottom_buttons(self.bottom_frame)



    def add_main_digits_buttons(self, parent):
        for r in range(3):
            for c in range(3):
                value = (c + 1) + (2 - r) * 3 # number on the button
                self.buttons.append(
                    Button(parent, text=str(value), padx=5, pady=1,
                           relief=RAISED, bg="lightblue",
                           font=self.font))
                self.buttons[-1].config(
                    command=lambda x=str(value): fn.add_digit(self.label_string, x))
                self.buttons[-1].grid(row=r, column=c, padx=2, pady=2)

    def add_zero_button(self, parent):
        # "0" digit button
        self.buttons.append(Button(parent, text=str(0), padx=5, pady=1,
                                   relief=RAISED, bg="lightblue",
                                   font=("Helvetica", 15)))
        self.buttons[-1].config(
            command=lambda x='0': fn.add_digit(self.label_string, x))
        self.buttons[-1].grid(row=3, column=0, padx=2, pady=2)

    def add_dot_button(self, parent):
        # "." button
        dot_button = Button(parent, text=".", padx=7, pady=1,
                            relief=RAISED, bg="lightblue",
                            font=("Helvetica", 15))
        dot_button.config(command=fn.add_dot)
        dot_button.grid(row=3, column=1, padx=2, pady=2)

    def add_equal_button(self, parent):
        # "=" button
        equalButton = Button(parent, text='=', padx=4, pady=1,
                             relief=RAISED, bg="lightblue",
                             font=("Helvetica", 15))
        equalButton.grid(row=3, column=2, padx=2, pady=2)
        equalButton.config(command=self.equal_press)

    def add_function_buttons(self, parent):
        for i in range(len(self.opers_symbols)):
            self.func_buttons.append(Button(parent, text=self.opers_symbols[i],
                                            padx=5, pady=1, relief=RAISED,
                                            bg="lightgreen", font=self.font))
            self.func_buttons[-1].grid(padx=2, pady=2, sticky = 'we')
            self.func_buttons[-1].config(
                command=lambda to_set=self.oper_funcs[i]: self.oper_press(to_set))


    def to_store(self):
        self.storage = int(self.label_string.get())
        print(f"storage is {self.storage}")

    def equal_press(self):
        """When equal is pressed.
        Storage is updated.
        Storage is displayed"""
        print("pressed equal")

        self.save_last_value()
        self.evaluate_equal()
        self.reset_label()
        self.display_storage()
        print("*****")


    def oper_press(self, to_set):
        """What happens when an operation button is pressed"""
        print(f"press on {to_set}")
        self.save_value()
        self.evaluate()
        self.set_operation(to_set) # change operation to new one
        self.reset_label() # set label back to zero
        print("******")

    def save_value(self):
        self.value = int(self.label_string.get())

    def save_last_value(self):
        self.last_value = self.value

    def reset_value(self):
        self.last_value = 0

    def evaluate(self):
        """Update storage with previous stored value [operation] new input"""
        # set storage to prev storage [oper] what's on the label
        print(f"Storage before press: {self.storage}, "
              f"operation before press: {self.current_operation}")
        if self.current_operation == 'add':
            self.storage = self.storage + self.value
        elif self.current_operation == 'sub':
            self.storage = self.storage - self.value
        elif self.current_operation == 'mul':
            self.storage = self.storage * self.value
        elif self.current_operation == 'div':
            self.storage = self.storage / self.value
        print(f"Applied value is {self.value}")
        print(f"Storage updated to {self.storage} ")

    def evaluate_equal(self):
        """Update storage with previous stored value [operation] new input"""
        # set storage to prev storage [oper] what's on the label

        if self.current_operation == 'add':
            self.storage = self.storage + self.last_value
        elif self.current_operation == 'sub':
            self.storage = self.storage - self.last_value
        elif self.current_operation == 'mul':
            self.storage = self.storage * self.last_value
        elif self.current_operation == 'div':
            self.storage = self.storage / self.last_value

        print(f"Storage updated to {self.storage} ")


    def set_operation(self, to_set):
        """Change the current operation"""
        self.current_operation = to_set  # now can change the operation
        print(f"operation is now {self.current_operation}")

    def reset_label(self):
        """Set label back to zero"""
        self.label_string.set('0')
        print("label set to zero")

    def display_storage(self):
        self.label_string.set(str(self.storage))


    def clear_all(self):
        self.last_value = 0
        self.value = 0
        self.current_operation = 'add'
        self.storage = 0
        self.reset_label()

    def delete(self):
        if len(self.label_string.get()) == 1:
            self.reset_label()
        else:
            self.label_string.set(self.label_string.get()[0:-1])




    def add_bottom_buttons(self, parent):
        self.bottom_buttons.append(Button(parent, bg="red", font=self.font,
                                          text="CLEAR", command=self.clear_all))
        self.bottom_buttons[-1].grid(row=0, column=0,padx=2, pady=2)
        self.bottom_buttons.append(Button(parent, bg ="red", font=self.font,
                                          text="DELETE", command=self.delete))
        self.bottom_buttons[-1].grid(row=0, column=1,padx=2, pady=2)



class App:
    def __init__(self, master):
        self.master = master
        calc = Calculator(self.master)


if __name__ == '__main__':
    root = Tk()
    root.title("Calculator")
    root.resizable(False, False)
    # root.geometry("500x500")
    root.configure(bg="blue")

    app = App(root)

    root.mainloop()


