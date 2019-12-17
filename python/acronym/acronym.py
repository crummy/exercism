import re


def abbreviate(words: str) -> str:
    result = ""
    for word in re.split(r"[ -]", words.replace("_", "")):
        if len(word) > 0:
            letter = word[0]
            if letter.isalpha():
                result += letter.upper()
    return result
