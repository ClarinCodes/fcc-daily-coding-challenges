#17-03-2026 | 17-03-2026

'''
    Given: years and anniversary milestone names.
    Problem: find the anniversary milestone name with given int(year)
    Return: milestone name
    Example: get_milestone(26) should return "Silver"
'''

def get_milestone(years):
    anniversaries = [
     #(y, label)
      (1, "Paper"),
      (5, "Wood"),
      (10, "Tin"),
      (25, "Silver"),
      (40, "Ruby"),
      (50, "Gold"),
      (60, "Diamond"),
      (70, "Platinum")
    ]
    for y, label in reversed(anniversaries): # we can reverse the list instead of using reversed() here.
        if years >= y:
            return label
    return "Newlyweds"
