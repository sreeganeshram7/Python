class volume_2:
    def __init__(self, r, h):
        self.radius = r
        self.height = h

    def sphere(self):
        print((4 / 3) * 3.14 * pow(self.radius, 3))

    def cylinder(self):
        print(3.14 * (self.radius * self.radius) * self.height)

    def cone(self):
        print((1 / 3) * (3.14) * pow(self.radius, 2) * self.height)


if __name__ == "__main__":
    obj = volume_2(5, 6)
    obj.cone()
