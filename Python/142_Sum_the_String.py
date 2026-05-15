#30-12-2025 | 19-03-2026

'''
	Given: string with combination of int and char.
	Problem: add only the int in the given str.
	return: the total value of ints.
	Example: string_sum("a1b20c300") should return 321
'''

def string_sum(s):
    total = 0
    current_num = ""

    for char in s:
        if char.isdigit():
            current_num += char
        else:
            if current_num:
                total += int(current_num)
                current_num = ""

    if current_num:
        total += int(current_num)

    return total
