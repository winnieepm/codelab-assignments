import json

with open('datasets/wk9_rotten-tomatoes.json', 'r') as jsonfile:
    
    jsondata = json.load(jsonfile)
    occurrences = 0
    list_in = []

    for movie in jsondata['movies']:
        if "abridged_cast" in movie:
            for person in movie["abridged_cast"]:
                if "625475404" == person["id"]:
                    occurrences+=1
    print(occurrences)