# 06-07-2026 | 06-07-2026


# return only the words that are entirely lowercase
# "hello GOOD world" should return "hello world"

def get_lowercase_words(s):

    return " ".join([word for word in s.split() if word.islower()])
