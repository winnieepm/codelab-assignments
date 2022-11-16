def pigLatin(word): 
    index = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for letter in word:
        index += 1

        if word[0] in vowels:
            return word + 'yay'
            break

        elif word[0] not in vowels and word[1] in vowels:
            return word[1:] + word[0] + 'ay'
            break
        
        elif word[index] in vowels:
            return word[index:] + word[:index] + 'ay'
            break

# 1d. Modify your code in part 1c to repeat just the first word in pig latin one hundred times, but also print the rest of the words after that.
# def repeat(fn):
#     repeats = range(101)
#     for num in repeats:
#          print(fn)

# str = input("Enter input: ")
# str = str.split(' ')

# repeat(pigLatin(str[0]))
# print(str[1:])

# print(pigLatin(list = input('write here: ').split()[0]*100))

str = input('write here: ').split()
print(pigLatin(str[0])*100, str[0:])


