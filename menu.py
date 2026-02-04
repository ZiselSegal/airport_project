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
            print("1. Add a new line\n"
                  "2. ")
            check = input('plz enter action number: ')
            match check:
                case '1':
                    asking = False
                    while asking == False:
                        point_of_departure = input(str("please enter a point of departure:   ")).upper()
                        destination_point = input(str("please enter destination point:  ")).upper()
                        read_func = fun.check_flightlines_status(point_of_departure, destination_point)
                        if read_func == False:
                            new_line_question = (input("Do you want to choose a new line? (y/n)"))
                            if new_line_question == "y":
                                continue
                            elif new_line_question == "n":
                                exit()
                        elif read_func == True:
                            level_2 = fun.price_calculation()
                            if level_2 == True:
                                fun.add_flightline(point_of_departure, destination_point)





        case '2':
            pass
        case '3':
            exit()





