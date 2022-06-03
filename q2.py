def creditcard(cno):
    if len(cno)>16 or len(cno)<16 :
        print("Invalid card number")
    else:
        print(cno[12:])

cardnumber=input("enter the card number: ")
creditcard(cardnumber)
