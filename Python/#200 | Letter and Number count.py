def count_letters_and_numbers(s):
    letters = []
    numbers = []
    #separating string and integers
    for i in s:
        if i.isdigit():
            numbers.append(i)
        elif i.isalpha():
            letters.append(i)

    if len(letters) != 1:
        letter_str = "letters"
    else:
        letter_str = "letter"

    if len(numbers) != 1:
        number_str = "numbers"
    else:
        number_str = "number"

    return f"The string has {len(letters)} {letter_str} and {len(numbers)} {number_str}."
