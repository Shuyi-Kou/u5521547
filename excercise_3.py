def speeding_ticket(speed, is_birthday):
    if is_birthday is False:
        if float(speed) <= 60:
           print("no ticket")
        elif (float(speed) <= 80 and float(speed) >60):
            print("small ticket")
        else:
            print("big ticket")
    else:
        if float(speed) <= 65:
           print("no ticket")
        elif float(speed) <= 85 and float(speed) >65:
            print("small ticket")
        else:
            print("big ticket")
speeding_ticket(60, False)
speeding_ticket(75, False)
speeding_ticket(65, True)
            