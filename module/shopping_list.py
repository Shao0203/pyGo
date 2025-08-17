class ShoppingList:
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    def get_item_count(self):
        return len(self.shopping_list)

    def get_total_price(self):
        total_price = 0
        for price in self.shopping_list.values():
            total_price += price
        return total_price


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def letter_count(self):
        return len(self.sentence)

    def word_count(self):
        return len(self.sentence.split(' '))

    def uppertize(self):
        return self.sentence.upper()
