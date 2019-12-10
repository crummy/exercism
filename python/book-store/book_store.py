from collections import Counter
from typing import List, Set

book_price = 8
discounts = {1: 100, 2: 95, 3: 90, 4: 80, 5: 75}


def min_price(books: List[int], books_in_set: List[int]) -> float:
    if len(books) == 0:
        return cost(books_in_set)
    if set(books).issubset(set(books_in_set)):  # no more unique books to add to the set
        return cost(books_in_set) + min_price(books, [])
    book: int = books[0]
    remaining_books: List[int] = books[1:]
    if book in books_in_set:
        print(f"already have {book} in set {books_in_set}. remaining: {remaining_books}")
        return min_price(remaining_books + [book], books_in_set)  # put book at end to pick up later
    else:
        continue_set = min_price(remaining_books, books_in_set + [book])
        end_set = cost(books_in_set + [book]) + min_price(remaining_books, [])
        if continue_set < end_set:
            return continue_set
        else:
            print(f"found cheap set: {books_in_set} costs {end_set}, remaining: {books}")
            return end_set


def cost(books: List[int]) -> float:
    if len(books) == 0:
        return 0
    discount = discounts[len(books)]
    return len(books) * book_price * discount


def total(basket: List[int]) -> float:
    return min_price(basket, [])
