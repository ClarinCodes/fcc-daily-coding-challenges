#16-08-2025 | 29-03-2026 

'''
    Given: two strings.
    Problem: check whether each string contains the same character in any order. do casing (converting all char to upper or lower case)ignore white space.
    Return: True if the two str has same characters, else False.
'''

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1_clean = str1.replace(" ", "").lower()
    str2_clean = str2.replace(" ", "").lower()
    
    # Sort letters
    return sorted(str1_clean) == sorted(str2_clean)

def test_cases():
    print(are_anagrams("listen", "silent"))                # True
    print(are_anagrams("School master", "The classroom"))  # True
    print(are_anagrams("A gentleman", "Elegant man"))      # True
    print(are_anagrams("Hello", "World"))                  # False
    print(are_anagrams("apple", "banana"))                 # False
    print(are_anagrams("cat", "dog"))                      # False

if __name__ == "__main__":
    test_cases()
