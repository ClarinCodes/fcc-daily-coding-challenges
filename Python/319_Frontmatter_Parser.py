# 25-06-2026 | 25-06-2026

"""
    Problem:
        Parse a frontmatter block wrapped in --- delimiters and return a
        dictionary containing the key-value pairs. Values should be converted
        to their appropriate types (bool, int, float, or str).

    Args:
        text (str): A string containing the frontmatter block.

    Return:
        dict: A dictionary of parsed key-value pairs.
"""

def parse_frontmatter(text):
    result = {}

    for line in text.split("\n")[1:-1]:
        key, value = line.split(":", 1)
        value = value.strip()

        if value == "true":
            result[key] = True
        elif value == "false":
            result[key] = False
        else:
            try:
                result[key] = float(value) if "." in value else int(value)
            except ValueError:
                result[key] = value

    return result


def test_cases():
    assert parse_frontmatter(
        "---\ntitle: My Post\ndraft: false\nviews: 100\n---"
    ) == {
        "title": "My Post",
        "draft": False,
        "views": 100,
    }

    assert parse_frontmatter(
        "---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---"
    ) == {
        "id": "6a174db57256a112f932195c",
        "title": "My Book",
        "locale": "en",
        "wordCount": 10000,
        "published": False,
    }

    assert parse_frontmatter(
        "---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---"
    ) == {
        "version": "1.0.0",
        "url": "https://example.com",
        "private": True,
    }

    assert parse_frontmatter(
        "---\nrating: 4.5\nprice: 9.99\n---"
    ) == {
        "rating": 4.5,
        "price": 9.99,
    }

    print("All tests passed!")


if __name__ == "__main__":
    test_cases()
