#   Exercise 1

def barcode_loop():
    string_ = "This is the bar code - "
    barcodes = ["barcode001", "barcode002", "barcode003"]

    for i in barcodes:
        print(string_ + i)


#   barcode_loop()

def sum_of_num(n):
    result = 0
    for i in range(0, n+1):
        result = result + i

    print(result)


#   sum_of_num(7)


def read_data():
    fileOne = open("dep_one.txt", "r")
    fileOneData = fileOne.read()

    fileTwo = open("dep_two.txt", "r")
    fileTwoData = fileTwo.read()

    fileOne.close()
    fileTwo.close()
    return fileOneData, fileTwoData


def write_data():
    read_var = read_data()
    fileThree = open("dep", "w")
    fileThree.write(read_var[0] + "\n" + read_var[1])

    fileThree.close()


write_data()


def fibonacci(n):
    value_one = 0
    value_two = 1
    for i in range(1, n):
        n = value_one + value_two
        value_one = value_two
        value_two = n
        print(value_two)


#   fibonacci(10)

def call_sum_two_number():
    from modL4 import sum_of_numbers
    print(sum_of_numbers(5,2))


call_sum_two_number()

