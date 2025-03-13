# c_line_up_system.py
'''
Title: Waiting in Line
Author: Laksh Chopra
Date-Created: 06/10/2022
'''

### --- SUBROUTINES --- ###
### INPUTS
def menu():
    '''
    User selects a function
    :return: int.
    '''
    print("""
    1. Stand in Line
    2. Serve a Customer
    3. Exit
    """)
    CHOICE = input("> ")
    return int(CHOICE)

def askName():
    '''
    Waiting customer inputs their name
    :return: str
    '''
    return input("Name: ")

### PROCESSING
def addToLine(NAME, LINE):
    '''
    Add the name of the customer to the line
    :param NAME: str
    :param LINE: list of the current customers in line
    :return: list
    '''
    LINE.append(NAME)
    return LINE

def serveNextCustomer(LINE):
    '''
    Returns the next customer in line
    :param LINE: list
    :return: str
    '''
    CUSTOMER = LINE.pop(0)
    return CUSTOMER

### OUTPUTS
def displayNextCustomer(CUSTOMER):
    '''
    displays text to indicate the next customer
    :param CUSTOMER: str
    :return: none
    '''
    print(f"The next customer to be served is {CUSTOMER}.")
def displayLineLength(LINE):
    '''
    Displays to the customer where they are in the line
    :param LINE: list
    :return: nothing
    '''
    print(f"{LINE[-1]}, you are the {len(LINE)} person in line.")

### --- MAIN PROGRAM CODE --- ###
if __name__ == "__main__":
    ### VARIABLES
    CUSTOMERS = []
    while True:
        ### INPUTS
        ACTION = menu()
        if ACTION == 1:
            CUSTOMER = askName()
            CUSTOMERS = addToLine(CUSTOMER, CUSTOMERS)
            print(CUSTOMERS)
            displayLineLength(CUSTOMERS)
        elif ACTION == 2:
            if len(CUSTOMERS) > 0:
                NOW_SERVING = serveNextCustomer(CUSTOMERS)
                displayNextCustomer(NOW_SERVING)
            else:
                print("No one is in line.")
        else:
            exit()

        ### PROCESSING

        ### OUTPUTS