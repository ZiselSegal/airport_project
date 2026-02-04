import funcs as fun

#handles user UI and input logic recieves nothing and returns None
def menu():
    print('1.manager\n'
          '2.customer\n'
          '3.exit')
    action = input('plz enter action number: ')
    match action:
        case '1':
            validation = fun.login_management(user='a',password=None,retorn_of_credentials=[])
            while validation == False:
                name = input('plz enter user name: ')
                password = input('plz enter password: ')
                credentials = fun.load_credentials()
                validation = fun.login_management(name,password,credentials)
                if validation == False:
                    print('invalid login')
        case '2':
            pass
        case '3':
            exit()
menu()