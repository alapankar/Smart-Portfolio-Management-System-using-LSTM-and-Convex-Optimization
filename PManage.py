import tkinter as tk
from tkinter import *
import os


root=tk.Tk()

root.title("Smart Portfolio Management System")


canvas=tk.Canvas(root, height=600, width=900)
canvas.pack()

def retreive():
    stocks=[]
    info=""
    stocks=stock_entry.get().split(',')
    for stock in stocks:
        stock=stock.strip()
        if stock.lower()=="google":
            stock="GOOG"
        elif stock.lower()=="amazon":
            stock="AMZN"
        elif stock.lower()=="facebook":
            stock="FB"
        print(stock)
        
        info+=stock+", "
        
    label_3=Label(canvas, text="You have selected "+info+" stocks", width=20, font=("bold",10))
    label_3.place(relheight=0.1, relwidth=0.8, relx=0.13, rely=0.3)

    label_4=Label(canvas, text="You want to invest "+investment_entry.get()+" rupees", width=20, font=("bold",10))
    label_4.place(relheight=0.1, relwidth=0.8, relx=0.13, rely=0.5)
    

label_0=Label(canvas, text="Smart Portfolio Management System", width=20, font=("bold",20))
label_0.place(relheight=0.1, relwidth=0.8, relx=0.1, rely=0.1)


stock_label=Label(canvas, text="Enter the company name(s)", width=20, font=("bold",10))
stock_label.place(relheight=0.1, relwidth=0.8, relx=0.01, rely=0.2)

stock_entry=Entry(canvas)
stock_entry.place(relheight=0.04, relwidth=0.2, relx=0.52, rely=0.23)
#
investment_label=Label(canvas, text="Enter the amount to invest", width=20, font=("bold",10))
investment_label.place(relheight=0.1, relwidth=0.8, relx=0.01, rely=0.4)

investment_entry=Entry(canvas)
investment_entry.place(relheight=0.04, relwidth=0.2, relx=0.52, rely=0.43)

#
confirm_btn=tk.Button(root, text="Confirm" , fg="white", bg="#263d42", padx=10, pady=5, command=retreive)
confirm_btn.place(relx=0.485, rely=0.83)

predict_btn=tk.Button(root, text="Get Result" , fg="white", bg="#263d42", padx=10, pady=5)
predict_btn.place(relx=0.48, rely=0.9)

root.mainloop()

