#1
def greet(language):
    return {
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'english': 'Welcome',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }.get(language, 'Welcome')

#2
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5


total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

print(total_goals)

#3
def two_sort(array):
    array.sort()
    
    return '***'.join(array[0])


#4
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
    

#5
def solution(a, b):
    short, long = (a, b) if len(a) < len(b) else (b, a)
    
    return short + long + short


#6
def fix_the_meerkat(arr):
    return arr[::-1]
