import tkinter as tk
import time
import random
JS = tk.Tk()
PK = tk.Tk()


def run_jeddah_Steel():
    layout()
    value_items()
    menu_bar()
    measurements()
    comment_box()
    list_options()
    buttonFuctionality()
    JS.mainloop()

def layout():
    JS.geometry("1270x500")
    JS.configure(bg="#333333")
    JS.title("Jeddah Steel Interface")
    label = tk.Label(JS, text="Jeddah Steel Pvt Ltd", height=10, font=("Helvetica", 20, "bold italic"), fg="Yellow", bg="#333333")
    label.place(x=1050, y=10, height=40, width=210)

def buttonFuctionality():
    button = tk.Button(JS, text="Submit", font=("Times", 20, "bold"), fg="red")
    button.place(x=1140, y=445,height=50,width=120)

def value_items():
    grid_frame = JS
    tk.Label(grid_frame, text="Cutting Job:", bg="#333333", font=("Times", 20), fg="white").grid(row=0,column=0)
    tk.Label(grid_frame, text='Job Number:', bg="#333333", font=("Times",16), fg="white").grid(row=1, column=0)
    tk.Label(grid_frame, text='Supplier Code:', font=("Times",16), bg="#333333", fg="white").grid(row=2, column=0)
    tk.Label(grid_frame, text='Broker Code:', font=("Times",16), bg="#333333", fg="white").grid(row=3, column=0)
    e1 = tk.Entry(grid_frame).grid(row=1, column=1)
    e2 = tk.Entry(grid_frame).grid(row=2, column=1)
    e3 = tk.Entry(grid_frame).grid(row=3, column=1)

def comment_box():
    tk.Label(text="Comments:",bg="black", font=("Times",16), fg="white").place(x=7, y=202, height=30, width=115)
    comment = tk.Text(JS).place(x=130, y=200, height=55, width=250)

def list_options():
    tk.Label(JS, text="Supplier Name:", font=("Times",16), fg="white", bg="black").place(x=6,y=142,height=30,width=120)
    new_box = tk.Listbox(JS)
    new_box.insert(tk.END, "- AISHA STEEL LTD")
    new_box.insert(tk.END, "- GUL DEEWAN")
    new_box.insert(tk.END, "- China")
    new_box.insert(tk.END, "- P&O")
    new_box.place(x=129, y=132, height=55, width=250)

    #Coil Type
    tk.Label(JS, text="Coil Type:", font=("Times", 16), fg="white", bg="black").place(x=850, y=400, height=30,
                                                                                          width=120)
    box = tk.Listbox(JS)
    box.insert(tk.END, "- CRC")
    box.insert(tk.END, "- HRC")
    box.insert(tk.END, "- GI")
    box.insert(tk.END, "- P&O")
    box.place(x=850, y=430, height=55, width=250)

def menu_bar():
    home = tk.Menu(JS)
    JS.configure(menu=home)
    file_menu = tk.Menu(home)
    home.add_cascade(label="Home",menu=file_menu)
    file_menu.add_command(label="Cutting Job")
    file_menu.add_command(label="Transactions")
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=JS.quit)

def measurements():
    tk.Label(JS, text="Width:", font=("Times",16), fg="white", bg="black").place(x=400,y=70,height=30,width=120)
    width = tk.Entry(JS).place(x=525,y=70,height=30,width=120)

    tk.Label(JS, text="Utilize:", font=("Times", 16), fg="white", bg="black").place(x=400, y=112, height=30, width=120)
    utilize = tk.Entry(JS).place(x=525, y=112, height=30, width=120)

    tk.Label(JS, text="Wastage:", font=("Times", 16), fg="white", bg="black").place(x=400, y=154, height=30, width=120)
    wastage = tk.Entry(JS).place(x=525, y=154, height=30, width=120)

    tk.Label(JS, text="Weight MM:", font=("Times", 16), fg="white", bg="black").place(x=660, y=70, height=30, width=120)
    weightMM = tk.Entry(JS).place(x=785, y=70, height=30, width=120)

    tk.Label(JS, text="T.pipe:", font=("Times", 16), fg="white", bg="black").place(x=660, y=112, height=30, width=120)
    Tpipe = tk.Entry(JS).place(x=785, y=112, height=30, width=120)

    tk.Label(JS, text="DC No:", font=("Times", 16), fg="white", bg="black").place(x=920, y=112, height=30, width=120)
    Tpipe = tk.Entry(JS).place(x=1045, y=112, height=30, width=120)

    tk.Label(JS, text="Order No:", font=("Times", 16), fg="white", bg="black").place(x=920, y=70, height=30, width=120)
    Tpipe = tk.Entry(JS).place(x=1045, y=70, height=30, width=120)

#def numbers():
    





def update_time():
    global clock_label
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    JS.after(1000, update_time)

def password_main_layout():
    PK.geometry("1270x500")
    PK.configure(bg="#333333")
    PK.title("Jeddah Steel Interface")
    label = tk.Label(PK, text="Jeddah Steel Pvt Ltd", height=10, font=("Times", 50), fg="Yellow", bg="#333333")
    label.place(x=370, y=10, height=40, width=500)

    tk.Label(PK, text="Username: ", font=("Arial", 18), fg="white").place(x=500, y=250)
    username_entry = tk.Entry(PK, font=("Arial", 18))
    username_entry.place(x=600, y=250, height=30, width=180)

    tk.Label(PK, text="Password: ", font=("Arial", 18), fg="white").place(x=500, y=300)
    password_entry = tk.Entry(PK, font=("Arial", 18), show="*")
    password_entry.place(x=600, y=300, height=30, width=180)

    btn_login = tk.Button(PK, text="Login", font=("Arial", 18), command=lambda: is_password_ok(username_entry.get(), password_entry.get()))
    btn_login.place(x=600, y=350)

    PK.mainloop()

def is_password_ok(username, password):
    if username == "ARZ" and password == "123":
        PK.destroy()
        run_jeddah_Steel()
    else:
        pass

password_main_layout()
#run_jeddah_Steel()