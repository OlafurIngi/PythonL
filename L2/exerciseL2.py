def exercise1():
    print(15 + 32)
    print(4 * 6)
    print("hello world")
    print(hello)
    print(len("hello world"))

# exercise1()


def arithmetic(value1, value2, value3, value4):
    xmean = (value1 + value2 + value3 + value4)/4
    print(xmean)


# arithmetic(10, 7, 3, 9)

def areaOfCircle():
    radius = eval(input("Please enter the radius: "))
    pi = 3.14
    print("The area of the circle is {0}".format(pi * radius * radius))

# areaOfCircle()

def arithmeticUser():
    xValue1, xValue2, xValue3, xValue4 = eval(input("Enter four numbers separated by comma: "))
    print((xValue1 + xValue2 + xValue3 + xValue4)/4)

# arithmeticUser()


def cupOfTea():
    cup = "a cup of tea"
    bread = "a piece of bread"
    print("I would like to have {0} and {1}".format(cup, bread))

# cupOfTea()


def summation():
    number = eval(input("Choose a random number: "))
    result = 0
    for i in range(number + 1):
        result = result + i
    print(result)

# summation()


