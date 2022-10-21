class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if (self.a + self.b) > self.c:
            print('да')
        else:
            print('нет')

triangle = TriangleChecker(2,3,7)
triangle.is_triangle()