from collections import Counter

def min_price(counts):
    count = counts[1]
    if (count == 0):
      return counts[1:]
    else:
      a = 1 + [counts[1] - 1] + counts[1:]
      b = counts[1:]


def total(basket):
    counts = list(Counter(basket).values())
    return min_price(counts)

assert total([1]) == 8