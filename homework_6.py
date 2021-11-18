class Hm: 
    def __init__(self): 
        self.x = 0
        self.y = 0
 
    def meaning(self): 
        numbers = [2, 5, 7, 9, 12, 35, 15, 67] 
 
        my_number = 40 
        for self.x in numbers: 
            for self.y in range(numbers.index(self.x) + 1, len(numbers)): 
                if self.x + numbers[self.y] == my_number: 
                    print([numbers.index(self.x), self.y]) 
 
 
h = Hm() 
h.meaning()
