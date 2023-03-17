from matrix import Matrix, Zero3_Vector

def load_triangle(_position : tuple[float, float, float], _edge : float) -> tuple[list[Matrix], list[tuple[int]], list[tuple[int]]]:
	m = (_edge ** 2 * 3 / 4) ** (1 / 2)
	vertices = [
		Matrix(
			_position,
			_is_vector=True),
		Matrix(
			(_position[0] + _edge, _position[1], _position[2]),
			_is_vector=True),
		Matrix(
			(_position[0] + _edge / 2, _position[1] + m, _position[2]),
			_is_vector=True),
	]
	edges = [
		(0, 1),
		(1, 2),
		(2, 0),
	]
	surfaces = [
		(0, 1, 2)
	]
	return (vertices, edges, surfaces)

def load_square():
	pass

def load_cube():
	pass

def load_tetra():
	pass

SHAPES = {
	'Triangle'	:	load_triangle,
	'Square'	:	load_square,
	'Cube'		:	load_cube,
	'Tetra'		:	load_tetra,
}

class Shape:
	def __init__(self, _position : Matrix = Zero3_Vector, _edge : float = 1, _shape_type = None) -> None:
		self.position	: Matrix	= _position
		self.edge		: float		= _edge

		self.vertices	: list[Matrix]
		self.edges		: list[tuple[int]]
		self.surfaces	: list[tuple[int]]

		shape_data = _shape_type(_position.V, _edge)
		self.vertices = shape_data[0]
		self.edges = shape_data[1]
		self.surfaces = shape_data[2]

	def __repr__(self) -> str:
		return f'pos: {self.position}\nedge: {self.edge}\nv: {self.vertices}\ne: {self.edges}\ns: {self.surfaces}\n'

if __name__ == '__main__':
	triangle = Shape(_shape_type=SHAPES['Triangle'])
	print(triangle)

