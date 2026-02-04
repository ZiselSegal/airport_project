def menu():
    print('1.manager\n'
          '2.customer\n'
          '3.exit')
    action = input('plz enter action number: ')
    match action:
        case '1':
            name = input('plz enter user name: ')
            password = input('plz enter password: ')
        case '2':
            pass
        case '3':
            exit()