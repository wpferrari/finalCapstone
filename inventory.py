from time import sleep


# ========The beginning of the class==========
class Shoe:
    # constructing the class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):  # function into a class to return cost variable
        return self.cost

    def get_quantity(self):  # function into a class to return quantity variable
        return self.quantity

    def __str__(self):  # string format
        item = f"{self.country:15} {self.code:10} {self.product:28} {self.cost:5}  {self.quantity:10}"
        return item


# =============Shoe list===========

shoe_list = []  # blank list


# ==========Functions outside the class==============
def read_shoes_data():  # function to read inventory and insert into the list
    try:
        with open('inventory.txt', 'r') as y:  # opening txt to read
            for n, line in enumerate(y.readlines()):
                if n == 0:
                    pass
                else:
                    shoe_list.append(line.strip().split(','))  # inserting each line into a list
    except FileNotFoundError:
        print('File not found.')


def capture_shoes():  # function to add new shoe

    # creating some variables about shoe details
    country = input('Please enter the country: ').title()
    while True:  # creating a validation up to code
        code = input('Please enter the code [0 to return to main menu]: ').upper()
        if code == '0':
            return
        elif code != '0':
            # checking len of the code
            if len(code) > 8:
                print('The code is long, please insert again.')
            elif len(code) < 8:
                print('Your code is short, please insert again.')
            elif len(code) == 8:
                if 'SKU' in code: # checking characters in code
                    code_check = False
                    for x in shoe_list:
                        if x[1] == code:
                            code_check = True
                    if code_check == True:  # checking if code doesn't exist
                        print('Code already exist, please enter different code.')
                    else:
                        break
                else:
                    print("Your code must start with SKU, please insert again.")
    product = input('Please enter the product name: ').title()
    cost = input('Please enter the cost: ')
    quantity = input('Please enter the quantity: ')
    shoe_list.append([country, code, product, cost, quantity])
    print('New Shoe included on stock.')

    with open('inventory.txt', 'a') as insert:  # including the new shoe into the txt doc
        insert.write(f'{country},{code},{product},{cost},{quantity}\n')
    sleep(3)


def view_all():  # function to get and print all inventory items
    print("{:16}{:11}{:29}{:6}{:2}".format('Country', 'Code', 'Product', 'Cost', 'Quantity'))
    for l in shoe_list:
        item = Shoe(l[0], l[1], l[2], l[3], l[4])
        print(item.__str__())
    print()
    hold = input('Press Enter to continue.')


def re_stock():  # function to check the lowest shoe in stock
    lower = 0
    lower_item = []
    position = 0

    for n, w in enumerate(shoe_list):  # loop to check quantity of each shoe
        w[4] = int(w[4])

        if n == 0:  # if is the first check, the lowest stock will be the first
            lower = w[4]
            position = n

        else:  # if is not the first in the line, do the validation
            if lower > w[4]:
                lower = w[4]
                position = n
    try:
        print(f'The lower item in stock is {shoe_list[position]}')
        question = int(input('Would you like to add any quantity?\n'
                             'Enter quantity to be add or 0 if not:  '))  # variable to check if the user wants to insert quantity in stock

        if question != 0:  # preparing the string to update into the txt
            lower_item = shoe_list[position]
            lower_item[4] = str(lower_item[4])
            lower_item = ','.join(lower_item)
            shoe_list[position][4] = question + lower
            updated = shoe_list[position]
            updated[4] = str(updated[4])
            updated = ','.join(updated)

            with open('inventory.txt', 'r') as read:  # open and read txt
                data = read.read().strip()
                data = data.replace(lower_item, updated)  # replacing shoe in txt

            with open('inventory.txt', 'w') as update:
                update.write(data)  # updating new line

    except ValueError:
        print('erro')
    print('Shoe updated.')
    hold = input('Press Enter to continue.')
    return lower_item


def seach_shoe():  # function to search shoe by code
    shoe_code = input('Please enter the shoes code: ')
    shoe_found = False
    shoe_details = []
    for x in shoe_list:  # loop to check each line shoe code
        if shoe_code == x[1]:
            shoe_found = True
            shoe_details = x
    if shoe_found is True:  # if code is found, print out
        print(f"\nShoe Details:\n"
              f"Country: {shoe_details[0]}\n"
              f"Code:    {shoe_details[1]}\n"
              f"Product: {shoe_details[2]}\n"
              f"Cost     {shoe_details[3]}\n"
              f"Quantity {shoe_details[4]}")
    else:
        print('Shoe not found.')
    print()
    hold = input('Press Enter to continue.')


def value_per_item():  # function to calculate value of each item from the list
    print("{:16}{:11}{:29}{:7}{:11}{:9}".format('Country', 'Code', 'Product', 'Cost', 'Quantity', 'Value'))
    for n, x in enumerate(shoe_list):  # loop to calculate each line value
        value = int(shoe_list[n][3]) * int(shoe_list[n][4])
        item = Shoe(x[0], x[1], x[2], x[3], x[4])
        print(item.__str__(), value)
    print()
    hold = input('Press Enter to continue.')


def highest_qty():  # function to get highest shoe stock
    higher = 0
    higher_shoe = []
    for n, x in enumerate(shoe_list):  # loop to get the highest quantity stock
        x[4] = int(x[4])
        if n == 0:  # if is the first item, the first become the highest
            higher = x[4]
            higher_shoe = x
        else:  # if is not the first item, check
            if higher < x[4]:
                higher = x[4]
                higher_shoe = x

    print(f"\nThe highest stock shoe is:\n"
          f"Country:  {higher_shoe[0]}\n"
          f"Code:     {higher_shoe[1]}\n"
          f"Product:  {higher_shoe[2]}\n"
          f"Cost:     {higher_shoe[3]}\n"
          f"Quantity: {higher_shoe[4]}")
    print()
    hold = input('Press Enter to continue')


read_shoes_data()  # using the function to read the txt doc

# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:  # loop to keep the user into the main menu
    print('-' * 10, 'NIKE', '-' * 10)
    print()
    print(' ' * 7, 'Main Menu\n'
                   'ADD - To add new shoe on the stock.\n'
                   'ALL - To see all stock.\n'
                   'LOWER - To check the lowest stock shoe.\n'
                   'HIGHER - To check the hiest stock shoe.\n'
                   'SEARCH - To seach shoe by the code.\n'
                   'VALUE - To check the value of each shoe in stock.\n'
                   'EXIT - To exit.'
          )
    user_choice = input('Please enter one of the option above: ').upper().strip()  # variable to get user choose

    # creating different ways up to the user choose.
    if user_choice == 'EXIT':
        print('Thanks for using our system.')
        break

    else:

        if user_choice == 'ADD':
            capture_shoes()

        elif user_choice == 'ALL':
            view_all()

        elif user_choice == 'LOWER':
            re_stock()

        elif user_choice == 'HIGHER':
            highest_qty()

        elif user_choice == 'SEARCH':
            seach_shoe()

        elif user_choice == 'VALUE':
            value_per_item()

        else:
            print('Please check the options again.\n')
