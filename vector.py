import math


class Vector():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"x,y,z = {self.x, self.y, self.z}"

    def __add__(self, other):
        return Vector(
            int(self.x) + int(other.x),
            int(self.y) + int(other.y),
            int(self.z) + int(other.z))

    def __sub__(self, other):
        return Vector(
            int(self.x) - int(other.x),
            int(self.y) - int(other.y),
            int(self.y) - int(other.y))

    def __mul__(self, k):
        return Vector(
            int(self.x) * int(k),
            int(self.y) * int(k),
            int(self.z) * int(k))

    def __truediv__(self, k):
        return Vector(
            int(self.x) / int(k),
            int(self.y) / int(k),
            int(self.z) / int(k))

    def __abs__(self):
        return math.sqrt(int(self.x)**2 + int(self.y)**2 + int(self.z)**2)

    def normalize(self):
        return Vector(
            int(self.x) / abs(self),
            int(self.y) / abs(self),
            int(self.z) / abs(self))

    def __repr__(self):
        return 'Vector({:.3f}, {:.3f}, {:.3f})'.format(float(self.x),
                                                       float(self.y),
                                                       float(self.z))

    __str__ = __repr__


def main():
    x1 = input("input x1:")
    y1 = input("input y1:")
    z1 = input("input z1:")
    x2 = input("input x2:")
    y2 = input("input y2:")
    z2 = input("input z2:")
    k = input("input k:")
    v1 = Vector(x1, y1, z1)
    v2 = Vector(x2, y2, z2)
    print("输入向量1：", v1)
    print("输入向量2：", v2)
    print("向量加法：", v1 + v2)
    print("向量减法：", v1 - v2)
    print("向量乘法：", v1 * k)
    print("向量除法：", v1 / k)
    print("向量取模： {:.3f}".format(abs(v1)))
    print("向量标准化：", v1.normalize())


if __name__ == '__main__':
    main()
