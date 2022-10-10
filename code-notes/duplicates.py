list = [5, 3, 2, 5, 2, 1]

# SOLUTION REQUIRES AN EMPTY LOOP.
# dupes = []
# for num in list:
#     if num not in dupes:
#         dupes.append(num)
#     else:
#         print('duplicate found!')

# NO EXTRA VARIABLE NEEDED
def hasDupe(list):
    i=0
    while (i<len(list)-1):
        j=i+1
        while(j<len(list)):
            if list[i]==list[j]:
                print('Dupe found')
                return True
            j=j+1
        i=i+1
    return False