import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
import re
import pyperclip  # Use pip install pyperclip in the terminal
import customtkinter  # Use pip install customtkinter
import threading

amazon = []
links = []
link2 = []
wanted_price = []
prices = []

request_params = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive"
        }


# ---------------------------- Check if link is proper ------------------------------- #
def check_link(link1, expected_price):

    temp = re.split(".in|.ae", link1)[0]

    if temp == "www.amazon" or temp == "https://www.amazon":
        err = not_exists(link1)  # Checks if the product in the link does not exist

        if not err:
            messagebox.showwarning(title="Oops", message="Product does not exist!")
            return False

        with open("links.txt", "r") as file:  # Checks if the link is already present in file.
            urls = file.readlines()

        for url in urls:
            if link1+"\n" == url:
                messagebox.showwarning(title="Oops", message="This link already exists!")
                return False

        return check_price(expected_price)  # Will return the output of that function

    else:
        messagebox.showwarning(title="Oops", message="Please enter a valid amazon link!")
        return False


# ---------------------------- Check if product exists or not ------------------------------- #
def not_exists(link3):
    global request_params

    response = requests.get(url=link3, headers=request_params)
    soup = BeautifulSoup(response.text, "lxml")  # Please install lxml in the terminal using 'pip install lxml'

    try:
        soup.find(class_="h1").get_text()  # Searches for a specific text on 404 page,
        # returns true if text not found (product exists) and false if not found (doesn't exist)
    except AttributeError:
        print("")
    else:
        return False

    try:
        product = soup.find(id="productTitle").getText()
        price = soup.find(class_="a-offscreen").get_text()
    except AttributeError:
        return False
    else:
        return True


# ---------------------------- Check if price is proper ------------------------------- #
def check_price(expected_price):
    try:
        with open("price.txt", "a") as file:
            file.write(f"{int(expected_price)}\n")  # Checks if the entered value is integer or not
        return True
    except ValueError:
        messagebox.showwarning(title="Oops", message="Please enter integer value.")
        return False


# ---------------------------- Add links and price ------------------------------- #
def start_add_link():
    threading.Thread(target=add_link).start()


def add_link():

    link1 = link_entry.get()
    expected_price = expec_entry.get()
    con = check_link(link1, expected_price)  # Checks both price and link

    if con:
        with open("links.txt", "a") as file:
            file.write(f"{link1}\n")

        messagebox.showinfo(title="Success!", message="The data has been successfully added.")

        link_entry.delete(0, END)
        expec_entry.delete(0, END)


# ---------------------------- Delete All ------------------------------- #
def delete_all():

    with open("links.txt", "r") as file:
        links1 = file.readlines()

    with open("price.txt", "r") as file:
        prices1 = file.readlines()

    if not links1 and not prices1:
        messagebox.showwarning(title="Oops", message="It is already empty!")
    else:
        answer = messagebox.askokcancel(title="Delete?", message="Are you sure you want to delete everything?")
        if answer:
            with open("links.txt", 'r+') as file:
                file.truncate(0)

            with open("price.txt", 'r+') as file:
                file.truncate(0)

            messagebox.showinfo(title="Success!", message="Deleted!")


# ---------------------------- Delete All ------------------------------- #
def delete_current(x):
    global links, wanted_price

    for link in links:
        if link == links[x]:
            links.remove(link)
        else:
            continue

    for price in wanted_price:
        if price == wanted_price[x]:
            wanted_price.remove(price)
        else:
            continue

    with open("links.txt", 'r+') as file:
        file.truncate(0)
    with open("links.txt", 'w') as file:
        for link in links:
            file.write(link)

    with open("price.txt", 'r+') as file:
        file.truncate(0)
    with open("price.txt", 'w') as file:
        for p in wanted_price:
            file.write(p)


# ---------------------------- Check for links and price ------------------------------- #
def start_check_prices():
    threading.Thread(target=check_prices).start()


