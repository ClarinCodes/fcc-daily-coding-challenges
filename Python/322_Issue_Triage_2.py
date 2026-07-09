# 09-07-2026 | 09-07-2026

"""
Problem:
    Automatically assign or update labels for a software issue based on its title and current labels.
    The function follows specific rules to decide which labels to add, remove, or keep.
    It helps organize bugs, features, and security issues efficiently.

        Rules:

            1. If the issue has NO labels yet:
                - Add "bug" and "needs triage" if the title mentions "error" or "bug".
                - Add "enhancement" and "discussing" if the title mentions "feature" or "add".

            2. If the issue already has labels:
                - If it has "needs triage" AND the title says "simple" or "easy":
                    Remove "needs triage" and add "good first issue".
                - If it has "discussing" AND the title says "planned" or "next":
                    Remove "discussing" and add "on the roadmap".
                - If it still has "needs triage" or "discussing" after checking the above:
                    Remove those labels and add "help wanted" instead.

            3. Security Check (applies in all cases):
                - If the title mentions "security", always add the "critical" label.

Args:
    title (str): The title of the issue written in plain English.
    labels (list[str]): A list of labels currently assigned to the issue. Can be empty.

Return:
    list[str]: An updated list of labels that correctly reflect the issue's status and type.
"""


def triage_issue(title, labels):

    title_lower = title.lower()
    title_words = set(title_lower.split())
    labels_set = set(labels)
    result = set(labels)

    if not labels:
        if "error" in title_words or "bug" in title_words:
            result = {"bug", "needs triage"}
        elif "feature" in title_words or "add" in title_words:
            result = {"enhancement", "discussing"}

        if "security" in title_words:
            result.add("critical")
        return sorted(result)

    if "needs triage" in labels_set and ("simple" in title_words or "easy" in title_words):
        result.discard("needs triage")
        result.add("good first issue")

    if "discussing" in labels_set and ("planned" in title_words or "next" in title_words):
        result.discard("discussing")
        result.add("on the roadmap")

    if "needs triage" in result or "discussing" in result:
        result.discard("needs triage")
        result.discard("discussing")
        result.add("help wanted")

    if "security" in title_words:
        result.add("critical")

    return sorted(result)


def test_cases():
    assert triage_issue("app crashes with error", []) == ["bug", "needs triage"]
    assert triage_issue("app crashes with error", ["bug", "needs triage"]) == ["bug", "help wanted"]
    assert triage_issue("add dark mode", []) == ["discussing", "enhancement"]
    assert triage_issue("add dark mode", ["enhancement", "discussing"]) == ["enhancement", "help wanted"]
    assert set(triage_issue("xss security bug", [])) == {"bug", "critical", "needs triage"}
    assert triage_issue("security vulnerability in auth", []) == ["critical"]
    assert set(triage_issue("easy a11y fix", ["bug", "needs triage"])) == {"bug", "good first issue"}
    assert set(triage_issue("planned api migration", ["enhancement", "discussing"])) == {"enhancement", "on the roadmap"}
    assert set(triage_issue("improve security", ["enhancement", "discussing"])) == {"enhancement", "help wanted", "critical"}

    print("All tests passed!")


if __name__ == "__main__":
    test_cases()
