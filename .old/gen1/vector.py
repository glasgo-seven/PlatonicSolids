# from matrix import Matrix
# from engine_3d import matrix

class Vector:
	def __init__(self, _x : float = 0, _y : float = 0, _z : float = 0, _from_matrix_content : list[float] = None) -> None:
		self.x : float
		self.y : float
		self.z : float
		
		if _from_matrix_content is not None:
			self.x = _from_matrix_content[0]
			self.y = _from_matrix_content[1]
			self.z = _from_matrix_content[2]
		else:
			self.x = _x
			self.y = _y
			self.z = _z
		
		self.V : tuple[float] = (_x, _y, _z)

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
	
	def to_matrix_content(self) -> list[list[float]]:
		return [[self.x], [self.y], [self.z]]
	
	def __repr__(self) -> str:
		return f'(\n    x: {self.x},\n    y: {self.y},\n    z: {self.z}\n)'


if __name__ == '__main__':
	a = Vector(1, 2, 3)
	b = Vector(4, -2, 3)
	print(a + b)

