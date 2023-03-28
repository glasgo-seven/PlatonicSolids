# from vector import Vector
# from engine_3d import vector

class Matrix:
	def __init__(self, _content : list[list[float]]) -> None:
		self.content : list[list[float]] = _content
		self.m : int = len(_content)
		self.n : int = len(_content[0])

	def __add__(self, _add):
		if type(_add) is int or type(_add) is float:
			content = []
			for line in self.content:
				row = []
				for cell in line:
					row.append(cell + _add)
				content.append(row)
			return Matrix(content)
		
		elif type(_add) is Matrix:
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
		if type(_mul) is int or type(_mul) is float:
			content = []
			for line in self.content:
				row = []
				for cell in line:
					row.append(cell * _mul)
				content.append(row)
			return Matrix(content)
		elif type(_mul) is Matrix:
			content = []
			for line_a in self.content:
				row = []
				for line_b in _mul.T().content:
					def mul_vectors(v1, v2):
						# return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]
						s = sum([v1[i] * v2[i] for i in range(len(line_a))])
						print(v1, v2, s)
						return s
					row.append(mul_vectors(line_a, line_b))
				content.append(row)
			return Matrix(content)

		# elif type(_mul) is Matrix:
		# 	if self.n == _mul.m:
		# 		_mult = _mul.T()
		# 		content = []
		# 		def mul_vector(v1, v2):
		# 			if len(v1) == len(v2):
		# 				mul = 0
		# 				for i in range(len(v1)):
		# 					mul += v1[i] * v2[i]
		# 				return mul
				
		# 		for row_a in self.content:
		# 			row = []
		# 			for row_b in _mul.content:
		# 				row.append(mul_vector(row_a, row_b))
		# 			content.append(row)
		# 		return Matrix(content)

	def __rmul__(self, _mul):
		return self.__mul__(_mul)


	def __sub__(self, _sub):
		if type(_sub) == int or type(_sub) == float:
			return self.__add__(-_sub)
		elif type(_sub) == Matrix:
			return self.__add__(_sub.__mul__(-1))
	
	# def __rsub__(self, _sub):
	# 	return self.__sub__(_sub)


	def __truediv__(self, _div):
		return self.__mul__(1 / _div)
	
	def __rtruediv__(self, _div):
		return self.__truediv__(_div)


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


	def to_vector_content(self) -> list[float]:
		if self.m == 1 and self.n == 3:
			return self.content[0]
		t = self.T()
		if t.m == 1 and t.n == 3:
			return self.content[0]

	def __repr__(self) -> str:
		ret = '[\n'
		for line in self.content:
			ret += f'  {line}\n'
		ret += ']'
		return ret


if __name__ == '__main__':
	print(Matrix([[0,1], [1,2]]) * Matrix([[1], [2]]))
