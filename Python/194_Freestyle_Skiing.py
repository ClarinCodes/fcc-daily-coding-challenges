#20-02-2026 | 21-02-2025

''' given: a string with 2 words.
    problem: the first word must be in list1 and the second word must be in list2 
    given lists,
Valid first words:
"Misty"
"Ghost"
"Thunder"
"Solar"
"Sky"
"Phantom"
"Frozen"
"Polar"

Valid second words:
"Twister"
"Icequake"
"Avalanche"
"Vortex"
"Snowstorm"
"Frostbite"
"Blizzard"
"Shadow"

    example: is_valid_trick("Polar Vortex") should return True. '''


def is_valid_trick(trick_name):
    first_words = ["Misty","Ghost","Thunder","Solar","Sky","Phantom","Frozen","Polar"]
    second_words = ["Twister","Icequake","Avalanche","Vortex","Snowstorm","Frostbite","Blizzard","Shadow"]
    given_words = trick_name.split()

    if given_words[0] in first_words and given_words[1] in second_words:
        return True
    else:
        return False
            
