import re

class Luhn:
    digits_regex = re.compile(r'^\d+$')

    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        num_without_spaces = self.card_num.replace(" ", "")
        if not self.digits_regex.search(num_without_spaces):
            return False
        digits_list = list(num_without_spaces)
        if len(digits_list) <= 1:
            return False
        
        card_num_doubled = self.luhn_double(digits_list)

        checksum = sum(card_num_doubled)

        return checksum % 10 == 0


    def luhn_double(self, digits):
        doubled_last = True
        digits.reverse()
        for i in range(0, len(digits)):
            if not doubled_last:
                doubled = int(digits[i]) * 2
                if (doubled >= 10):
                    doubled = doubled - 9
                digits[i] = doubled
            else:
                digits[i] = int(digits[i])
            doubled_last = not doubled_last
        digits.reverse()
        return digits