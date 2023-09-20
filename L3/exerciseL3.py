def type_test():
    number_ = 10
    #   Checks type of number
    print(type(number_))
    #   Checks if type is float isinstance(var, type)
    print("Type is float:", isinstance(number_, float))
    print("Type is int:", isinstance(number_, int))

    type_one = 5
    type_two = "Hello"
    type_three = 3.3
    print(type(type_one), type(type_two), type(type_three))

    str_one = '123'
    str_two = "tom"
    str_three = '''this is'''
    str_four = '''                  hello
                  world'''

    print(str_one)
    print(str_two)
    print(str_three)
    print(str_four)


#   type_test()


def string_type():
    # Q1
    str_ = "smart lab"
    print(str_[0])
    print(str_[1:3])
    print(str_[:4])
    print(str_[:])
    print(str_[3:])
    # search for letter
    index = str_.find("r")
    print(str_[index:])

    # Q2
    str_lets_go = "hello"
    # delete string
    # del str_lets_go
    print(str_lets_go, "\n")

    # Q3
    str_find = "come on man"
    res = "co" in str_find
    print(res)

    resf = "come" not in str_find
    print(resf)

    print(str_find.find("on"), "\n")

    # Q4
    word_count = 0
    word = "Hello Tom"

    for val in word:
        word_count = word_count + 1
        print(val)


#   string_type()


def list_type():
    # get item within list
    list_one = [3, 10, [1, 2, 3]]
    print(list_one[2][1])

    # slice list
    print(list_one[2][1:])
    print(list_one[:-1])

    # append elements in list
    list_one.append(57)
    print(list_one)

    list_two = [9, 8]
    list_one = list_one + list_two
    print(list_one)

    # modify elements
    list_one[0] = 5
    print(list_one)

    # delete elements
    del list_one[0]
    print(list_one)

    # iterate through list
    for val in list_one:
        print(val)


list_type()
