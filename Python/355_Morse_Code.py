# 31-07-2026 | 31-07-2026

def decode_morse(code):
    morse = {
        ".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E",
        "..-.":"F","--.":"G","....":"H","..":"I",".---":"J",
        "-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",
        ".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T",
        "..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y",
        "--..":"Z"
    }

    result = []

    for word in code.split("   "):
        text = ""
        for letter in word.split():
            text += morse[letter]
        result.append(text)

    return " ".join(result)
