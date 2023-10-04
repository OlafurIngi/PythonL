# opgave 1

def supplier():
    input_product_one = input("Choose one of the following products (A, B, C): ").upper()
    input_product_two = input("Choose one of the following products (A, B, C): ").upper()

    if(input_product_one == "A" or input_product_one == "B") and (input_product_two == "A" or input_product_two == "B"):
        print("Your supplier is supplier 1")
    elif(input_product_one == "A" or input_product_one == "C") and (input_product_two == "A" or input_product_two == "C"):
        print("Your supplier is supplier 2")
    elif (input_product_one == "B" or input_product_one == "C") and (input_product_two == "B" or input_product_two == "C"):
        print("Your supplier is supplier 3")
    else:
        print("wrong inputs")


#   supplier()

def guess_the_number():
    import random
    num_between_zero_hundred = random.randint(0,100)
    guess_tally = 0


    while True:
        user_input = int(input("Choose a number between 0 and 100: "))
        if user_input == num_between_zero_hundred:
            print("Success, you beat the computer")
            guess_tally = guess_tally + 1
            print("You beat the computer in {0} guesses".format(guess_tally))
            break

        elif user_input < num_between_zero_hundred:
            print("The value is higher, try again")
            guess_tally = guess_tally + 1

        else:
            print("The value is lower, try again")
            guess_tally = guess_tally + 1


#   guess_the_number()

def multi_table():
    for x in range(0, 11):
        for y in range(0, 11):
            print(x * y, end=" \t ")



#   multi_table()


def keep_stock():
    weekly_manufacturing = 50
    import random
    inventory_level = 10

    for week in range(1, 53):
        weekly_shipped = random.randint(40, 60)
        print("the weekly shipped for week {0} is {1}".format(week, weekly_shipped))
        print("the inventory level for week {0} is {1}".format(week, inventory_level + weekly_manufacturing))
        inventory_level = inventory_level + weekly_manufacturing - weekly_shipped
        if inventory_level < 0:
            inventory_level = 0
        print("for week {0} the new inventory is {1}".format(week, inventory_level), "\n")


#   keep_stock()

def keep_stock_mod():
    weekly_manufacturing = 50
    import random
    inventory_level = 10
    stock_outs = 0
    total_inventory = 0
    for week in range(1, 1001):
        weekly_shipped = random.randint(40, 60)
        old_inv = inventory_level + weekly_manufacturing
        inventory_level = inventory_level + weekly_manufacturing - weekly_shipped

        if inventory_level < 0:
            inventory_level = 0
            stock_outs = stock_outs + 1

        total_inventory += inventory_level

        if week % 50 == 0:
            print("the weekly shipped for week {0} is {1}".format(week, weekly_shipped))
            print("for week {0} the old inventory is {1}".format(week, old_inv))
            print("for week {0} the new inventory is {1}".format(week, inventory_level))
            print("The amount of stock outs is {0}".format(stock_outs))
            print("The running total is {0}".format(total_inventory))
            print("The average inventory is {0}".format(total_inventory / week), "\n")


#   keep_stock_mod()


def cond_file_process():




