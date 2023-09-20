def find_date_time():
    str_ = '17-10-2019 15:30:17'
    index = str_.find(' ')
    print(str_[0:index])
    print(str_[1 + index:])


#   find_date_time()


def find_key_word():
    str_ = ('The traditionally literature has demonstrated the beneficial impact of an appropriate manufacturing '
            'strategy on the business strategy and performance,but this study highlights the difficulty of managers '
            'to set the strategy, let alone implementing it. This is partly caused by the immense pressure of '
            'customers in these dominantly Make-To-Order environments for SMEs. Current concepts for manufacturing '
            'capabilities have insufficiently accounted this phenomenon and an outline of a research agenda is '
            'presented')

    print(str_.find('manufacturing capabilities'))


#   find_key_word()


def inventory_management():
    listInv = ['drilling machine', 'counting machine', 'quality control machine', 'mounting machine']
    listAdd = ['drilling machine', 'robot']
    listInv.extend(listAdd)
    print(listInv)
    print(listInv.count('drilling machine'))
    listInv.sort()
    print(listInv)


#   inventory_management()


def sales():
    listSales = [250000, 180000, 320000, 90000, 400000]

    print(listSales[2:])
    print(max(listSales))
    print(min(listSales))


#   sales()

def open_file():

    fileOne = open("dep_one.txt", "r")
    fileOneData = fileOne.read()

    fileTwo = open("dep_two.txt", "r")
    fileTwoData = fileTwo.read()

    fileThree = open("dep", "w")
    fileThree.write(fileOneData + "\n" + fileTwoData)

    fileOne.close()
    fileTwo.close()
    fileThree.close()

    fileThree = open("dep", "r")
    fileThreeData = fileThree.read()
    print(fileThreeData)
    fileThree.close()

    fileThree = open("dep", "r")

    for lineInList in fileThree:
        index = lineInList.find(" ")
        print(lineInList[:index])

    fileThree.close()


#   open_file()

def max_min_avg():
    fileOpen = open("data.csv", "r")
    lines = fileOpen.readlines()
    listOne = lines[1:]
    listTwo = []

    for val in listOne:
        listTwo.append(int(val[:-1]))
    print(min(listTwo))
    print(max(listTwo))

    result = 0
    lenListTwo = len(listTwo)

    for val in range(lenListTwo):
        result = result + listTwo[val]

    print(result/lenListTwo)

#   max_min_avg()
