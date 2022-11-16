# write a function that takes in a list of integers as an argument and returns a list of integers comprising only the even numbers.

ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_evens(number):
    num=0
    num=+1
    for num in number:
        if num%2 == 0:
            print(num)

filter_evens(ints)