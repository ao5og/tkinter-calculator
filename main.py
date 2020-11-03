from tkinter import *
import functions as fn


class Calculator:
    def __init__(self, master):
        self.master = master
        self.button_side = 34
        self.font = ("Georgia", 15)

        # related to logic
        self.storage = 0
        self.current_operation = ''


        # declaring and placing the main frame onto the master
        self.main_frame = Frame(self.master, bg="brown", relief=RAISED, bd=5)
        self.main_frame.pack()

        # the variable which displays on the display
        self.label_string = StringVar()
        self.label_string.set('empty')

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

    # functions used for the logic
    def add_digit(self, digit):
        current = self.label_string.get()
        if current != 'empty':
            new_string = current + digit
        else:
            new_string = digit

        self.label_string.set(new_string)


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
        dot_button.config(command=self.add_dot)
        dot_button.grid(row=3, column=1, padx=2, pady=2)

    def add_equal_button(self, parent):
        # "=" button
        equalButton = Button(parent, text='=', padx=4, pady=1,
                             relief=RAISED, bg="lightblue",
                             font=("Helvetica", 15))
        equalButton.grid(row=3, column=2, padx=2, pady=2)
        equalButton.config(command=self.display_result)

    def add_function_buttons(self, parent):
        opers_symbols = ['+', '-', 'x', '/']
        oper_funcs = ['add', 'sub', 'mul', 'div']
        for i in range(len(opers_symbols)):
            self.func_buttons.append(Button(parent, text=opers_symbols[i],
                                            padx=5, pady=1, relief=RAISED,
                                            bg="lightgreen", font=self.font))
            self.func_buttons[-1].grid(padx=2, pady=2, sticky = 'we')
            self.func_buttons[-1].config(
                command=lambda oper=oper_funcs[i]: self.set_operation(oper))

    def add_bottom_buttons(self, parent):
        self.bottom_buttons.append(Button(parent, bg="red", font=self.font,
                                          text="CLEAR", command=self.clear))
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


