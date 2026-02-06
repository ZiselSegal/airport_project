import funcs as fun

#handles user UI and input logic recieves nothing and returns None
def main_menu():
    print('1.manager\n'
          '2.customer\n'
          '3.exit')
    action = input('Please enter an action number: ')
    match action:
        case '1':
            manager_menu()
        case '2':
            customer_menu()
        case '3':
            exit()
        case _:
            print('action not recognized plz enter one of the following actions')
            main_menu()

#handles manager UI recieves and returns nothing
def manager_menu():
    validation = False
    while validation == False:
        name = input('Please enter user name: ')
        password = input('Please enter password: ')
        credentials = fun.load_credentials()
        validation = fun.login_management(name,password,credentials)
        if validation == False:
            print('invalid login')
    print("1.Add a new line\n"
          "2.return to main menu\n"
          '3.exit')
    check = input('Please enter an action number: ')
    match check:
        case '1':
            asking = False
            while asking == False:
                point_of_departure = input(str("please enter a point of departure or exit:  ")).upper()
                if point_of_departure == 'EXIT':
                    exit()
                destination_point = input(str("please enter destination point or exit: ")).upper()
                if destination_point == 'EXIT':
                    exit()
                read_func = fun.check_flightlines_status(point_of_departure, destination_point)
                if read_func == False:
                    new_line_question = "Do you want to choose a new line? (y/n): "
                    yes_or_no = fun.answer_yes_or_no(new_line_question)
                    if yes_or_no == False:
                        return
                elif read_func == True:
                    level_2 = fun.price_calculation(point_of_departure, destination_point)
                    level_3 = fun.manager_transaction(level_2,point_of_departure,destination_point)
                    if level_3 == True:
                        fun.add_flightline(point_of_departure, destination_point)
                        return
        case '2':
            main_menu()
        case '3':
            exit()
        case _:
            print('action not recognized plz enter one of the following actions')
            main_menu()

# handler customer UI returns na drecieves nothing
def customer_menu():
    print('1.buy ticket\n'
          '2.return to main menu\n'
          '3.exit')
    action = input('Please enter an action number: ')
    match action:
        case '1':
            while True:
                fun.show_available_flightlines()
                point_of_departure = input(str("please enter a point of departure or exit:  ")).upper()
                if point_of_departure == 'EXIT':
                    exit()
                destination_point = input(str("please enter destination point or exit: ")).upper()
                if destination_point == 'EXIT':
                    exit()
                status = fun.check_purchase_status(point_of_departure,destination_point)
                if status == True:
                    ticket_price = float(fun.Calculating_flight_prices(point_of_departure, destination_point))
                    print(f"The ticket price for a flight from - {point_of_departure} to - {destination_point} is:  {ticket_price}")
                    purchase_confirmation = "Are you interested in buying? (y/n)"
                    yes_or_no = fun.answer_yes_or_no(purchase_confirmation)
                    if yes_or_no == True:
                        fun.add_to_budget(ticket_price)
                        ID = fun.create_ticket_ID()
                        fun.save_ticket_info(ID,ticket_price,point_of_departure,destination_point)
                        customer_menu()
                    elif yes_or_no == False:
                        print('purchase cancelled')
                        customer_menu()
        case '2':
            main_menu()      
        case '3':
            exit()
        case _:
            print('action not recognized plz enter one of the following actions')
            main_menu()
main_menu()