# Exercise 1
# print(7 // 3)


# Chaos function (exercise 2 - 7)
def main(person, job):
    print("This program illustrates a chaotic function")
    n = eval(input('How many numbers should i print ' + person + ' who is a ' + job + '? '))
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    for i in range(n):
        x = 2.0 * x * (1 - x)
        y = 4.0 * y * (1 - y)
        print(round(x, 2), round(y, 2))


main("Oli", "Engineer")
