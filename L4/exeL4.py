def say_hello():
    print("hello world")


#   say_hello()


def print_number():
    number = 12
    print("The print_number function will print: {0}".format(number))


#   print_number()

# print("number is {0}".format(number))

def sum_two_number(x, y):
    num_one = x
    num_two = y
    result = x + y
    print("The result of {0} and {1} summarized is: {2}".format(num_one, num_two, result))


#   sum_two_number(5, 2)

list_ = [1, 2, 5, 7]


def print_list(list_x):
    for i in list_x:
        print(i)


#   print_list(list_)


list_two = [10, 23, 1, 2, 6, 19]


def min_max(lists):
    min_val = min(lists)
    max_val = max(lists)
    return min_val, max_val


x, y = min_max(list_two)


#   print(x, y)


def sum_two(x, y):
    result = x + y
    return result


def print_new_result():
    first_par = 10
    second_par = 20
    result = sum_two(first_par, second_par)

    print(result)


#   print_new_result()


from modexeL4 import print_message as pm

pm("hello")
