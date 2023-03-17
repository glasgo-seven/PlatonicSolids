class Matrix:
	def __init__(self, _content : list[list[float]] | tuple[float], _is_vector : bool = False) -> None:
		if _is_vector:
			self.V = _content
			self.m = 1
			self.n = len(self.V)
		else:
			self.M = _content
			self.m = len(self.M)
			self.n = len(self.M[0])
		self.is_vector = _is_vector
	
	def mul(self, v1, v2):
		return sum([v1[i] * v2[i] for i in range(len(v1))])

	def __mul__(self, _mul):
		if self.is_vector and _mul.is_vector and self.n == _mul.n:
			return self.mul(self.V, _mul.V)
		elif not self.is_vector and _mul.is_vector:
			return Matrix(tuple([self.mul(row, _mul.V) for row in self.M]), True)
		
	def __repr__(self) -> str:
		if self.is_vector:
			return self.V.__repr__()
		else:
			ret = '[\n'
			for row in self.M:
				ret += f'    {row}\n'
			ret += ']'
			return ret
		

Identity3_Matrix = Matrix(
	[
		[1, 0, 0],
		[0, 1, 0],
		[0, 0, 1]
	]
)

Zero3_Matrix = Matrix(
	[
		[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]
	]
)

Zero3_Vector = Matrix((0, 0, 0), True)

M = {
	'T'		: Zero3_Matrix,
	'Ro_x'	: Zero3_Matrix,
	'Ro_y'	: Zero3_Matrix,
	'Ro_z'	: Zero3_Matrix,
	'Sc'	: Zero3_Matrix,
	'Re_x'	: Zero3_Matrix,
	'Re_y'	: Zero3_Matrix,
	'Re_z'	: Zero3_Matrix
}


if __name__ == '__main__':
	matrix = [
		[1, 2],
		[2, 4]
	]
	vector = (0, 2)
	vector_2 = (1, 4)

	M = Matrix(matrix)
	V = Matrix(vector, _is_vector=True)
	V2 = Matrix(vector_2, _is_vector=True)

	print(M)
	print(V)
	print(V2)
	print()
	print(M * V)
	print(V * V2)

