import json

with open('datasets/wk9_rotten-tomatoes.json', 'r') as jsonfile:
    
    jsondata = jsonfile.read()
    words = jsondata.split()
    occurrences = 0
    list_in = []

    # count how many movies the dataset has.
    # status: works*
    for i in jsondata:
        if 'title' in jsondata:
            occurrences+=1
    print('there are ' + str(occurrences) + ' movies in this dataset.')
  
    # *** 1- lacks \" to specify a movie instance, not just that it's the word 'title'.

 
    # # find how many movies Krasinski is in and print them
    # for i in words:
    #     if '\"name\"' in i:
    #         print(words.index(i))
    #         occurrences+=1   

# idk pq esta stuck en el index 115. como sumo 1 a la i? o mejor, pq no cambia cuando pasa a la proxima palabra!?