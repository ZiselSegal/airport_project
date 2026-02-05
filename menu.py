import funcs as fun

#handles user UI and input logic recieves nothing and returns None
def menu():
    print('1.manager\n'
          '2.customer\n'
          '3.exit')
    action = input('Please enter an action number: ')
    match action:
        case '1':
            validation = fun.login_management(user='a',password=None,retorn_of_credentials=[])
            while validation == False:
                name = input('Please enter user name: ')
                password = input('Please enter password: ')
                credentials = fun.load_credentials()
                validation = fun.login_management(name,password,credentials)
                if validation == False:
                    print('invalid login')
            print("1. Add a new line\n"
                  "2. ")
            check = input('Please enter an action number: ')
            match check:
                case '1':
                    asking = False
                    while asking == False:
                        point_of_departure = input(str("please enter a point of departure:   ")).upper()
                        destination_point = input(str("please enter destination point:  ")).upper()
                        read_func = fun.check_flightlines_status(point_of_departure, destination_point)
                        if read_func == False:
                            new_line_question = "Do you want to choose a new line? (y/n)"
                            yes_or_no = answer_yes_or_no(new_line_question)
                            if yes_or_no == True:
                                continue
                            elif yes_or_no == False:
                                return 
                        elif read_func == True:
                            level_2 = fun.price_calculation(point_of_departure, destination_point)
                            level_3 = fun.manager_transaction(level_2,point_of_departure,destination_point)
                            if level_3 == True:
                                fun.add_flightline(point_of_departure, destination_point)
                                return
        case '2':
            print('1.buy ticket')
            action = input('Please enter an action number: ')
            match action:
                case '1':
                    fun.show_available_flightlines()
                    point_of_departure = input(str("please enter a point of departure:   ")).upper()
                    destination_point = input(str("please enter destination point:  ")).upper()
                    ticket_price = float(fun.Calculating_flight_prices(point_of_departure, destination_point))
                    print(f"The ticket price for a flight from - {point_of_departure} to - {destination_point} is:  {ticket_price}")
                    purchase_confirmation = "Are you interested in buying? (y/n)"
                    yes_or_no = answer_yes_or_no(purchase_confirmation)
                    if purchase_confirmation == True:
                        fun.add_to_budget(ticket_price)
                    elif purchase_confirmation == False:
                        exit()
                    
        case '3':
            exit()

