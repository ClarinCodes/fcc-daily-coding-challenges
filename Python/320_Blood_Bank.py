# 26-06-2026 | 26-06-2026

"""
    Problem:
        Given a blood bank inventory and a list of patient requests, determine the maximum number of patients that can be served based on blood type compatibility rules.
    
    Compatibility Rules:
        - Type O patients: Can only receive Type O.
        - Type A patients: Can receive Type A or Type O.
        - Type B patients: Can receive Type B or Type O.
        - Type AB patients: Can receive Type AB, A, B, or O (Universal Recipient).
    
    Args:
        bank (list[str]): List of available blood units.
        patients (list[str]): List of patient blood types.

    Returns:
        str : A string formatted as "X of Y patients served", where X is the number of successful transfusions and Y is the total number of patients.
"""

def triage_blood(bank, patients):
    
    inv = {'A': 0, 'B': 0, 'AB': 0, 'O': 0}
    for b in bank:
        inv[b] += 1
    
    cured = 0
    
    for p in patients:
    
        if inv[p] > 0:
            inv[p] -= 1
            cured += 1
        
        elif p == 'AB':
            if inv['A'] > 0:
                inv['A'] -= 1; cured += 1
            elif inv['B'] > 0:
                inv['B'] -= 1; cured += 1
            elif inv['O'] > 0:
                inv['O'] -= 1; cured += 1

        elif p == 'A' and inv['O'] > 0:
            inv['O'] -= 1; cured += 1
        elif p == 'B' and inv['O'] > 0:
            inv['O'] -= 1; cured += 1
            
    return f"{cured} of {len(patients)} patients served"



def test_cases():
    assert triage_blood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"]) == "4 of 4 patients served"
    assert triage_blood(["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"]) == "3 of 5 patients served"
    assert triage_blood(["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"]) == "4 of 5 patients served"
    assert triage_blood(["O", "O", "O", "O", "O"], ["O", "A", "B", "AB"]) == "4 of 4 patients served"
    assert triage_blood(["A", "O", "B", "AB", "B", "AB", "O", "A", "A"], ["O", "A", "B", "AB", "A", "B", "A", "A", "B", "A", "B"]) == "8 of 11 patients served"
    assert triage_blood(["O", "B", "AB", "AB", "O", "A", "A", "AB", "O", "B", "B", "AB", "A", "B", "AB"], ["O", "A", "B", "B", "A", "B", "AB", "A", "B", "A", "O", "AB", "AB", "O"]) == "13 of 14 patients served"

    print("All test cases passed!")

if __name__ == "__main__":
    test_cases()
