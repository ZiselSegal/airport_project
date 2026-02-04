import os

def File_existence_check(file):
    files_to_check = ['airport_entry_fee.csv','available_flights.json','budget.txt','continents_pricing.csv','credentials.csv','funcs.py','main.py','menu.py']

    if file in files_to_check:
        return True
    else:
        return False
        

print(File_existence_check('budget.tt'))