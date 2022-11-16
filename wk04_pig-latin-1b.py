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


# 1b. repeat and print output x100
# def repeat(fn):
#     repeats = range(101)
#     for num in repeats:
#          print(fn)
    
# repeat(pigLatin(input("Enter input: ")))

print(pigLatin('enter')*100)