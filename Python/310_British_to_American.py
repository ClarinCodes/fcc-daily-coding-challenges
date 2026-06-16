# 16-06-2026 | 16-06-2026

"""
    Problem: 
        Convert British English spellings in a sentence to their American English equivalents.

    Args:
        sentence (str) : Input sentence.

    Return:
        str : Coverted sentence with American English spellings.
"""

import re

def british_to_american(sentence):

    # Given
    brit_to_amer = {
        "colour": "color",
        "flavour": "flavor",
        "honour": "honor",
        "neighbour": "neighbor",
        "labour": "labor",
        "humour": "humor",
        "centre": "center",
        "fibre": "fiber",
        "defence": "defense",
        "offence": "offense",
        "organise": "organize",
        "recognise": "recognize",
        "analyse": "analyze",
    }

    def replace(match, replacement):
        word = match.group()

        # preserve capitalization style
        if word.isupper():
            return replacement.upper()
        if word[0].isupper():
            return replacement.capitalize()
        return replacement

    for brit, amer in brit_to_amer.items():

        # re.escape(brit) ensures any special characters in the word are treated as normal text
        # re.IGNORECASE allows matching words regardless of uppercase/lowercase (e.g., "Colour", "COLOUR")
        pattern = re.compile(re.escape(brit), re.IGNORECASE)

        # pattern.sub(...) searches the sentence for the British word and replaces all occurrences
        # lambda m passes each matched word (m) into the replace() function
        # replace(m, amer) converts the word properly and preserves capitalization
        sentence = pattern.sub(lambda m: replace(m, amer), sentence)

    return sentence


def test_cases():
    assert british_to_american("I love the colour blue.") == "I love the color blue."
    assert british_to_american("The fibre optic cable is new.") == "The fiber optic cable is new."
    assert british_to_american("It's an honour to meet someone with such humour.") == "It's an honor to meet someone with such humor."
    assert british_to_american("The unrecognised artist analysed his colour palette at the centre.") == "The unrecognized artist analyzed his color palette at the center."
    assert british_to_american(
        "The offence analysed, with organisation, the defence centre and recognised that the neighbouring labouror was humourous, flavourful, and colourful."
    ) == "The offense analyzed, with organisation, the defense center and recognized that the neighboring laboror was humorous, flavorful, and colorful."

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
