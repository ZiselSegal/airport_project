import csv
# recieves nothing returns contents of budget.txt file as string
def load_budget():
    with open('budget.txt','r') as f:
        reader = f.read()
        return(int(reader))

# recieves nothing returns matrix of file contents where each row is a list inside the matrix
def load_credentials():
    with open('credentials.csv','r') as f:
        reader = csv.reader(f)
        return list(reader)[1::]

