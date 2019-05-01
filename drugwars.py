from tkinter import *
import random
import os
import time


class Drugs:

    def __init__(self, name, price_range, amount):
        self.name = name
        self.price_range = price_range
        self.amount = amount
        self.price_check()

    def price_check(self):
        # the * is to unpack the touple of values that the random goes between
        self.price = random.randint(*self.price_range)
        # print("the price of " + self.name + " is " + str(self.price))
        return self.price


class Events:

    def __init__(self, name, text, price_range):
        self.name = name
        self.price_range = price_range
        self.text = text
        self.price_mod()

    def price_mod(self):
        self.price = random.randint(*self.price_range)
        return self.price


my_drugs = [
    Drugs("Cocaine", (15000, 28000), 0),
    Drugs("Heroin", (2000, 10000), 0),
    Drugs("Weed", (300, 1000), 0),
    Drugs("Hash", (200, 1200), 0),
    Drugs("Opium", (400, 1800), 0),
    Drugs("Acid", (1000, 4200), 0),
    Drugs("Ludes", (18, 75), 0),

]

event_list = [
    Events("Cocaine", 'El Chapo Arrested! Coke price thru the roof!', (40000, 110000)),
    Events("Heroin", 'Trump cracks down on opiates! Heroin in high demand by addicts', (9000, 25000)),
    Events("Weed", 'The Mexicans have flooded the market with cheap grass! Weed prices bottom out', (50, 400)),
    Events("Hash", 'Ricky\'s hash driveway burned down! Jesus Murphy look at the price boys!', (800, 2000)),
    Events("Opium", 'Shenzhen 深圳 Opium 鸦片 Den 塔 was raided! Street price is popping off!', (1800, 6000))
]


def generatelocations():
    locs = {'Canada': ('Red Deer', 'Edmonton', 'Calgary', 'Toronto', 'Vancouver', 'St. Johns'),
            'USA': ('L.A.', 'NYC', 'Chicago', 'Miami', 'Houston', 'Phoenix')}
    country = list(locs.keys())
    country = country[random.randint(0, len(country)-1)]
    location = []
    for i in range(len(locs[country])):
        location.append(locs[country][i])
    return location


def generate_event():
    event_choice = random.randint(0, len(event_list)-1)
    if random.randint(0, 100) > 35:
        return event_choice
    else:
        return -1


def officer():
    global cash
    cash_taken = random.randint(1, cash-1)
    cash -= cash_taken
    return cash_taken


def price_change(event_number):
    price_list = []
    # again, fuck range() and its stupid handling of endpoints
    for i in range(0, len(my_drugs)):
        j = my_drugs[i]
        k = j.price_check()
        price_list.append(k)
    if event_number != -1:
        price_list[event_number] = event_list[event_number].price_mod()
        return price_list
    return price_list


def validate_numeric(value_string, numeric_type=int):
    """Validate a string as being a numeric_type"""
    try:
        if numeric_type(value_string) > 0:
            return numeric_type(value_string)
        else:
            raise ValueError
    except ValueError:
        raise


def validate_alpha(value_string):
    """Validate a string as being a single alpha type"""
    try:
        if value_string.isalpha() and len(value_string) == 1:
            return value_string
    except ValueError:
        raise


def check_inv():
    k = 0
    for i in range(0, len(my_drugs)-1):
        k += my_drugs[i].amount
        return k


def buy_func(price_list):
    global cash
    global inventory
    menu_iteration = 0
    while True:
        if menu_iteration < 1:
            drug_choice = input("Which drug?:\n")
            menu_iteration += 1
        else:
            drug_choice = input("Buy anything Else? (press / to go back)\n")
        try:
            if drug_choice == '/':
                break
            drug_choice = validate_numeric(drug_choice, int)
            if drug_choice in range(1, len(my_drugs) + 1):
                drug_choice = drug_choice - 1
                print(my_drugs[drug_choice].name + ": you have " + str(my_drugs[drug_choice].amount))
                print("The going price is: $" + str(price_list[drug_choice]))
                # need to restructure this
                while True:
                    buy_amount = input('How much you want to buy? (m for max)\n')
                    if buy_amount == 'm':
                        buy_amount = cash // price_list[drug_choice]
                        if buy_amount > 100 - inventory:
                            buy_amount = 100 - inventory

                    if buy_amount == '/':
                        break
                    try:
                        buy_amount = validate_numeric(buy_amount, int)
                        if buy_amount > 100 - inventory:
                            print("You don\'t have enough space for all that.")
                            continue
                        if buy_amount * price_list[drug_choice] <= cash:
                            my_drugs[drug_choice].amount += buy_amount
                            cash -= buy_amount * price_list[drug_choice]
                            inventory += buy_amount
                            print("Cash: $" + str(cash))
                            print("You bought " + str(buy_amount) + " " + my_drugs[drug_choice].name)
                            break
                        else:
                            print("You don\'t have enough cash!")
                            raise ValueError
                    except ValueError:
                        continue
        except ValueError:
            continue


