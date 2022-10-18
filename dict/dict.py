from random import randint

class Dict:

    def __init__(self):
#        x = input('Введите слово: ')
#        y = input('Введите перевод слова: ')
        self.dict = [["HOUSE", "ДОМ"],
                     ["CAT", "КОШКА"],
                     ["DOG", "СОБАКА"],
                     ["WATER", "ВОДА"],
#                     [x.upper(), y.upper()],
                     ["FLOWER", "ЦВЕТОК"],
                     ["GREEN", "ЗЕЛЁНЫЙ"],
                     ["PEN", "РУЧКА"],
                     ["PENCIL", "КАРАНДАШ"],
                     ["SCHOOL", "ШКОЛА"],
                     ["WORLD", "МИР"],
                     ["DOOR", "ДВЕРЬ"],
                     ["CHAIR", "СТУЛ"],
                     ["BED", "КРОВАТЬ"],
                     ["APPLE", "ЯБЛОКО"],
                     ["TABLE", "СТОЛ"],
                     ["BLACK", "ЧЁРНЫЙ"],
                     ["MOTHER", "МАМА"],
                     ["FATHER", "ПАПА"],
                     ["BAG", "СУМКА"],
                     ["HAND", "РУКА"]]
        self.current_word = randint(0, len(self.dict) - 1)
        self.marker_chars = self.get_marker_chars()
        print(self.marker_chars)

    def get_marker_chars(self):
        ret = []
        for i in range(len(self.dict[self.current_word][0])):
            ret.append(False)
        return ret
