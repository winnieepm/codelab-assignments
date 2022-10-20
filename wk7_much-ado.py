# INSTRUCTIONS
# Write a program to read in this file and count the total lines of dialog and the length (character count) of those lines for the two main characters: Benedick and Beatrice. Write that data out to a second file.



# STEP 0 turn file content into a line list called lines
lines=[]
with open('wk7.txt', 'r') as infile:
    for line in infile:
        lines.append(line)

# print(lines)
# STEP 1 find target person's name in lines list
ben=0
ben_char=0
bea=0
bea_char=0
for index, line in enumerate(lines):
    if line=="BENEDICK.\n":
        ben+=1
        while line!='\n':
            print(len(line))
        nextLine=lines[index+1]

    # if line=="BEATRICE.\n":
    #     bea+=1

# print(ben)
# print(bea)


# STEP 2 find all words BETWEEN chosen person and the next character speaking
# 2.1 define stop parameter




# 2.2 add dialogue lines to ben=[] or bea=[]