def sell_func(price_list):
    global cash
    global inventory
    menu_iteration = 0
    while True:
        if menu_iteration < 1:
            drug_choice = input("Which drug?:\n")

            menu_iteration += 1
        # can nuke this and menu_iteration if I dont want another option in the future
        else:
            drug_choice = input("Sell anything Else? (press / to go back)\n")
        try:
            if drug_choice == '/':
                break
            drug_choice = validate_numeric(drug_choice, int)
            if drug_choice in range(1, len(my_drugs) + 1) and my_drugs[drug_choice-1].amount > 0:
                drug_choice = drug_choice - 1
                print(my_drugs[drug_choice].name + ": you have " + str(my_drugs[drug_choice].amount))
                print("The going price is: $" + str(price_list[drug_choice]))
                # need to restructure this
                while True:
                    sell_amount = input('How much you want? (m for max)\n')
                    if sell_amount == 'm':
                        sell_amount = my_drugs[drug_choice].amount
                    if sell_amount == '/':
                        break
                    try:
                        sell_amount = validate_numeric(sell_amount, int)
                        if sell_amount <= my_drugs[drug_choice].amount:
                            my_drugs[drug_choice].amount -= sell_amount
                            cash += sell_amount * price_list[drug_choice]
                            inventory -= sell_amount
                            print("Cash: $" + str(cash))
                            print("You sold " + str(sell_amount) + " " + my_drugs[drug_choice].name + ' for $' + str(
                                sell_amount * price_list[drug_choice]))
                            break
                        else:
                            print("You don\'t have that much")
                            raise ValueError
                    except ValueError:
                        continue
            else:
                print('You don\'t have any')
                continue
        except ValueError:
            continue


def location_change():
    print("Locations:")
    for i in range(len(loc)):
        print(str(i + 1) + '. ' + loc[i])
    while True:
        loc_choice = input('Where do you want to go?:\n')
        try:
            # set this as 1-6 for an index of 0-5, then set from 1-7 because range isnt inclusive on the last number
            # could be fed locs variable for better autism, but manual based on # of locs is ok for now
            if int(loc_choice) in range(1, 7):
                return loc_choice
            # this should filter out all bad responses
        except ValueError:
            continue


def print_list(day_play, total_day, loc_choice, event_number, price_list, cash_stolen):
    os.system('cls' if os.name == 'nt' else 'clear')
    if event_number != -1:
        print("=" * 36 + "N E W S" + "=" * 37)
        print(event_list[event_number].text)
        print("=" * 79)
    if event_number == -1 and cash_stolen != 0:
        print("=" * 36 + "N E W S" + "=" * 37)
        print("Officer Leroy stopped you and took $" + str(cash_stolen) + " from you.")
        print("=" * 79)
    print("Location: " + loc[int(loc_choice) - 1])
    print("Day: " + str(day_play) + '/' + str(total_day))
    print("Cash: $" + str(cash))
    print("Inventory: " + str(inventory) + "/100")
    print("No. Inv:     Drug:    Price:")
    print("----------------------------")
    for i, drug in enumerate(my_drugs, 1):
        print(str(i) + ". " + " (" + str(drug.amount) + ") " + ' '.rjust(6-len(str(drug.amount))) + drug.name + ' '.rjust(8-len(str(drug.name))) + " $" + str(price_list[i-1]))


def gameloop(day_play, total_day):
    global cash
    loc_choice = location_change()
    event_number = generate_event()
    cash_stolen = 0
    if event_number == -1 and random.randint(0, 100) > 80:
        cash_stolen = officer()
    price_list = price_change(event_number)
    check_inv()
    print_list(day_play, total_day, loc_choice, event_number, price_list, cash_stolen)
    while True:
        menu_choice = input("Press b to buy, s to sell, or m to move.\n")
        try:
            menu_choice = validate_alpha(menu_choice)
            if menu_choice == 'b':
                buy_func(price_list)
                continue
            if menu_choice == 's':
                sell_func(price_list)
                continue
            if menu_choice == 'm':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
        # this should filter out all bad responses
        except ValueError:
            continue


# Pregame setup
loc = generatelocations()
global cash
global inventory
inventory = 0
starting_cash = 2000
cash = starting_cash
# filters player's input for the game duration
while True:
    day = input("How many days do you want to play?\n")
    try:
        day = validate_numeric(day, int)
        break
    except ValueError:
        continue
# Calls gameloop the number of times inputted by the player
for game_day in range(1, day+1):
    gameloop(game_day, day)
# ending printout of ending cash
print("You finished with $" + str(cash))
if cash > starting_cash:
    print('You made money! Up ' + str((cash/starting_cash).__round__()) + 'x! Well done.')
if cash == starting_cash:
    print('You broke even... hope you at least had fun')
if cash < starting_cash:
    print("You lost money, better go get a real job.")
time.sleep(8)
