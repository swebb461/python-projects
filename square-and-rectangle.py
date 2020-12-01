
class Shape:
    def what_am_i(self):
            print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, w, l):
	    self.width = w
	    self.length = l
    def calculate_perimeter(self):
	    return self.width * 2 + self.length * 2
    pass

class Square(Shape):
    def __init__(self, side):
            self.side = side
    def calculate_length(self):
            return self.side * 4
    def change_size(self, new_size):
            self.side += new_size
    pass
a_square = Square(100)
a_square.what_am_i()
print(a_square.calculate_length())
