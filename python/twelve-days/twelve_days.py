from typing import List


def recite(start_verse, end_verse) -> List[str]:
    return [recite_day(verse) for verse in range(start_verse, end_verse + 1)]


def recite_day(verse) -> str:
    if verse == 1:
        gifts = "a Partridge in a Pear Tree."
    else:
        gifts = items(verse)
    return f"On the {nth[verse]} day of Christmas my true love gave to me: " + gifts


def items(day) -> str:
    if day == 0:
        return ""
    return gift[day] + items(day - 1)


nth = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth",
       7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth", 11: "eleventh", 12: "twelfth"}
gift = {
    12: "twelve Drummers Drumming, ",
    11: "eleven Pipers Piping, ",
    10: "ten Lords-a-Leaping, ",
    9: "nine Ladies Dancing, ",
    8: "eight Maids-a-Milking, ",
    7: "seven Swans-a-Swimming, ",
    6: "six Geese-a-Laying, ",
    5: "five Gold Rings, ",
    4: "four Calling Birds, ",
    3: "three French Hens, ",
    2: "two Turtle Doves, ",
    1: "and a Partridge in a Pear Tree."
}

print(recite(1, 3))
