# INSTRUCTIONS
# Write a program to read in this file and count the total lines of dialog and the length (character count) of those lines for the two main characters: Benedick and Beatrice. Write that data out to a second file.



# STEP 0 turn file content into a line list called lines
lines=[]
with open('wk7.txt', 'r') as infile:
    for line in infile:
        lines.append(line)

# STEP 1 find target person's name in lines list
for line in lines:



# STEP 2 find words BETWEEN chosen person and the next
# 2.1 define stop parameter



# 2.2 add dialogue lines to ben=[] or bea=[]
