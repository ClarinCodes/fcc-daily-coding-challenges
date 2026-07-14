# 14-07-2026 | 14-07-2026

"""
    Problem:
        Given a pet type and age in human years, return the equivalent age in pet years.

    Args:
        pet (str): The name of the pet.
        age (int): The age of the pet in human years.

    Return:
        int: The calculated age of the pet in pet years.
"""

def pet_years(pet, age):

    pets = {
            "dog" : 7,
            "cat" : 6,
            "rabbit" : 8,
            "hamster" : 30,
            "guinea pig" : 12,
            "goldfish" : 6,
            "bird" : 5
            }
    
    return pets[pet] * age
