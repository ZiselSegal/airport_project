import csv
import os
import json
import random
import string

# recieves nothing returns contents of budget.txt file as string
def load_budget():
    with open('budget.txt','r') as f:
        reader = f.read()
        return(float(reader))

# פונקציה כניסה של מנהל
def login_management(user, password, retorn_of_credentials):
    for one_item in retorn_of_credentials:
        if one_item[0] == user and one_item[1] == password:
            return True
    return False

# recieves nothing returns matrix of file contents where each row is a list inside the matrix
def load_credentials():
    with open('credentials.csv','r') as f:
        reader = csv.reader(f)
        return list(reader)[1::]

#checks if all files needed for project are present and close the program if not return true or false
def File_existence_check():
    files_to_check = ['airport_entry_fee.csv','available_flights.json','budget.txt','continents_pricing.csv','credentials.csv','funcs.py','main.py','menu.py','tickets.csv']
    for file in files_to_check:
        if not os.path.exists(file):
            print('Error, missing files')
            return False,exit()
    return True

# A function that returns all airport details with prices
def load_airport_bank():
    with open('airport_entry_fee.csv','r') as f:
        reader = csv.reader(f)
        return list(reader)[1::]

#recieves nothing return available flights file contents as a list of dicts
def load_available_flights():
    with open('available_flights.json','r') as f:
        reader = json.load(f)
        return (reader["available_lines"])

#recives 2 airport codes checks if they are available or owned return false if not avilable or owned else returns true
def check_flightlines_status(departure_ap,destination_ap):
    airports = load_airport_bank()
    owned_lines = load_available_flights()
    counter = 0
    for line in owned_lines:
        if line["origin_airport"] == departure_ap and line["destination airport"] == destination_ap:
            print('line already owned')
            return False
    for airport in airports:
        if airport[0] == departure_ap or airport[0] == destination_ap:
            counter += 1
    if counter != 2:
        print('lines do not exist plz enter a valid flightline')
        return False
    return True

# recives 2 airports and writes them inside the avalable fllight filees returns nothing
def add_flightline(departure_ap,destination_ap):
    with open('available_flights.json','r+') as f:
        flightline = {"origin_airport":departure_ap,"destination airport":destination_ap}
        available_flights_lst = json.load(f)
        available_flights_lst["available_lines"].append(flightline)
        f.seek(0)
        json.dump(available_flights_lst,f)
        print(f'flightline: {departure_ap} to {destination_ap} registred sucssesfully')

#recieves 2 airports calculate price of line returns the price
def price_calculation(departure_ap,destination_ap):
    pricing_menu = load_airport_bank()
    line_price = 0
    for price in pricing_menu:
        if price[0] == departure_ap or price[0] == destination_ap:
            line_price += int(price[5])
    return line_price

#function receives line price and 2 airports and calculates it vs budget and confirm the purchase returns true or false
def manager_transaction(line_price,departure_ap,destination_ap):
    budget = load_budget()
    if budget >= line_price:
        confirmation = input(f'confirm purchase for {line_price} with budget of {budget}: y/n:')
        if confirmation == 'y':
            print(f'transaction completed new budget: {budget - line_price}')
            with open('budget.txt','w') as f:
                f.write(str(budget - line_price))
            return True
        else:
            print('transaction cancelation completed')
            return False
    print(f'insufficent balance for filghtline {departure_ap} to {destination_ap} price: {line_price} budget: {budget}')
    return False

# The function receives an amount as a parameter and adds it to the airport's bank account.
def add_to_budget(amount):
    current_amount = load_budget()
    new_amount = amount + current_amount
    with open('budget.txt','w') as f:
        f.write(f'{new_amount}')
    print('The payment was made successfully')
    
# prints all available flight orderly recievs nothing and returns nothing
def show_available_flightlines():
    flightlines = load_available_flights()
    for flightline in flightlines:
        print(f'available flight: {flightline["origin_airport"]} to {flightline["destination airport"]}')

#creates random 8 char ticket id recieves nothing and returns ID
def create_ticket_ID():
    charecters = string.printable
    ID = ''
    for num in range(8):
        ID += random.choice(charecters)
    return ID

#function recieves
def save_ticket_info(ID,price,origin_point,destination):
    ticket_info = [ID,str(price),origin_point,destination]
    with open('tickets.csv','a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(ticket_info)
        print('ticket info saved')
