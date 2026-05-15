#11-05-2026 | 11-05-2027

'''
    Problem:
            Find the oldest age and return their names.

    Args:
            data (list[dict]) -> List of people where each dict contains, name (str) and age (int).

    Return:
            list[str] -> List of names who are the oldest. 

    get_oldest([{ "name": "Allison", "age": 25 },
                { "name": "Bill", "age": 30 },
                { "name": "Carol", "age": 30 }]) 
                should return ["Bill", "Carol"].
'''

def get_oldest(people):
    
    max_age = max(x["age"] for x in people)

    return [i["name"] for i in people if i["age"] == max_age]
