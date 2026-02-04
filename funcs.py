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

