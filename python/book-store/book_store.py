from collections import Counter
from typing import List, Set

base_book_price = 8
discounts = {1: 100, 2: 95, 3: 90, 4: 80, 5: 75}


def min_price(books: List[int], books_in_set: List[int]) -> float:
    assert len(books_in_set) == len(set(books_in_set))  # no dupes

    no_more_books = len(books) == 0
    if no_more_books:
        return cost(books_in_set)

    no_more_unique_books = set(books).issubset(set(books_in_set))
    if no_more_unique_books:
        return cost(books_in_set) + min_price(books, [])

    book: int = books[0]
    remaining_books: List[int] = books[1:]

    if book in books_in_set:  # skip book, put at end of list to pick up later
        return min_price(remaining_books + [book], books_in_set)
    else:
        price_with_book_added = min_price(remaining_books, books_in_set + [book])
        price_with_book_skipped = cost(books_in_set + [book]) + min_price(remaining_books, [])
        print(f"is {price_with_book_added} < {price_with_book_skipped} for {remaining_books} and {books_in_set + [book]}?")
        if price_with_book_added < price_with_book_skipped:
            return price_with_book_added
        else:
            return price_with_book_skipped


def cost(books: List[int]) -> float:
    books_in_set = len(books)
    if books_in_set == 0:
        return 0
    discount = discounts[books_in_set]
    value = books_in_set * base_book_price * discount
    return value


def total(basket: List[int]) -> float:
    return min_price(basket, [])
