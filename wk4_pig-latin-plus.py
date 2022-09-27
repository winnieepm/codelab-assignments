def pigLatin(word): 
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
            break

# 1a. print(pigLatin(input("Enter input: ")))


# 1b. repeat and print output from function x100
# def repeat(fn):
#     repeats = range(101)
#     for num in repeats:
#         print(fn)
# repeat(pigLatin(input("Enter input: ")))


# 1c. Modify your code in part 1a to split() the input into a list of multiple words. If there is only one word, it'll just be a list with one element. Then, only print the Pig Latin for the first word. The Python documentation for a particualr string method will be very useful here!

str = input("Enter input: ")
str = str.split(' ')

pigLatin(str[0])