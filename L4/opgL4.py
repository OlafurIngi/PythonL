#   Exercise 1

def barcode_loop():
    barcodes = ["This is the bar code - barcode001", "This is the bar code - barcode002", "This is the bar code - barcode003"]

    for i in barcodes:
        print(i)


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


#   write_data()


def fibonacci(n):
    result = 0
    value_one = 0
    value_two = 1
    for i in range(1, n):
        n = value_one + value_two
        value_one = value_two
        value_two = n
        result += 1

        print(value_two)


#   fibonacci(7)




