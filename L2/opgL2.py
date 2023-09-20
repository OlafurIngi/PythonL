# Assignment 1

L, W = 5, 0.8

Lambda = L * W
print(Lambda)  # 4

# Assignment 2

CashPrice = 2398000
TransactionCost = CashPrice * 0.0323
DownPayment = CashPrice * 0.10
PreparedCash = TransactionCost + DownPayment
print(PreparedCash)  # 317255.4


# Assignment 3


def numberOfCentersCalculated():
    NumberOfCenters = eval(input("Enter the amount of work centers: "))
    Results = 1
    for i in range(1, NumberOfCenters + 1):
        Results = Results * i
        print(Results)


# numberOfCentersCalculated()


# Assignment 4

totalCost = 980000
interestPerYear = 0.07
payPerYear = 25000


def loanPayback():
    global totalCost
    global interestPerYear
    global payPerYear
    year = 1
    while year * payPerYear <= totalCost:
        year = year + 1

    totalInterest = year * interestPerYear * totalCost
    print("The Total amount of years till the loan is paid back is {0}".format(year))
    print("the total interest is {0}".format(totalInterest))


loanPayback()


# Assignment 5


def warehouse():
    days = 1
    while (days / 3) * 100 + 1000 >= (days / 2) * 75:
        days = days + 1

    print('It took {0}'.format(days), "for the warehouse to be emptied")


warehouse()
