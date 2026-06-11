# 11-06-2026 | 11-06-2026

"""

    Problem:
    Given a list of ideas, each containing:
    [idea_name, optimistic_estimate, realistic_estimate, pessimistic_estimate],
    compute the expected completion time using:
    
    expected = ((optimistic + 4 * realistic + pessimistic) / 6) * len(idea_name)

    Args:
        ideas (List[List]): A 2D list where each inner list contains:
            - idea_name (str)
            - optimistic estimate (int)
            - realistic estimate (int)
            - pessimistic estimate (int)

    Return:
        List[str]: Idea names sorted by expected completion time (ascending).
    
"""

def analyze_ideas(ideas):
    estimated = {}

    for idea in ideas:

        name = idea[0]
        optimistic = idea[1]
        realistic = idea[2]
        pessimistic = idea[3]

        expected = ((optimistic + 4 * realistic + pessimistic) / 6) * len(name)
        estimated[name] = expected

    sorted_items = sorted(estimated.items(), key=lambda item: item[1])

    sorted_names = []
    for name, _ in sorted_items:
        sorted_names.append(name)

    return sorted_names

 def test_cases():
    assert analyze_ideas([
        ["Add logging", 2, 5, 15],
        ["SEO optimization", 4, 8, 20],
        ["Fix bug", 1, 3, 5]
    ]) == ["Fix bug", "Add logging", "SEO optimization"]

    assert analyze_ideas([
        ["Dark mode", 1, 3, 8],
        ["Real-time collaboration feature", 6, 12, 20],
        ["Add tooltip", 1, 2, 4]
    ]) == ["Add tooltip", "Dark mode", "Real-time collaboration feature"]

    assert analyze_ideas([
        ["Update user profile page", 3, 7, 14],
        ["Add pagination", 2, 5, 10],
        ["Add tags", 2, 3, 6],
        ["Fix login bug", 1, 4, 8]
    ]) == ["Add tags", "Fix login bug", "Add pagination", "Update user profile page"]

    assert analyze_ideas([
        ["Migrate database", 14, 25, 40],
        ["Add chat assistant", 8, 15, 24],
        ["Redesign onboarding flow", 3, 7, 13],
        ["Add language support", 6, 11, 18]
    ]) == ["Redesign onboarding flow", "Add language support", "Add chat assistant", "Migrate database"]

    print("All test cases passed!")

if __name__ == "__main__":
    test_cases()
