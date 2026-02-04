import csv
import os
import json

# recieves nothing returns contents of budget.txt file as string
def load_budget():
    with open('budget.txt','r') as f:
        reader = f.read()
        return(int(reader))

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
    files_to_check = ['airport_entry_fee.csv','available_flights.json','budget.txt','continents_pricing.csv','credentials.csv','funcs.py','main.py','menu.py']
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

        
