class Matrix:
	def __init__(self, _content : list[list[float]]) -> None:
		self.content = _content
		self.m = len(_content)
		self.n = len(_content[0])

	def __add__(self, _add):
		if type(_add) == int or type(_add) == float:
			content = []
			for line in self.content:
				row = []
				for cell in line:
					row.append(cell + _add)
				content.append(row)
			return Matrix(content)
		
		elif type(_add) == Matrix:
			if self.m == _add.m and self.n == _add.n:
				content = []
				for m in range(self.m):
					row = []
					for n in range(self.n):
						row.append(self.content[m][n] + _add.content[m][n])
					content.append(row)
				return Matrix(content)

	def __radd__(self, _add):
		return self.__add__(_add)


	def __mul__(self, _mul):
		if type(_mul) == int or type(_mul) == float:
			content = []
			for line in self.content:
				row = []
				for cell in line:
					row.append(cell * _mul)
				content.append(row)
			return Matrix(content)

		elif type(_mul) == Matrix:
			if self.n == _mul.m:
				_mult = _mul.T()
				content = []
				# for m in range(self.m):
				# 	row = []
				# 	x = 0
				# 	for n in range(self.n):
				# 		x += self.content[m][n] * _mul.content[n][m]
				def mul_vector(v1, v2):
					if len(v1) == len(v2):
						mul = 0
						for i in range(len(v1)):
							mul += v1[i] * v2[i]
						return mul
				
				for row_a in self.content:
					row = []
					for row_b in _mul.content:
						row.append(mul_vector(row_a, row_b))
					content.append(row)
				return Matrix(content)

	def __rmul__(self, _mul):
		return self.__mul__(_mul)


	def __sub__(self, _sub):
		if type(_sub) == int or type(_sub) == float:
			return self.__add__(-_sub)
		elif type(_sub) == Matrix:
			return self.__add__(_sub.__mul__(-1))
	
	def __rsub__(self, _sub):
		return self.__sub__(_sub)

	def T(self):
		content = [[0 for _ in range(self.m)] for _ in range(self.n)]
		for m in range(self.m):
			for n in range(self.n):
				content[n][m] = self.content[m][n]
		return Matrix(content)

	def det(self, M = None) -> float:
		if M is None:
			M = self.content.copy()
			m = self.m
			n = self.n
		else:
			m = len(M)
			n = len(M[0])

		if m == n:
			if m * n == 4:
				return M[0][0] * M[1][1] - M[0][1] * M[1][0]
			else:
				detM = 0
				for i in range(n):
					sign = 1 if i % 2 == 0 else -1
					M_ = []
					for row in M[1:]:
						M_.append(row[:i] + row[i+1:])
					detM += sign * M[0][i] * self.det(M_)
				return detM
		
		return 0

	def to_vector(self):
		if self.m == 1 and self.n == 3:
			return self.content[0]

	def __repr__(self) -> str:
		ret = '[\n'
		for line in self.content:
			ret += f'  {line}\n'
		ret += ']'
		return ret



def add_n(_matrix : list[list], _n : float) -> list[list]:
	for line in _matrix :
		row = []
		for cell in line :
			row.append(cell + _n)
		yield row

def add_n1(_matrix : list[list], _n : float) -> list[list]:
	new_matrix = []
	for line in _matrix :
		row = []
		for cell in line :
			row.append(cell + _n)
		new_matrix.append(row)
	return new_matrix

def add_n2(_matrix : list[list], _n : float) -> list[list]:
	for m in range(len(_matrix)) :
		for n in range(len(_matrix[m])) :
			_matrix[m][n] += _n
	return _matrix

def add(_matrix_A : list[list], _matrix_B : list[list]) -> list[list]:
	pass


if __name__ == '__main__':
	matrix_A = [
		[1, 2, 3],
		[4, 5, 6]
	]
	matrix_B = [
		[1, 2],
		[3, 4],
		[5, 6]
	]
	A = Matrix(matrix_A)
	B = Matrix(matrix_B)
	print(A)
	print(B)
	print(A * B)

	# import timeit

	# print()
	# print([*add_n(matrix, 2)])
	# print(timeit.timeit("add_n(matrix, 2)", number=10000))

	# print()
	# print(add_n1(matrix, 2))
	# print(timeit.timeit("add_n1(matrix, 2)", number=10000))

	# print()
	# print(add_n2(matrix, 2))
	# print(timeit.timeit("add_n2(matrix, 2)", number=10000))
