from random import randint

from OpenGL.GL import *

from matrix import Matrix, Zero3_Vector

def generate_colors():
	colors = []
	for z in [a / 100 for a in range(100)]:
		for y in [a / 100 for a in range(100)]:
			for x in [a / 100 for a in range(100)]:
				if x**2 + y**2 + z**2 == 0.25:
					colors.append((x, y, z))
	return colors

COLOR_CIRCLE = generate_colors()
COLOR_CIRCLE_LEN = len(COLOR_CIRCLE) - 1

COLORS = {
	#				 r g b
	'black'		:	(0,0,0),
	'blue'		:	(0,0,1),
	'green'		:	(0,1,0),
	'cian'		:	(0,1,1),
	'red'		:	(1,0,0),
	'purple'	:	(1,0,1),
	# 'yellow'	:	(1,1,0),
	'yellow'	:	(1,0.5,0),
	'white'		:	(1,1,1)
}

def load_axises(_position : tuple[float, float, float], _edge : float) -> tuple[list[Matrix], list[tuple[int]], list[tuple[int]], list[tuple[float, float, float]]]:
	gl_mode = GL_LINES
	vertices = [
		Matrix(_position, _is_vector = True),

		Matrix((_position[0] + _edge, _position[1], _position[2]), _is_vector = True),
		Matrix((_position[0] - _edge, _position[1], _position[2]), _is_vector = True),

		Matrix((_position[0], _position[1] + _edge, _position[2]), _is_vector = True),
		Matrix((_position[0], _position[1] - _edge, _position[2]), _is_vector = True),

		Matrix((_position[0], _position[1], _position[2] + _edge), _is_vector = True),
		Matrix((_position[0], _position[1], _position[2] - _edge), _is_vector = True)
	]
	edges = [
		(1,2),
		(3,4),
		(5,6)
	]
	surfaces = None
	colors = [
		COLORS['red'],
		COLORS['green'],
		COLORS['blue']
	]
	return (vertices, edges, surfaces, colors, gl_mode)

def load_point(_position : tuple[float, float, float], _edge : float) -> tuple[list[Matrix], list[tuple[int]], list[tuple[int]], list[tuple[float, float, float]]]:
	gl_mode = GL_POINTS
	vertices = [
		Matrix(_position, _is_vector = True)
	]
	edges = None
	surfaces = None
	colors = None
	return (vertices, edges, surfaces, colors, gl_mode)

def load_triangle(_position : tuple[float, float, float], _edge : float) -> tuple[list[Matrix], list[tuple[int]], list[tuple[int]]]:
	m = (_edge ** 2 * 3 / 4) ** (1 / 2)
	gl_mode = GL_TRIANGLES
	vertices = [
		Matrix(
			_position,
			_is_vector=True),
		Matrix(
			(_position[0] + _edge, 
			_position[1], _position[2]),
			_is_vector=True),
		Matrix(
			(_position[0] + _edge / 2, _position[1] + m, _position[2]),
			_is_vector=True)
	]
	edges = [
		(0, 1),
		(1, 2),
		(2, 0)
	]
	surfaces = [
		(0, 1, 2)
	]
	colors = [
		COLORS['white']
	]
	return (vertices, edges, surfaces, colors, gl_mode)

def load_square(_position : tuple[float, float, float], _edge : float) -> tuple[list[Matrix], list[tuple[int]], list[tuple[int]]]:
	gl_mode = GL_QUADS
	vertices = [
		Matrix(
			_position,
			_is_vector=True),
		Matrix(
			(_position[0] + _edge, _position[1], _position[2]),
			_is_vector=True),
		Matrix(
			(_position[0] + _edge, _position[1] + _edge, _position[2]),
			_is_vector=True),
		Matrix(
			(_position[0], _position[1] + _edge, _position[2]),
			_is_vector=True)
	]
	edges = [
		# (0, 1),
		# (1, 2),
		# (2, 0),

		# (0, 2),
		# (2, 3),
		# (3, 0),

		(0, 1),
		(1, 2),
		(2, 3),
		(3, 0)
	]
	surfaces = [
		# (0, 1, 2),
		# (0, 2, 3),
		(0, 1, 2, 3)
	]
	colors = [
		# COLORS['red'],
		# COLORS['blue'],
		# COLORS['purple']
		COLOR_CIRCLE[randint(0, COLOR_CIRCLE_LEN)],
	]
	return (vertices, edges, surfaces, colors, gl_mode)

