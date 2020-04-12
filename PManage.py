import tkinter as tk
from tkinter import *
import os

root = tk.Tk()

root.title("Smart Portfolio Management System")

canvas = tk.Canvas(root, height=600, width=900)
canvas.pack()


def retreive():
    stocks = []
    info = ""
    stocks = stock_entry.get().split(',')
    for stock in stocks:
        stock = stock.strip()
        if stock.lower() == "google":
            stock = "GOOG"
        elif stock.lower() == "amazon":
            stock = "AMZN"
        elif stock.lower() == "facebook":
            stock = "FB"
        print(stock)

        info += stock + ", "

    label_3 = Label(canvas, text="You have selected " + info + " stocks", width=20, font=("bold", 10))
    label_3.place(relheight=0.1, relwidth=0.8, relx=0.13, rely=0.3)

    label_4 = Label(canvas, text="You want to invest " + investment_entry.get() + " rupees", width=20,
                    font=("bold", 10))
    label_4.place(relheight=0.1, relwidth=0.8, relx=0.13, rely=0.5)


label_0 = Label(canvas, text="Smart Portfolio Management System", width=20, font=("bold", 20))
label_0.place(relheight=0.1, relwidth=0.8, relx=0.1, rely=0.1)

stock_label = Label(canvas, text="Enter the company name(s)", width=20, font=("bold", 10))
stock_label.place(relheight=0.1, relwidth=0.8, relx=0.01, rely=0.2)

stock_entry = Entry(canvas)
stock_entry.place(relheight=0.04, relwidth=0.2, relx=0.52, rely=0.23)

######################################################################################

cal_label = Label(canvas, text="PLease select the inception date", width=20, font=("bold", 10))
cal_label.place(relheight=0.1, relwidth=0.8, relx=0.0001, rely=0.55)

from tkcalendar import Calendar, DateEntry
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
datestring = ''
def enterdate():
    def print_sel():
        datestring=cal.selection_get()
        print(datestring)
        cal.see(datetime.date(year=2016, month=2, day=5))

    top = tk.Toplevel(root)

    import datetime
    today = datetime.date.today()

    mindate = datetime.date(year=2018, month=1, day=21)
    maxdate = today + datetime.timedelta(days=5)
    #print(mindate, maxdate)

    cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                   mindate=mindate, maxdate=maxdate, disabledforeground='red',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

calbutton = tk.Button(canvas, text="Calendar", fg="white", bg="#263d42", padx=10, pady=5, command=enterdate)
calbutton.place(relx=0.58, rely=0.57)

cal2_label = Label(canvas, text="PLease select the end date", width=20, font=("bold", 10))
cal2_label.place(relheight=0.1, relwidth=0.8, relx=0.0001, rely=0.64)

calbutton2 = tk.Button(canvas, text="Calendar", fg="white", bg="#263d42", padx=10, pady=5, command=enterdate)
calbutton2.place(relx=0.58, rely=0.66)

########################################################################################

investment_label = Label(canvas, text="Enter the amount to invest", width=20, font=("bold", 10))
investment_label.place(relheight=0.1, relwidth=0.8, relx=0.01, rely=0.4)

investment_entry = Entry(canvas)
investment_entry.place(relheight=0.04, relwidth=0.2, relx=0.52, rely=0.43)

#

predict_btn = tk.Button(root, text="Get Result", fg="white", bg="#263d42", padx=10, pady=5, command=retreive)
predict_btn.place(relx=0.48, rely=0.9)

root.mainloop()
