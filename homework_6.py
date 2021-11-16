class Hm:
    def meaning(self):
        numbers = [2, 5, 7, 9, 12, 35, 15, 67]
        my_number = 40
        for first in numbers:
            for second in numbers:
                if first+second == my_number:
                    print([first, second])

h = Hm()
h.meaning()
