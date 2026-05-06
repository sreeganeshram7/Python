class medical:
    def __init__(self, name, wt, ht):
        self.name = name
        self.wt = wt
        self.ht = ht
        self.result = (self.wt / pow(self.ht, 2))

    def bmi(self):
        print('Body Mass Index: ', self.result)


if __name__ == "__main__":
    medical1 = medical('David', 83, 1.85)
    medical1.bmi()
