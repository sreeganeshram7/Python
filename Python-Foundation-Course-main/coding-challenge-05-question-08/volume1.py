class volume_1:
    def __init__(self, l, b, h):
        self.length = l
        self.breadth = b
        self.height = h

    def cube(self):
        print(pow(self.length, 3))

    def cuboid(self):
        print(self.length * self.breadth * self.height)


if __name__ == "__main__":
    obj = volume_1(2, 3, 4)
    obj.cube()
