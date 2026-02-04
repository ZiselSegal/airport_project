import csv
import os

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

