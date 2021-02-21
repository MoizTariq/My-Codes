from tkinter import *
def calculate():
    bill = (800 * int(oe1.get().strip())) + (500 * int(oe2.get().strip())) + (350 * int(oe3.get().strip()))
    menu.destroy()
    order.destroy()
    receipt = Tk()
    receipt.resizable(0, 0)
    receipt.geometry("250x50")
    receipt.title("Receipt")
    Label(receipt, text = "Your bill = Rs.{}/-".format(bill), font = "Lato", bg = "#006241", fg = "white").pack()
    Label(receipt, text = "Thank you for ordering!", font = "Electra", fg = "#006241").pack()
    receipt.mainloop()
menu = Tk()
menu.resizable(0, 0)
order = Tk()
order.resizable(0, 0)
menu.title("Starbucks Menu")
menu.geometry("255x220")
#menu.iconbitmap("D:/Thunder Cross Split Attack/Starbucks.ico")
order.title("Order")
order.geometry("285x145")
#p1 = PhotoImage(file = "D:/Thunder Cross Split Attack/Starbucks.png")
#Label(menu, image = p1).pack()
ml = Label(menu, text = "Starbucks", font = ("Bebas Neue", 25, "bold", "italic", "underline"), fg = "#006241").place(x = 50, y = 10)
ml0 = Label(menu, text = "Menu", font = ("Bebas Neue", 20, "bold", "underline"), fg = "#006241").place(x = 90, y = 55)
ml1 = Label(menu, text = "1. Cappuccino...(Rs.800/-per cup)", font = "Electra", fg = "#006241").place(x = 4, y = 110)
ml2 = Label(menu, text = "2. Latte...............(Rs.500/-per cup)", font = "Electra", fg = "#006241").place(x = 4, y = 140)
ml3 = Label(menu, text = "3. Espresso.......(Rs.350/-per cup)", font = "Electra", fg = "#006241").place(x = 4, y = 170)
Label(menu, text = "All prices are inclusive of GST.", font = ("Electra", 8)).pack(side = "bottom")
ol0 = Label(order, text = "Quantity", font = "Electra").grid(row = 0, column = 1)
ol1 = Label(order, text = "Cappuccino", font = "Electra").grid(row = 1, column = 0)
ol2 = Label(order, text = "Latte", font = "Electra").grid(row = 2, column = 0)
ol3 = Label(order, text = "Espresso", font = "Electra").grid(row = 3, column = 0)
oe1 = Entry(order, justify = CENTER, font = "Lato")
oe1.grid(row = 1, column = 1)
oe2 = Entry(order, justify = CENTER, font = "Lato")
oe2.grid(row = 2, column = 1)
oe3 = Entry(order, justify = CENTER, font = "Lato")
oe3.grid(row = 3, column = 1, pady = 5)
b1 = Button(order, text = "Confirm Order", command = calculate, cursor = "hand2", font = ("Electra", "12", "italic"), width = 15, bd = 5).grid(row = 4, column = 1)
order.mainloop()
menu.mainloop()
