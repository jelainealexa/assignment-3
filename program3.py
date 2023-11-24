import customtkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Label, PhotoImage, Frame
from datetime import datetime

window = customtkinter.CTk()
window.title("Berry Very Fruity Store")
window.geometry("815x425")
window.config(bg="#FDAB9F")
window.resizable(False, False)

font1 = ('Kristen ITC', 32, 'bold')
font2 = ('Poppins', 25, 'bold')
font3 = ('Poppins', 16, 'bold')
font4 = ('Courier New', 16, 'bold')

apple_price = 20
orange_price = 25
total_price = 0
qty_apple = 0
qty_orange = 0

image1 = PhotoImage(file="appleeye.png").subsample(7, 7)
image2 = PhotoImage(file="orangeyum.png").subsample(7, 7)
image3 = PhotoImage(file="thanku.png").subsample(6, 6)

apple_frame = customtkinter.CTkFrame(window, bg_color="#FDAB9F", fg_color ='#F0997D', corner_radius=10, width=212, height=233)
apple_frame.place(relx=33/815, rely=51/425)

orange_frame = customtkinter.CTkFrame(window, bg_color="#FDAB9F", fg_color ='#F0997D', corner_radius=10, width=212, height=233)
orange_frame.place(relx=261/815, rely=51/425)

menu_label = customtkinter.CTkLabel(window, text="Berry Very Fruity!", font=font1, text_color="#9E4244", bg_color="#FDAB9F")
menu_label.place(relx=120/815, rely=5/425)

receipt_frame = customtkinter.CTkFrame(window, bg_color='#FDAB9F', fg_color="#D3756B", width=300, height=399)
receipt_frame.place(relx=487/815, rely=13/425)

receipt_frame_text = customtkinter.CTkLabel(receipt_frame, text="Your current order will \n appear here.", font=("Poppins", 12, 'bold'), text_color="#875052", bg_color="#D3756B")
receipt_frame_text.place(relx=240/815, rely=185/425)

order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def increase_quantity(item):
    global qty_apple, qty_orange
    if item == "apple":
        qty_apple += 1
    elif item == "orange":
        qty_orange += 1
    update_labels()

def decrease_quantity(item):
    global qty_apple, qty_orange
    if item == "apple" and qty_apple > 0:
        qty_apple -= 1
    elif item == "orange" and qty_orange > 0:
        qty_orange -= 1
    update_labels()

def update_labels():
    qty_apple_label.config(text=f"Quantity: {qty_apple}")
    qty_orange_label.config(text=f"Quantity: {qty_orange}")
    

def pay():
    global total_price
    total_price = qty_apple * apple_price + qty_orange * orange_price

    if total_price == 0:
        messagebox.showwarning(title="Error", message="Please select at least one.")
    else:
        for widget in receipt_frame.winfo_children():
            widget.destroy()
        create_receipt()

def create_receipt():
    store_label = customtkinter.CTkLabel(receipt_frame, text="Berry Very Fruity!", font=("Kristen ITC", 20, 'bold'), text_color="#7c3739", bg_color="#D3756B")
    store_label.place(relx=185 / 815, rely=20 / 425)
    
    separator_line = Frame(receipt_frame, height=2, width=300, bg="#7c3739").place(relx=90 / 815, rely=55 / 425)
    
    bill_label = customtkinter.CTkLabel(receipt_frame, text="RECEIPT", font=("Courier New", 25, 'bold'), text_color="#7c3739", bg_color="#D3756B")
    bill_label.place(relx=250 / 815, rely=70 / 425)
    
    separator_line = Frame(receipt_frame, height=2, width=300, bg="#7c3739").place(relx=90 / 815, rely=110 / 425)
    
    bill_label = customtkinter.CTkLabel(receipt_frame, text=f'Date: {order_date}', font=font4, text_color="#7c3739", bg_color="#D3756B")
    bill_label.place(relx=80 / 815, rely=118 / 425)
    
    product_header_label = customtkinter.CTkLabel(receipt_frame, text="PRODUCT", font=font4, text_color="#7c3739", bg_color="#D3756B")
    product_header_label.place(relx=78 / 815, rely=155 / 425)
    
    qty_header_label = customtkinter.CTkLabel(receipt_frame, text="QTY", font=font4, text_color="#7c3739", bg_color="#D3756B")
    qty_header_label.place(relx=375 / 815, rely=155 / 425)
    
    price_header_label = customtkinter.CTkLabel(receipt_frame, text="PRICE", font=font4, text_color="#7c3739", bg_color="#D3756B")
    price_header_label.place(relx=580 / 815, rely=155 / 425)

    if qty_apple > 0:
        product_label = customtkinter.CTkLabel(receipt_frame, text="Apples", font=font4, text_color="#7c3739", bg_color="#D3756B")
        product_label.place(relx=36 / 300, rely=180 / 399)

        qty_label = customtkinter.CTkLabel(receipt_frame, text=f"{qty_apple}", font=font4, text_color="#7c3739", bg_color="#D3756B")
        qty_label.place(relx=148 / 300, rely=180 / 399)

        price_label = customtkinter.CTkLabel(receipt_frame, text=f"₱{qty_apple * apple_price}", font=font4, text_color="#7c3739", bg_color="#D3756B")
        price_label.place(relx=220 / 300, rely=180 / 399)

    if qty_orange > 0:
        product_label = customtkinter.CTkLabel(receipt_frame, text="Oranges", font=font4, text_color="#7c3739", bg_color="#D3756B")
        product_label.place(relx=32 / 300, rely=205 / 399)

        qty_label = customtkinter.CTkLabel(receipt_frame, text=f"{qty_orange}", font=font4, text_color="#7c3739", bg_color="#D3756B")
        qty_label.place(relx=148 / 300, rely=205 / 399)

        price_label = customtkinter.CTkLabel(receipt_frame, text=f"₱{qty_orange * orange_price}", font=font4, text_color="#7c3739", bg_color="#D3756B")
        price_label.place(relx=220 / 300, rely=205 / 399)


    separator_line = Frame(receipt_frame, height=2, width=300, bg="#7c3739")
    separator_line.place(relx=30 / 300, rely=240 / 399)
    
    bill_label = customtkinter.CTkLabel(receipt_frame, text=f'TOTAL: ₱{total_price}', font=("Courier New", 22, 'bold'), text_color="#7c3739", bg_color="#D3756B")
    bill_label.place(relx=120 / 300, rely=255 / 399)

    confirm_button = customtkinter.CTkButton(receipt_frame, command=confirm_purchase, text="Confirm Purchase", font=font3, fg_color="#c04243", hover_color="#9c3537", bg_color="#D3756B", corner_radius=20, cursor="hand2")
    confirm_button.place(relx=60 / 300, rely=335 / 399)

