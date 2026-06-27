# 27-06-2026 | 27-06-2026

"""
    Problem:
        - Determine whether the given string can be spelled using element symbols from the periodic table.
        - Ignore casing.

    Args:
        word (str) : Input word.

    Return:
        list[str] : Elements from periodic table.

    Example:
        "neon" should return ["Ne", "O", "N"]

"""

def get_periodic_spelling(word):
    elements = [
        "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
        "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
        "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
        "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
        "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
        "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
        "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
        "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
        "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
        "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
        "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
        "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
    ]
    
    symbol_map = {s.lower(): s for s in elements}
    
    n = len(word)
    word_lower = word.lower()
    
    memo = {}

    def solve(index):
        if index == n:
            return []
        
        if index in memo:
            return memo[index]
        
        for length in [2, 1]:
            if index + length <= n:
                sub = word_lower[index:index+length]
                if sub in symbol_map:
                    rest = solve(index + length)
                    if rest is not None:
                        result = [symbol_map[sub]] + rest
                        memo[index] = result
                        return result
        
        memo[index] = None
        return None

    result = solve(0)
    return result if result is not None else []

def test_cases():
    assert get_periodic_spelling("neon") == ["Ne", "O", "N"]
    assert get_periodic_spelling("rational") == ["Ra", "Ti", "O", "N", "Al"]
    assert get_periodic_spelling("yarn") == ["Y", "Ar", "N"]
    assert get_periodic_spelling("carbon") in (["C", "Ar", "B", "O", "N"], ["Ca", "Rb", "O", "N"])
    assert get_periodic_spelling("noisy") in (["N", "O", "I", "S", "Y"], ["No", "I", "S", "Y"])
    assert get_periodic_spelling("bicycles") in (["B", "I", "C", "Y", "Cl", "Es"], ["Bi", "C", "Y", "Cl", "Es"])
    assert get_periodic_spelling("optics") in (["O", "P", "Ti", "C", "S"], ["O", "P", "Ti", "Cs"], ["O", "Pt", "I", "C", "S"], ["O", "Pt", "I", "Cs"])
    assert get_periodic_spelling("value") == []

    print("All test cases passed!")

if __name__ == "__main__":
    test_cases()
