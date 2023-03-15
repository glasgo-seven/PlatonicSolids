from matrix import Matrix

class Vector:
	def __init__(self, _x : float, _y : float, _z : float) -> None:
		self.x = _x
		self.y = _y
		self.z = _z
		self.V = (_x, _y, _z)

	def __add__(self, _V):
		return Vector(self.x + _V.x, self.y + _V.y, self.z + _V.z)
	
	def __radd__(self, _V):
		return self.__add__(_V)
	
	def __sub__(self, _V):
		return Vector(self.x - _V.x, self.y - _V.y, self.z - _V.z)
	
	def __rsub__(self, _V):
		return self.__sub__(_V)
	
	def __mul__(self, _V):
		return self.x * _V.x + self.y * _V.y + self.z * _V.z
	
	def __rmul__(self, _V):
		return self.__mul__(_V)
	
	def length(self) -> float:
		return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1 / 2)
	
	def to_matrix(self) -> Matrix:
		return Matrix([[self.x], [self.y], [self.z]])
	
	def __repr__(self) -> str:
		return f'(\n    x: {self.x},\n    y: {self.y},\n    z: {self.z}\n)'


if __name__ == '__main__':
	a = Vector(1, 2, 3)
	b = Vector(4, -2, 3)
	print(a + b)

