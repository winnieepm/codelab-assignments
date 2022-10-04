ints = int(input('Write a number: '))

def fizbuzz(num):
    if num%3==0:
        if num%5==0:
                print('fizzbuzz')
        else:
                print('fizz')
    elif num%5==0:
            print('buzz')
    else:
            print(num)

fizbuzz(ints)