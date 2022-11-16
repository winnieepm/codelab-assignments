# make a dictionary for Bea and Ben

# upload file
with open('wk7.txt', 'r') as infile:
    text = infile.read()

# variables
bea=0
ben=0
bea_char=0
ben_char=0
lines= text.split("\n\n")
dictionary = {'Beatrice':[], 'Benedick':[]} # defined dictionary

for line in lines:
    line.replace('\n', ' ')

    if line.startswith('BEATRICE.'):
        bea+=1
        bea_char+=len(line)-9

        dictionary['Beatrice'].append(line)
        
    elif line.startswith('BENEDICK.'):
        ben+=1
        ben_char+=len(line)-9

        dictionary['Benedick'].append(line)


print(dictionary)
