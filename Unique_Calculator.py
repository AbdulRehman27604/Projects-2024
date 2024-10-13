import tkinter as tk
import math
cal = tk.Tk()
CALCULATION = ""

def add_to_calculator(number):
    global CALCULATION
    CALCULATION += str(number)
    text_box.delete(1.0, "end")
    text_box.insert(1.0, CALCULATION)

def evaluate_str():
    global CALCULATION
    try:
        CALCULATION = str(eval(CALCULATION))
        text_box.delete(1.0,"end")
        text_box.insert(1.0, CALCULATION)
    except:
        clear_input()
        text_box.insert(1.0, "Error 365")

def clear_input():
    global CALCULATION
    CALCULATION = ""
    text_box.delete(1.0, "end")

cal.title("ARZ_Calculator")
cal.geometry("312x500")
cal.configure(bg="black")
text_box = tk.Text(cal, height=5, width=27, font=("Arial", 18), bg="grey")
text_box.place(x=4, y=8)

def Quadratics():
    #equation = print("Equation = " + str(square)+"X^2" + " " + "+" + " " + str(power1)+"X" + " " + "+" " " + str(noncoff))

    square = float(e1.get())
    power1 = float(e2.get())
    noncoff = float(e3.get())

    b = power1 * power1
    core = 4 * square * noncoff
    bottom = 2 * square

    if core > b:
        iota = b - core
        iota = iota * -1
        str_1 = "X = " + "("+str(-(power1)/bottom) + " " + "+" + " " + (str((math.sqrt(iota))/bottom)  + "i" + ")")
        str_2 = "Y = " + "("+str(-(power1)/bottom) + " " + "-" + " " + (str((math.sqrt(iota))/bottom)  + "i" + ")")
        text_box.delete(1.0, "end")
        text_box.insert(1.0, str_1)
        text_box.insert(1.0, str_2)
    else:
        new = b - core
        x = str(((-1 * power1))/bottom + ((math.sqrt(new))/bottom))
        y = str(((-1 * power1))/bottom - ((math.sqrt(new))/bottom))
        str_x = "X1 = ", x
        str_y = "X2 = ", y
        text_box.delete(1.0, "end")
        text_box.insert(1.0, str_x)
        text_box.insert(1.0, str_y)
    e1.delete(0,"end")
    e2.delete(0, "end")
    e3.delete(0, "end")


btn_7 = tk.Button(cal, text="7", height=2, width=2, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator(7)).place(x=10,y=250)
btn_8 = tk.Button(cal, text="8", height=2, width=2, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator(8)).place(x=76,y=250)
btn_9 = tk.Button(cal, text="9", height=2, width=2, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator(9)).place(x=146,y=250)
btn_4 = tk.Button(cal, text="4", height=2, width=2, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator(4)).place(x=10,y=320)
btn_5 = tk.Button(cal, text="5", height=2, width=2, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator(5)).place(x=76,y=320)
btn_6 = tk.Button(cal, text="6", height=2, width=2, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator(6)).place(x=146,y=320)
btn_1 = tk.Button(cal, text="1", height=2, width=2, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator(1)).place(x=10,y=390)
btn_2 = tk.Button(cal, text="2", height=2, width=2, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator(2)).place(x=76,y=390)
btn_3 = tk.Button(cal, text="3", height=2, width=2, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator(3)).place(x=146,y=390)
btn_0 = tk.Button(cal, text="0", height=1, width=17, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator(0)).place(x=10,y=460)

btn_plus = tk.Button(cal, text="+", height=1, width=5, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator("+")).place(x=220,y=250)
btn_minus = tk.Button(cal, text="-", height=1, width=5, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator("-")).place(x=220,y=305)
btn_multiply = tk.Button(cal, text="x", height=1, width=5, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator("*")).place(x=220,y=360)
btn_div = tk.Button(cal, text="÷", height=1, width=5, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator("/")).place(x=220,y=410)

btn_equal = tk.Button(cal, text="=", height=1, width=5, font=("Times", 18),bg="black",fg="black", command=lambda: evaluate_str()).place(x=220,y=460)
btn_clear = tk.Button(cal, text="Clear", height=1, width=5, font=("Times", 18),bg="black",fg="black", command=lambda: clear_input()).place(x=10,y=200)

btn_bracket_1 = tk.Button(cal, text="(", height=1, width=1, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator("(")).place(x=98,y=200)
btn_bracket_2 = tk.Button(cal, text=")", height=1, width=1, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator(")")).place(x=150,y=200)

btn_power = tk.Button(cal, text="^", height=1, width=1, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator("**")).place(x=205,y=200)
btn_root = tk.Button(cal, text="√", height=1, width=1, font=("Times", 18),bg="black",fg="black", command=lambda: add_to_calculator("**0.5")).place(x=260,y=200)

tk.Label(text="X^2:", font=("Times", 15), fg="black", bg="yellow").place(x=10, y=130)
e1 = tk.Entry(cal)
e1.place(x=55,y=131, width=50, height=22)

tk.Label(text="X: ", font=("Times", 15), fg="black", bg="yellow").place(x=115, y=130)
e2 = tk.Entry(cal)
e2.place(x=148,y=131, width=50, height=22)

tk.Label(text="No X:", font=("Times", 15), fg="black", bg="yellow").place(x=205, y=130)
e3 = tk.Entry(cal)
e3.place(x=258,y=131, width=50, height=22)

solve_button = tk.Button(cal, text="Solve", command=Quadratics)
solve_button.place(x=235, y=165)


tk.mainloop()