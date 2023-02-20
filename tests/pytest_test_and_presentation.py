# pytest - test and presentation how to use
#

# use classes & methods
class Square:
	def __init__(self, length:int, width:int):
		self.length = length
		self.width = width
	def calculate_surface(self):
		return self.length*self.width
	def some_calculation(self):
		return (1+self.length)*(1+self.width)

# how to use pytes
from unittest import TestCase

class SquaresTesting(TestCase):
	def test_surface(self):
		square=Square(10,20)
		self.assertTrue(square.calculate_surface()==10*20)
		square=Square(20,30)
		self.assertTrue(square.calculate_surface()==20*30)
	def test_some_calculation(self):
		square=Square(10,20)
		self.assertTrue(square.some_calculation()==(1+10)*(1+20))

if __name__ == '__main__':
	square=Square(10,20)
	print(f"square surface={square.calculate_surface()} calculation={square.some_calculation()}")
