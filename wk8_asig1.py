# Think about everything you know about your Praxis cohort (the icebreakers doc is fair game). Think about the kind of questions that might interest you about such a corpus and the best way to structure that information to answer those questions. Write some Python code in the vein of the Scholars Lab example in the data structures review that represents the model you come up with. This one is intentionally a bit amorphous, but any practice in thinking about the shape of data is useful.

# peeps into data
caroline = {'bio': {'born':'united states', 'edu':'phd student', 'job_exp':'teaching asistant', 'dept':'art history'}, 'icebreak': {'best_tacos': 'brazos tacos', 'bad_movie':'tremors (1990)'}}
malcolm = {'bio': {'born':'united states', 'edu':'phd student', 'job_exp':'teaching asistant', 'dept':'history'}, 'icebreak': {'best_tacos': 'brazos tacos', 'bad_movie':'anything kevin hart', 'worst_dish':'iceberg lettuce'}}
samantha = {'bio': {'born':'jamaica', 'edu':'phd student', 'job_exp':['instructor', 'research assistant'], 'dept':'english'}, 'icebreak': {'best_tacos': 'don\'t know', 'bad_movie':'a knight\'s tale (2001)', 'worst_dish':'cornmeal porridge'}}
winnie = {'bio': {'born':'puerto rico', 'edu':'phd student', 'job_exp':['instructor', 'research assistant'], 'dept':'spanish'}, 'icebreak': {'best_tacos': 'don\'t know', 'bad_movie':['labyrinth (1986)', 'waiting (2005)'], 'worst_dish':'cornmeal porridge'}}


# ask questions

#1- Did the films chosen for favorite bad movie come out in a similar decade?
cohort = [caroline, malcolm, samantha, winnie]
movies = []

for person in cohort:
    str_answer = str(person['icebreak']['bad_movie'])
    movie_yrs = []

    # while loop vars
    index=0
    start=0
    end=0
    
    while index < len(str_answer):
        if str_answer[index] == '(':
            start = index+1
        elif str_answer[index] == ')':
            end = index
            movie_yrs.append(str_answer[start:end])
        index+=1  


    print(type(movie_yrs)  )
    # print('The movies came out on' + str(movie_yrs) + ', respectively.')
    

# ISSUES
# a. pq no sale waiting (2005)? FIXED thanks to Jeremy
# b. why can't i get nice string values out for movie_yrs? should i concatenate the lists?


# extra questions, if i ever try again
# 1-a necesitas otra variable con los años en una decada pa' compararla (la variable) con movie_yrs. 
# 1-b añade regla pendeja: "si 2 < años en movie_yrs == decada, print("yup, they're from similar decades / no, they're not far apart in time")
#2- What are the worst dishes they've eaten?
#3- Is this cohort a diverse group?


# Jeremy's advice on nov/03: 
# issue: pq no sale waiting (2005)?
# add elif stmt to catch whatever you're missing. 
# find a way to make the start/end vars to look for the second pair of parentheses