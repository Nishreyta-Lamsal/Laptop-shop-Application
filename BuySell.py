import messages
import write

def purchase():
    """ The main function to purchase laptops is added here. A 2D list is created and the user is asked if s/he wants to return more laptops.A function to print and write the invoice is called.
    """
    print("\n Purchase a laptop here. \n")

    file_contents = write.read_file()
    mainData = write.dictionary(file_contents)

    placeholder = []
    write.print_laptop(file_contents, mainData)  # list of laptop is printed
    continueLoop = True
    while continueLoop:  # outerloop
        
        Id = valid_id_purchase(mainData)
        messages.available()
        qn = int(valid_quantity_purchase(mainData, Id))
        mainData[Id][3] = int(mainData[Id][3]) - qn
        placeholder.append([Id, qn])

        write.write_file(mainData)
        write.print_laptop(file_contents, mainData)

        more = True
        while more:  #inner loop
            userInput = input("Do you want to buy or sell more laptop?(yes/no): ")
            
            if userInput.lower() == "no":
                continueLoop = False  # outerloop is terminated, bill details will be asked
                more = False  # inner loop is terminated

            elif userInput.lower() == "yes":
                continueLoop = True  # outerloop continues, more costumes will be purchaseed
                more = False  # inner loop is terminated

            else:
                messages.invalid()
                more = True  # inner loop continues

    print()
    write.purchase_bill(placeholder)  # function to print and write the bill
    messages.purchase()

def valid_id_purchase(mainData):
    """
        Valid or invalid ID entered is checked by this function.If the ID is not valid, an invalid message is shown.It takes the dictionary as a parameter, and returns the valid ID.
    """
    Valid_input = False
    while Valid_input == False:
        try:
            ID = int(input("Enter the ID of the laptop you want to purchase: "))
            if ID > 0 and ID <= len(mainData):  # ID should be greater than 0 and less than or equal to the length of the
                # dictionary
                if int(mainData[ID][3]) > 0:
                    Valid_input = True
                    return ID
                else:
                    messages.out_of_stock()
            else:
                messages.invalid()
        except:
            messages.invalid()
def valid_quantity_purchase(Datapoint, ID):
    """ The availability of laptops is checked by this function. """
    valid_quantity = False
    while valid_quantity == False:
        try:
            quantity = int(input("How many pieces do you want to purchase?: "))
            if quantity > 0 and quantity <= int(Datapoint[ID][3]):
                valid_quantity = True
                return quantity
            else:
                messages.range() 
        except:
            messages.invalid()


def sell():
    """ The main function to sell laptops is added here. A 2D list is created and the user is asked if s/he wants to rent more laptops.A function to print and write the invoice is called.
    """
    print("\n Sell a laptop here. \n")

    file_contents = write.read_file()
    Datapoint = write.dictionary(file_contents)

    placeholder = []
    write.print_laptop(file_contents, Datapoint)
    continueLoop = True  # assigning boolean value 
    while continueLoop:  # outerloop

        Id = valid_id_sell(Datapoint)
        messages.available()
        qn = int(valid_quantity_sell(Datapoint, Id))
        Datapoint[Id][3] = int(Datapoint[Id][3]) - qn
        placeholder.append([Id, qn])

        write.write_file(Datapoint)
        write.print_laptop(file_contents, Datapoint)

        additional = True
        while additional:  # innerloop
            userInput = input("Do you want to buy or sell more laptops?(yes/no): ")

            if userInput.lower() == "no":
                continueLoop = False  # outerloop is terminated, bill details will be asked
                additional = False  # innerloop is terminated

            elif userInput.lower() == "yes":
                continueLoop = True  # outerloop continues, more laptops will be rented
                additional = False  # innerloop is terminated

            else:
                messages.invalid()
                additional = True  # innerloop continues

    print()
    write.sell_bill(placeholder)  # This function prints and writes the invoice
    messages.sell()

def valid_id_sell(Datapoint):
    """
         Valid or invalid ID entered is checked by this function.If the ID is not valid, an invalid message is shown.It takes the dictionary as a parameter, and returns the valid ID.
    """
    valid_id = False
    while valid_id == False:
        try:
            ID = int(input("Enter the ID of the Laptop you want to sell: "))
            if ID > 0 and ID <= len(Datapoint):
                valid_id = True
                return ID
            else:
                messages.invalid()
        except ValueError:
            messages.invalid()


def valid_quantity_sell(mainData, ID):
    """
        This function checks if the quantity entered is valid or not i.e.if the quantity is not less than 0 or in range of the laptop availability.
    """
    valid_quantity = False
    while valid_quantity == False:
        try:
            quantity = int(input("How many pieces do you want to sell?: "))
            if quantity > 0:
                valid_quantity = True
                return quantity
            else:
                messages.invalid()
        except ValueError:
            messages.invalid()


def purchase():
    """ The main function to purchase laptops is added here. A 2D list is created and the user is asked if s/he wants to return more laptops.A function to print and write the invoice is called.
    """
    print("\n Purchase a laptop here. \n")

    file_contents = write.read_file()
    mainData = write.dictionary(file_contents)

    placeholder = []
    continueLoop = True
    while continueLoop:  # outerloop
        write.print_laptop(file_contents, mainData)  # list of laptop is printed
        Id = valid_id_sell(mainData)
        qn = int(valid_quantity_sell(mainData, Id))
        mainData[Id][3] = int(mainData[Id][3]) + qn
        placeholder.append([Id, qn])

        write.write_file(mainData)
        write.print_laptop(file_contents, mainData)

        more = True
        while more == True:  # inner loop
            userInput = input("Do you want to buy or sell more laptop?(yes/no): ")
            if userInput.lower() == "no":
                continueLoop = False  # outerloop is terminated, bill details will be asked
                more = False  # inner loop is terminated

            elif userInput.lower() == "yes":
                continueLoop = True  # outerloop continues, more costumes will be purchased
                more = False  # inner loop is terminated

            else:
                messages.invalid()
                more = True  # inner loop continues

    print()
    write.purchase_bill(placeholder)  # function to print and write the bill
    messages.purchase()