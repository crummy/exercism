from collections import Counter
import re

def count_words(sentence):
    words = re.split(r"[\s,_]+", strip(r"\W", sentence.lower()))
    stripped = list(map(lambda word: strip(r"\W", word), words))
    return Counter(stripped)

def strip(regex, word):
    stripped = re.sub(f"^{regex}+", "", word)
    stripped = re.sub(f"{regex}+$", "", stripped)
    return stripped