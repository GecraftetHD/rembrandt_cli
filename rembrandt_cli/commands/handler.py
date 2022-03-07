def command_func(command):
    if command == 'device':
        print("Device window")
    elif command == 'status':
        print("status command")

    elif command == 'pay':
        print("pay <walletfile> <destinationuuid> <amount> [text]")
    else:
        print("type `help` for help")
