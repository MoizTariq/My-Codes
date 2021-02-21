from tkinter import *
operator = "none"
def add():
    e1.insert(0, 0)
    global first_num
    global operator
    first_num = float(e1.get().strip())
    e1.delete(0, END)
    operator = "+"
def subtract():
    e1.insert(0, 0)
    global first_num
    global operator
    first_num = float(e1.get().strip())
    e1.delete(0, END)
    operator = "-"
def multiply():
    e1.insert(0, 0)
    global first_num
    global operator
    first_num = float(e1.get().strip())
    e1.delete(0, END)
    operator = "x"
def divide():
    e1.insert(0, 0)
    global operator
    global first_num
    first_num = float(e1.get().strip())
    e1.delete(0, END)
    operator = "/"

def calculate():
    e1.insert(0, 0)
    second_num = float(e1.get().strip())
    ans = IntVar
    if operator == "+":
        ans = first_num + second_num
    elif operator == "-":
        ans = first_num - second_num
    elif operator == "x":
        ans = first_num * second_num
    elif operator == "/":
        ans = first_num / second_num
    elif operator == "none":
        ans = float(e1.get().strip())
    e1.delete(0, END)
    if ans % 1 == 0:
        e1.insert(0, int(ans))
    else:
        e1.insert(0, ans)
def insert(f):
    e1.insert(END, f)
def clear():
    e1.delete(0, END)
def backspace():
    e1.delete(len(e1.get().strip()) - 1)

calculator = Tk()
calculator.title("Calculator by Moiz Tariq")
calculator.geometry("264x350")
calculator.resizable()

e1 = Entry(calculator, justify = RIGHT, font = ("Bold", 47), width = 140)
e1.pack(side = TOP)

b1 = Button(calculator, text = "+", command = add, bd = 5, font = 12, width = 6, height = 2, activebackground = "Light Gray").place(x = 195, y = 240)
b2 = Button(calculator, text = "-", command = subtract, bd = 5, font = 12, width = 6, height = 2, activebackground = "Light Gray").place(x = 195, y = 185)
b3 = Button(calculator, text = "x", command = multiply, bd = 5, font = 12, width = 6, height = 2, activebackground = "Light Gray").place(x = 195, y = 130)
b4 = Button(calculator, text = "÷", command = divide, bd = 5, font = 12, width = 6, height = 2, activebackground = "Light Gray").place(x = 195, y = 75)
b5 = Button(calculator, text = "=", command = calculate, bg = "light gray", bd = 5, font = 12, width = 6, height = 2).place(x = 195, y = 295)
b6 = Button(calculator, text = "1", command = lambda : insert(1), bd = 5, font = "Bold", bg = "white", width = 6, height = 2, activebackground = "Light Gray").place(x = 0, y = 240)
b7 = Button(calculator, text = "2", command = lambda : insert(2), bd = 5, font = "Bold", bg = "white", width = 6, height = 2, activebackground = "Light Gray").place(x = 65, y = 240)
b8 = Button(calculator, text = "3", command = lambda : insert(3), bd = 5, font = "Bold", bg = "white", width = 6, height = 2, activebackground = "Light Gray").place(x = 130, y = 240)
b9 = Button(calculator, text = "4", command = lambda : insert(4), bd = 5, font = "Bold", bg = "white", width = 6, height = 2, activebackground = "Light Gray").place(x = 0, y = 185)
b10 = Button(calculator, text = "5", command = lambda : insert(5), bd = 5, font = "Bold", bg = "white", width = 6, height = 2, activebackground = "Light Gray").place(x = 65, y = 185)
b11 = Button(calculator, text = "6", command = lambda : insert(6), bd = 5, font = "Bold", bg = "white", width = 6, height = 2, activebackground = "Light Gray").place(x = 130, y = 185)
b12 = Button(calculator, text = "7", command = lambda : insert(7), bd = 5, font = "Bold", bg = "white", width = 6, height = 2, activebackground = "Light Gray").place(x = 0, y = 130)
b13 = Button(calculator, text = "8", command = lambda : insert(8), bd = 5, font = "Bold", bg = "white", width = 6, height = 2, activebackground = "Light Gray").place(x = 65, y = 130)
b14 = Button(calculator, text = "9", command = lambda : insert(9), bd = 5, font = "Bold", bg = "white", width = 6, height = 2, activebackground = "Light Gray").place(x = 130, y = 130)
b15 = Button(calculator, text = "0", command = lambda : insert(0), bd = 5, font = " Bold", bg = "white", width = 13, height = 2, activebackground = "Light Gray").place(x = 0, y = 295)
b16 = Button(calculator, text = ".", command = lambda : insert("."), bd = 5, font = "Bold", bg = "white", width = 6, height = 2, activebackground = "Light Gray").place(x = 130, y = 295)
b17 = Button(calculator, text = "Clear", command = clear, bd = 5, width = 16, height = 2, padx = 5, pady = 5, activebackground = "Light Gray").place(x = 0, y = 75)
b18 = Button(calculator, text = "←", command = backspace, bd = 5, font = "Bold", width = 6, height = 2, activebackground = "Light Gray").place(x = 130, y = 75)

calculator.mainloop()
