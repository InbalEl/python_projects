import sys

#------------------------------------------------------------------------------#
#ex1()

def ex1():
    list = []
    for n in range(2000, 3201):
        if (n % 5 != 0) and (n % 7 == 0):
            list.append(str(n))
    print(','.join(list))

#------------------------------------------------------------------------------#
#ex2()

def ex2(num):
    if num == 1:
        return num
    return (ex2(num - 1) * num)

#num = int(sys.argv[1])
#print(ex2(num))

#------------------------------------------------------------------------------#
#ex3(8)

def ex3(num):
    dict = {}
    for n in range(1, num+1):
        dict[n] = n*n
    print(dict)

#------------------------------------------------------------------------------#
#ex4()

def ex4():
    numbers = input("enter numbers, comma seperated: ")
    " ".join(numbers.split())
    list = (numbers.split(','))
    tup = tuple(list)
    print(list)
    print(tup)

#------------------------------------------------------------------------------#
#ex5()

class InputOutStr()