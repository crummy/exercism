from collections import defaultdict
import re


def is_isogram(string: str) -> bool:
    letter_counts: dict[str:int] = defaultdict(int)
    letters: str = re.sub(r"[^a-z]*", "", string.lower())
    for letter in letters:
        letter_counts[letter] += 1
    return all(count < 2 for count in letter_counts.values())