def load_cube(_position : tuple[float, float, float], _edge : float) -> tuple[list[Matrix], list[tuple[int]], list[tuple[int]]]:
	gl_mode = GL_TRIANGLES
	vertices = [
		Matrix(
			(_position[0], _position[1], _position[2]),
			_is_vector=True),
		Matrix(
			(_position[0] + _edge, _position[1], _position[2]),
			_is_vector=True),
		Matrix(
			(_position[0] + _edge, _position[1] + _edge, _position[2]),
			_is_vector=True),
		Matrix(
			(_position[0], _position[1] + _edge, _position[2]),
			_is_vector=True),

		Matrix(
			(_position[0], _position[1], _position[2] + _edge),
			_is_vector=True),
		Matrix(
			(_position[0] + _edge, _position[1], _position[2] + _edge),
			_is_vector=True),
		Matrix(
			(_position[0] + _edge, _position[1] + _edge, _position[2] + _edge),
			_is_vector=True),
		Matrix(
			(_position[0], _position[1] + _edge, _position[2] + _edge),
			_is_vector=True),
	]
	edges = [
		(0, 1),
		(1, 2),
		(2, 0),
		(0, 3),
		(3, 2),

		(4, 5),
		(5, 6),
		(6, 4),
		(4, 7),
		(7, 6),
		
		(0, 4),
		(1, 5),
		(2, 6),
		(3, 7),
		
		(4, 3),
		(5, 2),
	]
	'''
			3			2
		0			1

			7			6
		4			5
	'''
	surfaces = [
		
		(0, 1, 2),
		(0, 3, 2),
		(4, 5, 6),
		(4, 7, 6),

		(4, 5, 1),
		(4, 0, 1),
		(7, 6, 2),
		(7, 3, 2),

		(4, 7, 3),
		(4, 0, 3),
		(5, 6, 2),
		(5, 1, 2),

		
		# (0, 1, 2, 3),
		# (4, 5, 6, 7),

		# (0, 1, 5, 4),
		# (2, 3, 7, 6),

		# (0, 3, 7, 4),
		# (1, 2, 6, 5),
	]
	colors = [
		# COLORS['red'],
		# COLORS['blue'],
		# COLORS['purple']

		# COLORS['blue'],
		# COLORS['green'],
		# COLORS['green'],
		# COLORS['blue'],

		# COLORS['cian'],
		# COLORS['red'],
		# COLORS['red'],
		# COLORS['cian'],

		# COLORS['purple'],
		# COLORS['yellow'],
		# COLORS['yellow'],
		# COLORS['purple'],

		COLORS['yellow'],
		COLORS['yellow'],
		COLORS['yellow'],
		COLORS['yellow'],
		COLORS['yellow'],
		COLORS['yellow'],
		COLORS['yellow'],
		COLORS['yellow'],
		COLORS['yellow'],
		COLORS['yellow'],
		COLORS['yellow'],
		COLORS['yellow'],


	]
	return (vertices, edges, surfaces, colors, gl_mode)

def load_tetra():
	pass

SHAPES = {
	'Axises'	:	load_axises,
	'Point'		:	load_point,
	'Triangle'	:	load_triangle,
	'Square'	:	load_square,
	'Cube'		:	load_cube,
	'Tetra'		:	load_tetra,
}


class Shape:
	def __init__(self, _position : Matrix = Zero3_Vector, _edge : float = 1, _shape_type = None, _color = COLORS['white']) -> None:
		self.position	: Matrix	= _position
		self.edge		: float		= _edge

		shape_data = _shape_type(_position.V, _edge)
		self.vertices	: list[Matrix]		= shape_data[0]
		self.edges		: list[tuple[int]]	= shape_data[1]
		self.surfaces	: list[tuple[int]]	= shape_data[2]
		if shape_data[3] is None:
			self.colors 		: tuple[float, float, float] = _color
		else:
			self.colors 		: list[tuple[float, float, float]] = shape_data[3]
		self.gl_mode = shape_data[4]
			

	def __repr__(self) -> str:
		return f'pos: {self.position}\nedge: {self.edge}\nv: {self.vertices}\ne: {self.edges}\ns: {self.surfaces}\n'

if __name__ == '__main__':
	# triangle = Shape(_shape_type=SHAPES['Triangle'])
	# print(triangle)
	print(generate_colors())

