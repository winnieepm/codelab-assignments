# INSTRUCTIONS
# Write a program to read in this file and count the total lines of dialog and the length (character count) of those lines for the two main characters: Benedick and Beatrice. Write that data out to a second file.

# STEP 0 upload file
with open('wk7.txt', 'r') as infile:
    text = infile.read()

bea=0
ben=0
bea_char=0
ben_char=0
lines= text.split("\n\n")

for line in lines:
    line.replace('\n', ' ')

    if line.startswith('BEATRICE.'):
        bea+=1
        bea_char+=len(line)-9
        
    elif line.startswith('BENEDICK.'):
        ben+=1
        ben_char+=len(line)-9


# STEP 3 printout
with open('wk7_result.txt', 'w') as outfile:
    outfile.write('Beatrice has '+str(bea)+' lines which equals '+str(bea_char)+' characters.\n')
    outfile.write('Benedick has '+str(ben)+' lines which equals '+str(ben_char)+' characters.\n')
    outfile.close()

    # Jeremy helped me work through this problem. He was so patient!