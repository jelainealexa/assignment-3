import customtkinter
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import threading
import time

window = customtkinter.CTk()
window.title("Apple Store")
window.geometry("600x480")
window.config(bg="#FDAB9F")
window.resizable(False, False)

font1 = ('Kristen ITC', 27, 'bold')
font2 = ('Poppins', 22, 'bold')
font3 = ('Poppins', 14, 'bold')
font_footer = ('Poppins', 10)

bg_image = PhotoImage(file="bg_apples.png").subsample(2,2)
bg_label = Label(window, image=bg_image, bg="#FDAB9F")
bg_label.place(relwidth=1, relheight=1)

title_label = customtkinter.CTkLabel(window, text="Berry Very Fruity!", font=font1, text_color="#9E4244", bg_color="#FDAB9F")
title_label.pack(pady=20)

label_money = customtkinter.CTkLabel(window, text="Enter the amount you have (₱):", font=font3, text_color="#9E4244", bg_color="#FDAB9F")
label_money.pack(pady=5)

entry_money = Entry(window, font=font3, width=15, justify='center', fg='#9E4244')
entry_money.pack()

label_apple_price = customtkinter.CTkLabel(window, text="Enter the price of each apple (₱):", font=font3, text_color="#9E4244", bg_color="#FDAB9F")
label_apple_price.pack(pady=10)

entry_apple_price = Entry(window, font=font3, width=15, justify='center', fg='#9E4244')
entry_apple_price.pack()

def calculate_apples():
    try:
        money = float(entry_money.get())
        apple_price = float(entry_apple_price.get())

        if money < 0 or apple_price <= 0:
            messagebox.showwarning("Invalid Input", "Please enter valid values.")
            return

        buyapples1_label.place_forget()
        buyapples2_label.place_forget()

        loading_label = customtkinter.CTkLabel(window, text="Processing your purchase...", font=("Poppins", 14, 'bold'), text_color="#9E4244", bg_color="#FDAB9F")
        loading_label.place(relx=100 / 300, rely=280 / 399)

        window.after(2000, lambda: process_confirmation(loading_label, money, apple_price))

    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter numeric values.")

def process_confirmation(loading_label, money, apple_price):
    loading_label.destroy()
    
    max_apples = int(money // apple_price)
    change = money - (max_apples * apple_price)

    max_apples_label.configure(text=f"You get {max_apples} sweet apples!")
    change_label.configure(text=f"Change: ₱{change:.2f}")

calculate_button = customtkinter.CTkButton(window, command=calculate_apples, text="Calculate", font=font3,
                                           fg_color="#FC4C4E", hover_color="#d0494b", bg_color="#FDAB9F", corner_radius=10, cursor="hand2")
calculate_button.pack(pady=20)

max_apples_label = customtkinter.CTkLabel(window, text="", font=("Poppins", 20, 'bold'), text_color="#9E4244", bg_color="#FDAB9F")
max_apples_label.pack(pady=10)

change_label = customtkinter.CTkLabel(window, text="", font=("Poppins", 20, 'bold'), text_color="#9E4244", bg_color="#FDAB9F")
change_label.pack(pady=3)

buyapples1_label = customtkinter.CTkLabel(window, text="Fresh Red Apples", font=font2, text_color="#9E4244", bg_color="#FDAB9F")
buyapples1_label.place(relx=140 / 400, rely=270 / 400)

buyapples2_label = customtkinter.CTkLabel(window, text="A Berry Very Sweet and Healthy Choice!", font=font3, text_color="#9E4244", bg_color="#FDAB9F")
buyapples2_label.place(relx=110 / 400, rely=300 / 400)

footer_label = customtkinter.CTkLabel(window, text="© 2023 Berry Very Fruity. All rights reserved.", font=font_footer, text_color="#9E4244", bg_color="#FDAB9F")
footer_label.place(relx=130 / 400, rely=370 / 400)

window.mainloop()