def confirm_purchase():
    for widget in receipt_frame.winfo_children():
        widget.destroy()

    loading_label = customtkinter.CTkLabel(receipt_frame, text="Processing your purchase...", font=("Poppins", 14, 'bold'), text_color="#9E4244", bg_color="#D3756B")
    loading_label.place(relx=50 / 300, rely=200 / 399)

    window.after(2000, process_confirmation, loading_label)

def process_confirmation(loading_label):
    image3_label = Label(receipt_frame, image=image3, bg="#D3756B")
    image3_label.place(relx=70 / 300, rely=120 / 399)

    thankyou1_label = customtkinter.CTkLabel(receipt_frame, text="Your order is confirmed!", font=("Poppins", 21, 'bold'), text_color="#9E4244", bg_color="#D3756B")
    thankyou1_label.place(relx=21 / 300, rely=230 / 399)

    thankyou2_label = customtkinter.CTkLabel(receipt_frame, text=" Thank you and enjoy your berry \n delicious fruits!", font=("Poppins", 13, 'bold'), text_color="#9E4244", bg_color="#D3756B")
    thankyou2_label.place(relx=40 / 300, rely=270 / 399)

    loading_label.destroy()

placeorder_button = customtkinter.CTkButton(window, command=pay, text="Place Order", font=font3, fg_color="#FC4C4E", hover_color="#d0494b", bg_color="#FDAB9F", corner_radius=20, cursor="hand2")
placeorder_button.place(relx=185 / 815, rely=350 / 425)

img1_label = Label(window, image=image1, text="Apples\n Price: ₱20", font=font3, fg="#9E4244", bg="#F0997D", compound="top", anchor="n", width=250, height=270)
img1_label.place(relx=35 / 815, rely=57 / 425)

img2_label = Label(window, image=image2, text="Oranges\n Price: ₱25", font=font3, fg="#9E4244", bg="#F0997D", compound="top", anchor="n", width=250, height=270)
img2_label.place(relx=265 / 815, rely=57 / 425)

qty_apple_label = Label(window, text=f"Quantity: {qty_apple}", font=("Poppins", 14, 'bold'), fg="#9E4244", bg="#FDAB9F")
qty_apple_label.place(relx=93 / 815, rely=300 / 425)

qty_orange_label = Label(window, text=f"Quantity: {qty_orange}", font=("Poppins", 14, 'bold'), fg="#9E4244", bg="#FDAB9F")
qty_orange_label.place(relx=317 / 815, rely=300 / 425)

decrease_button1 = customtkinter.CTkButton(window, command=lambda: decrease_quantity("apple"), text="-", font=font3,
                                           fg_color="#9E4244", bg_color="#FDAB9F", hover_color="#713334", cursor="hand2", corner_radius=10, width=40, height=16)
decrease_button1.place(relx=40 / 815, rely=297 / 425)

increase_button1 = customtkinter.CTkButton(window, command=lambda: increase_quantity("apple"), text="+", font=font3,
                                           fg_color="#9E4244", bg_color="#FDAB9F", hover_color="#713334", cursor="hand2", corner_radius=10, width=40, height=10)
increase_button1.place(relx=200 / 815, rely=297 / 425)

decrease_button2 = customtkinter.CTkButton(window, command=lambda: decrease_quantity("orange"), text="-", font=font3,
                                           fg_color="#9E4244", bg_color="#FDAB9F", hover_color="#713334", cursor="hand2", corner_radius=10, width=40, height=16)
decrease_button2.place(relx=265 / 815, rely=297 / 425)

increase_button2 = customtkinter.CTkButton(window, command=lambda: increase_quantity("orange"), text="+", font=font3,
                                           fg_color="#9E4244", bg_color="#FDAB9F", hover_color="#713334", cursor="hand2", corner_radius=10, width=40, height=16)
increase_button2.place(relx=425 / 815, rely=297 / 425)

footer_label = customtkinter.CTkLabel(window, text="© 2023 Berry Very Fruity Store. All rights reserved.", font=("Poppins", 10), text_color="#9E4244", bg_color="#FDAB9F")
footer_label.place(relx=140 / 815, rely=397 / 425)

window.mainloop()