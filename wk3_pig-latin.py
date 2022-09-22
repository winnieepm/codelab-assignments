# goal: write a program that can translate english into pig latin. 

# 1st ATTEMPT
# word = input('Type one word: ')
# print(word[1:] + word[0] + 'ay')
# function

# FUNCTION
# def pigLatin(word):
#     return print(word[1:] + word[0] + 'ay')

# word = 'scholar'
# vowels = ['a', 'e', 'i', 'o', 'u']
# index = 0 

# def pigLatin(word):
    
word = input('Type one word: ')
index = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for letter in word:
        index += 1

        if word[0] in vowels:
            print(word + 'yay')
            break

        elif word[0] not in vowels and word[1] in vowels:
            print(word[1:] + word[0] + 'ay')
            break
        
        elif word[index] in vowels:
            print(word[index:] + word[:index] + 'ay')
    