def check_prices():
    global links, wanted_price

    try:
        with open("links.txt", "r") as file:
            links = file.readlines()
    except FileNotFoundError:
        with open("links.txt", "w") as file:  # Creates the text file if it doesn't exist
            print("")

    try:
        with open("price.txt", "r") as file:
            wanted_price = file.readlines()
    except FileNotFoundError:
        with open("price.txt", "w") as file:  # Creates the text file if it doesn't exist
            print("")

    if not links and not wanted_price:  # This will execute if the text files are empty
        messagebox.showwarning(title="Oops", message="Please enter a link and value first.")
    else:
        for link in links:
            amazon.append(re.sub("\n", "", link))  # To remove the '\n' from each line/data

        x = 0  # To use for prices
        y = 0  # To see if we got an item under our price

        flag = False

        for URL in amazon:

            response = requests.get(url=URL, headers=request_params)
            soup = BeautifulSoup(response.text, "lxml")  # Please install lxml in the terminal using 'pip install lxml'

            try:
                product = soup.find(id="productTitle").getText()
                price = soup.find(class_="a-offscreen").get_text()
            except AttributeError:
                messagebox.showwarning(title="Error!", message="An issue has occurred.\nPlease try again later!")
                flag = True  # If the servers are overloaded
                break

            p_name = re.split(r',', product)[0]  # To get a smaller name of products
            p_name = p_name.split("        ")[1]  # Removes random space that appears before the name of the product

            try:
                price_without_currency = price.split("AED")[1]
                currency = "AED"
            except IndexError:
                try:
                    price_without_currency = price.split("₹")[1]
                    currency = "₹"
                except IndexError:
                    messagebox.showwarning(title="Oops!", message=f"{p_name}\nIs out of stock!")
                    continue

            price_as_float = float(re.sub(",", "", price_without_currency))

            if x <= (len(wanted_price) - 1):
                if price_as_float < int(wanted_price[x]):  # Executes if any product is under our given price
                    y += 1
                    messagebox.showinfo(title="Details!", message=f'Product = {p_name} \nCurrent Price = {currency}{int(price_as_float)} '
                                                              f'\nExpected Price = {currency}{wanted_price[x]} '
                                                              f'\nLink will be copied to your clipboard!')

                    pyperclip.copy(URL)  # Copies the link to your clipboard

                    answer = messagebox.askyesno(title="Delete?", message="Do you want to delete product link?")

                    if answer:
                        delete_current(x)
                        continue
            x += 1

        if y > 0:  # If even a single product is on sale, this will execute
            messagebox.showinfo(title="Complete!", message="Process Complete!\nEnjoy Shopping")
        elif not flag:  # Otherwise this will execute
            messagebox.showinfo(title=":(", message="Process Complete!\nNo price drops yet!")


# ---------------------------- UI SETUP ------------------------------- #
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.title("Amazon Price Tracker")
app.geometry("540x390")
app.config(pady=10, padx=50)
app.iconbitmap("amaz.ico")

canvas = customtkinter.CTkCanvas(width=200, height=200, background=app["bg"], highlightthickness=0)
photo = PhotoImage(file="amaz.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0, pady=20)

web_link = customtkinter.CTkLabel(master=app, text="Link:")
web_link.grid(column=0, row=1, pady=5)

expec = customtkinter.CTkLabel(master=app, text="Expected Value:  ")
expec.grid(column=0, row=2, pady=5)

link_entry = Entry(width=40)
link_entry.grid(column=1, row=1, pady=5)

expec_entry = Entry(width=40)
expec_entry.grid(column=1, row=2, columnspan=2, pady=5)

add_btn = customtkinter.CTkButton(master=app, text="Add", fg_color="#f8981d", hover_color="#ffbf00",
                                  text_color="black", width=70, command=start_add_link)
add_btn.grid(column=3, row=1, pady=5, padx=6)

check_btn = customtkinter.CTkButton(master=app, text="Check", fg_color="#f8981d", hover_color="#ffbf00",
                                    text_color="black", width=70, command=check_prices)
check_btn.grid(column=3, row=2, pady=5, padx=7)

delete_btn = customtkinter.CTkButton(master=app, text="Delete All", fg_color="#e60000", text_color="black",
                                     hover_color="#b30000", width=90, command=delete_all)
delete_btn.grid(column=1, row=3, pady=5)

app.mainloop()
