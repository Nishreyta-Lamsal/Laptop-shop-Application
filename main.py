import messages
import write
import BuySell

# This is the main file 
messages.welcome()
loop = True

while loop:
    messages.select_option()

    select_option = False
    while not select_option:
        try:
            select = int(input("Enter an option: "))
            select_option = True
        except:
            messages.invalid()
            messages.select_option()
    if select == 1:
        BuySell.purchase()
    elif select == 2:
        BuySell.sell()
    elif select == 3:
        messages.thanks()
        loop = False
    else:
        messages.invalid()
