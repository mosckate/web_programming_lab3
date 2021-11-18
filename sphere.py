from math import pi
class Sphere:
    def __init__(self, x=0, y=0, z=0, r=1):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def get_volume_(self):
        return 4 / 3 * pi * (self.r ** 3)

    def get_square_(self):
        return 4 * pi * (self.r ** 2)

    def get_radius_(self):
        return self.r

    def get_center_(self):
        return (self.x, self.y, self.z)

    def set_radius_(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        if self.x >= x and self.y >= y and self.z >= z:
            return True
        else:
            return False