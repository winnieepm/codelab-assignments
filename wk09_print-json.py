import json

caroline = {'bio': {'born':'united states', 'edu':'phd student', 'job_exp':'teaching asistant', 'dept':'art history'}, 'icebreak': {'best_tacos': 'brazos tacos', 'bad_movie':'tremors (1990)'}}
malcolm = {'bio': {'born':'united states', 'edu':'phd student', 'job_exp':'teaching asistant', 'dept':'history'}, 'icebreak': {'best_tacos': 'brazos tacos', 'bad_movie':'anything kevin hart', 'worst_dish':'iceberg lettuce'}}
samantha = {'bio': {'born':'jamaica', 'edu':'phd student', 'job_exp':['instructor', 'research assistant'], 'dept':'english'}, 'icebreak': {'best_tacos': 'don\'t know', 'bad_movie':'a knight\'s tale (2001)', 'worst_dish':'cornmeal porridge'}}
winnie = {'bio': {'born':'puerto rico', 'edu':'phd student', 'job_exp':['instructor', 'research assistant'], 'dept':'spanish'}, 'icebreak': {'best_tacos': 'don\'t know', 'bad_movie':['labyrinth (1986)', 'waiting (2005)'], 'worst_dish':'cornmeal porridge'}}
cohort = [caroline, malcolm, samantha, winnie]

with open('wk9_result.json', 'w') as rawdata:
    rawdata.write(json.dumps(cohort))