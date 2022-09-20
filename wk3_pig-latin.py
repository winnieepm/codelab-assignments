# goal: write a program to that accepts one word at a time and prints out its simplified pig latin translation


# 1. get one word, probs using a built-in function, and store it in a variable
word = input('Type one word: ')

# 2.  translation process 
# 2.1 find index of the first character = word[0]
# 2.2 move first character to last. easier to slice and add = word[1:] + word[0]
# 3. print translation
print(word[1:] + word[0] + 'ay')
