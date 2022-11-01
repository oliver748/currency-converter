from tkinter import *
import customtkinter
from utilities.fetch_prices import fetch

app = customtkinter.CTk()
app.geometry("480x210")
app.resizable(FALSE, FALSE)
app.title("Currency Converter")
CURRENCIES = [
    "USD",
    "EUR",
    "GBP",
    "INR",
    "AUD",
    "CAD",
    "SGD",
    "CHF",
    "MYR",
    "JPY",
    "CNY",
    "DKK",
]

def convert():
    # fetches the values picked in the option menus
    amount = entry_1.get()
    option_1 = optionmenu_1.get()
    option_2 = optionmenu_2.get()
    fetch_rates = fetch()

    def matcher(option):
        # sips through all currencies to find the match
        for currency in fetch_rates:
            name = currency.split(":")[0]
            if option == name:
                rate = currency.split(":")[1]
                return rate
        return 1  # returns 1 as no match means it's USD

    currency_1 = matcher(option_1)
    currency_2 = matcher(option_2)

    # calculates conversion
    output_amount = float(amount) * float(currency_2) / float(currency_1)
    output_amount = round(output_amount, 2)

    e2.set(f"{output_amount:,}")  # :, means it does 1000 -> 1,000

def switch():
    option_1 = optionmenu_1.get()
    option_2 = optionmenu_2.get()
    optionmenu_1.set(option_2)
    optionmenu_2.set(option_1)
    convert()

frame = customtkinter.CTkFrame(app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(frame, text="→")
label_1.pack()
label_1.place(x=110, y=35)

e1 = StringVar()
entry_1 = customtkinter.CTkEntry(frame, textvariable=e1, width=125)
entry_1.pack()
entry_1.place(x=35, y=35)

e2 = StringVar()
entry_2 = customtkinter.CTkEntry(frame, textvariable=e2, width=125)
entry_2.pack()
entry_2.place(x=200, y=35)

optionmenu_1 = customtkinter.CTkOptionMenu(frame, values=CURRENCIES)
optionmenu_1.pack()
optionmenu_1.place(x=35, y=70)
optionmenu_1.set(CURRENCIES[0])

optionmenu_2 = customtkinter.CTkOptionMenu(frame, values=CURRENCIES)
optionmenu_2.pack()
optionmenu_2.place(x=185, y=70)
optionmenu_2.set(CURRENCIES[1])

button_1 = customtkinter.CTkButton(frame, text="Convert", command=lambda: convert())
button_1.pack()
button_1.place(x=35, y=105)

button_2 = customtkinter.CTkButton(frame, text="Switch", command=lambda: switch())
button_2.pack()
button_2.place(x=185, y=105)

if __name__ == "__main__":
    app.mainloop()
