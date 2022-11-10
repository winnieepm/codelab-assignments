import json
import nltk

with open("MAAN_dialog.json","r") as infile:
    dialog = json.loads(infile.read())

bea = ""
ben = ""

for line in dialog:
    if line["role"] == "BEATRICE":
        bea+=" "+line["dialog"]
    elif line["role"] == "BENEDICK":
        ben+=" "+line["dialog"]