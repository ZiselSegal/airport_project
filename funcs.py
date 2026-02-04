# recieves nothing returns contents of budget.txt file as string
def load_budget():
    with open('budget.txt','r') as f:
        reader = f.read()
        return(reader)

