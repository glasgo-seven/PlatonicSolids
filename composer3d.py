from utils import *
from shape3d import Vertex, Shape2D, Shape3D

def Cube(_position : Vertex = Vertex(0, 0, 0), _edge : float = 1, _color : tuple[float] = None):
	half_edge = _edge / 2
	'''
			3			2
		0			1

			7			6
		4			5
	'''
	VERTICES = [
		Vertex(
			_position.x - half_edge,
			_position.y - half_edge,
			_position.z - half_edge,
		),
		Vertex(
			_position.x - half_edge,
			_position.y + half_edge,
			_position.z - half_edge,
		),
		Vertex(
			_position.x + half_edge,
			_position.y + half_edge,
			_position.z - half_edge,
		),
		Vertex(
			_position.x + half_edge,
			_position.y - half_edge,
			_position.z - half_edge,
		),
		
		Vertex(
			_position.x - half_edge,
			_position.y - half_edge,
			_position.z + half_edge,
		),
		Vertex(
			_position.x - half_edge,
			_position.y + half_edge,
			_position.z + half_edge,
		),
		Vertex(
			_position.x + half_edge,
			_position.y + half_edge,
			_position.z + half_edge,
		),
		Vertex(
			_position.x + half_edge,
			_position.y - half_edge,
			_position.z + half_edge,
		),
		
	]
	return Shape3D(_position, VERTICES, [
		Shape2D(_position, [
			VERTICES[0],
			VERTICES[1],
			VERTICES[2],
			VERTICES[3],
		], _color),
		Shape2D(_position, [
			VERTICES[4],
			VERTICES[5],
			VERTICES[6],
			VERTICES[7],
		], _color),

		Shape2D(_position, [
			VERTICES[0],
			VERTICES[1],
			VERTICES[5],
			VERTICES[4],
		], _color),
		Shape2D(_position, [
			VERTICES[2],
			VERTICES[3],
			VERTICES[7],
			VERTICES[6],
		], _color),

		Shape2D(_position, [
			VERTICES[0],
			VERTICES[3],
			VERTICES[7],
			VERTICES[4],
		], _color),
		Shape2D(_position, [
			VERTICES[1],
			VERTICES[2],
			VERTICES[6],
			VERTICES[5],
		], _color),

	])


def Tetrahedron(_position : Vertex = Vertex(0, 0, 0), _edge : float = 1, _color : tuple[float] = None):
	half_edge = _edge / 2
	y_base = _edge / 4 * ((2 / 3) ** (1 / 2))
	z_diff = _edge / (2 * (3 ** (1 / 2)))
	'''
				3		

				2		
		0			1
	'''
	VERTICES = [
		Vertex(
			_position.x - half_edge,
			_position.y - y_base,
			_position.z - z_diff,
		),
		Vertex(
			_position.x + half_edge,
			_position.y - y_base,
			_position.z - z_diff,
		),
		Vertex(
			_position.x,
			_position.y - y_base,
			_position.z + 2 * z_diff,
		),
		Vertex(
			_position.x,
			_position.y + 3 * y_base,
			_position.z,
		),
		
	]
	return Shape3D(_position, VERTICES, [
		Shape2D(_position, [
			VERTICES[0],
			VERTICES[1],
			VERTICES[2],
		], _color),
		Shape2D(_position, [
			VERTICES[0],
			VERTICES[1],
			VERTICES[3],
		], _color),
		Shape2D(_position, [
			VERTICES[1],
			VERTICES[2],
			VERTICES[3],
		], _color),
		Shape2D(_position, [
			VERTICES[2],
			VERTICES[0],
			VERTICES[3],
		], _color),
		
	])


def Octahedron(_position : Vertex = Vertex(0, 0, 0), _edge : float = 1, _color : tuple[float] = None):
	half_edge = _edge / 2
	height = _edge * ((1 / 2) ** (1 / 2))
	'''
				4		

			3			2
		0			1

				5
	'''
	VERTICES = [
		Vertex(
			_position.x - half_edge,
			_position.y,
			_position.z - half_edge,
		),
		Vertex(
			_position.x + half_edge,
			_position.y,
			_position.z - half_edge,
		),
		Vertex(
			_position.x + half_edge,
			_position.y,
			_position.z + half_edge,
		),
		Vertex(
			_position.x - half_edge,
			_position.y,
			_position.z + half_edge,
		),
		Vertex(
			_position.x,
			_position.y + height,
			_position.z,
		),
		Vertex(
			_position.x,
			_position.y - height,
			_position.z,
		),
		
	]
	return Shape3D(_position, VERTICES, [
		Shape2D(_position, [
			VERTICES[0],
			VERTICES[1],
			VERTICES[4],
		], _color),
		Shape2D(_position, [
			VERTICES[0],
			VERTICES[1],
			VERTICES[5],
		], _color),

		Shape2D(_position, [
			VERTICES[1],
			VERTICES[2],
			VERTICES[4],
		], _color),
		Shape2D(_position, [
			VERTICES[1],
			VERTICES[2],
			VERTICES[5],
		], _color),
		
		Shape2D(_position, [
			VERTICES[2],
			VERTICES[3],
			VERTICES[4],
		], _color),
		Shape2D(_position, [
			VERTICES[2],
			VERTICES[3],
			VERTICES[5],
		], _color),
		
		Shape2D(_position, [
			VERTICES[3],
			VERTICES[0],
			VERTICES[4],
		], _color),
		Shape2D(_position, [
			VERTICES[3],
			VERTICES[0],
			VERTICES[5],
		], _color),
		
	])


def Icosahedron(_position : Vertex = Vertex(0, 0, 0), _edge : float = 1, _color : tuple[float] = None):
	fi = pi * 2 / 5
	r = _edge / (2 * sin(fi / 2))
	y_top = _edge / 2 * (3 - 1 / sin(fi / 2)) ** (1 / 2)
	circumradius = ((10 + (2 * 5 ** (1 / 2))) ** (1 / 2)) * (_edge / 4)
	print(circumradius, y_top)
	'''
				5
				3
		4				2
			0		1

				6
		7				10
			8		9
				11

	'''
	VERTICES = list()
	for i in range(5):
		vertex = Vertex(
			_position.x,
			_position.y + circumradius - y_top,
			_position.z - r,
		)
		vertex.rotate(_position, fi * i, 'Ro_y')
		VERTICES.append(vertex)
	VERTICES.append(
		Vertex(
			_position.x,
			_position.y + circumradius,
			_position.z,
		))
	

	for i in range(5):
		vertex = Vertex(
			_position.x,
			_position.y - circumradius + y_top,
			_position.z + r,
		)
		vertex.rotate(_position, fi * i, 'Ro_y')
		VERTICES.append(vertex)
	VERTICES.append(
		Vertex(
			_position.x,
			_position.y - circumradius,
			_position.z,
		))

	return Shape3D(_position, VERTICES, [
		Shape2D(_position, [
			VERTICES[0],
			VERTICES[1],
			VERTICES[5],
		], _color),
		Shape2D(_position, [
			VERTICES[1],
			VERTICES[2],
			VERTICES[5],
		], _color),
		Shape2D(_position, [
			VERTICES[2],
			VERTICES[3],
			VERTICES[5],
		], _color),
		Shape2D(_position, [
			VERTICES[3],
			VERTICES[4],
			VERTICES[5],
		], _color),
		Shape2D(_position, [
			VERTICES[4],
			VERTICES[0],
			VERTICES[5],
		], _color),

		Shape2D(_position, [
			VERTICES[0],
			VERTICES[1],
			VERTICES[9],
		], _color),
		Shape2D(_position, [
			VERTICES[1],
			VERTICES[2],
			VERTICES[10],
		], _color),
		Shape2D(_position, [
			VERTICES[2],
			VERTICES[3],
			VERTICES[6],
		], _color),
		Shape2D(_position, [
			VERTICES[3],
			VERTICES[4],
			VERTICES[7],
		], _color),
		Shape2D(_position, [
			VERTICES[4],
			VERTICES[0],
			VERTICES[8],
		], _color),

		Shape2D(_position, [
			VERTICES[6],
			VERTICES[7],
			VERTICES[3],
		], _color),
		Shape2D(_position, [
			VERTICES[7],
			VERTICES[8],
			VERTICES[4],
		], _color),
		Shape2D(_position, [
			VERTICES[8],
			VERTICES[9],
			VERTICES[0],
		], _color),
		Shape2D(_position, [
			VERTICES[9],
			VERTICES[10],
			VERTICES[1],
		], _color),
		Shape2D(_position, [
			VERTICES[10],
			VERTICES[6],
			VERTICES[2],
		], _color),

		Shape2D(_position, [
			VERTICES[6],
			VERTICES[7],
			VERTICES[11],
		], _color),
		Shape2D(_position, [
			VERTICES[7],
			VERTICES[8],
			VERTICES[11],
		], _color),
		Shape2D(_position, [
			VERTICES[8],
			VERTICES[9],
			VERTICES[11],
		], _color),
		Shape2D(_position, [
			VERTICES[9],
			VERTICES[10],
			VERTICES[11],
		], _color),
		Shape2D(_position, [
			VERTICES[10],
			VERTICES[6],
			VERTICES[11],
		], _color),
	])


def Dodecahedron(_position : Vertex = Vertex(0, 0, 0), _edge : float = 1, _color : tuple[float] = None):
	fi = pi * 2 / 5
	r = _edge / (2 * sin(fi / 2))
	circumradius = (3 ** (1 / 2)) * (1 + (5 ** (1 / 2))) * _edge / 4
	_y_top = _edge / 2 * (3 * (3 + 2 * (5 ** (1 / 2))) / 2 - 1 / sin(fi / 2)) ** (1 / 2)

	y_top = (circumradius ** 2 - r ** 2) ** (1 / 2)
	d = _edge / 2 * (1 + (5 ** (1 / 2)))
	r_ = d / (2 * sin(fi / 2))
	y_mid = (circumradius ** 2 - r_ ** 2) ** (1 / 2)

	
	# print(circumradius, y_top)
	'''
				
				3
		4				2
			0		1

			8		7
		9				6
				5	
				

	'''
	VERTICES = list()

	# top
	for i in range(5):
		vertex = Vertex(
			_position.x,
			_position.y + y_top,
			_position.z - r,
		)
		vertex.rotate(_position, fi * i, 'Ro_y')
		VERTICES.append(vertex)

	# top-mid
	for i in range(5):
		vertex = Vertex(
			_position.x,
			_position.y + y_mid,
			_position.z - r_,
		)
		vertex.rotate(_position, fi * i, 'Ro_y')
		VERTICES.append(vertex)

	# bottom-mid
	for i in range(5):
		vertex = Vertex(
			_position.x,
			_position.y - y_mid,
			_position.z + r_,
		)
		vertex.rotate(_position, fi * i, 'Ro_y')
		VERTICES.append(vertex)

	# bottom
	for i in range(5):
		vertex = Vertex(
			_position.x,
			_position.y - y_top,
			_position.z + r,
		)
		vertex.rotate(_position, fi * i, 'Ro_y')
		VERTICES.append(vertex)

	return Shape3D(_position, VERTICES, [
		Shape2D(_position, [
			VERTICES[0],
			VERTICES[1],
			VERTICES[2],
			VERTICES[3],
			VERTICES[4],
		], _color),

		Shape2D(_position, [
			VERTICES[0],
			VERTICES[1],
			VERTICES[6],
			VERTICES[-7],
			VERTICES[5],
		], _color),
		Shape2D(_position, [
			VERTICES[1],
			VERTICES[2],
			VERTICES[7],
			VERTICES[-6],
			VERTICES[6],
		], _color),
		Shape2D(_position, [
			VERTICES[2],
			VERTICES[3],
			VERTICES[8],
			VERTICES[-10],
			VERTICES[7],
		], _color),
		Shape2D(_position, [
			VERTICES[3],
			VERTICES[4],
			VERTICES[9],
			VERTICES[-9],
			VERTICES[8],
		], _color),
		Shape2D(_position, [
			VERTICES[4],
			VERTICES[0],
			VERTICES[5],
			VERTICES[-8],
			VERTICES[9],
		], _color),

		Shape2D(_position, [
			VERTICES[-1],
			VERTICES[-2],
			VERTICES[-7],
			VERTICES[6],
			VERTICES[-6],
		], _color),
		Shape2D(_position, [
			VERTICES[-2],
			VERTICES[-3],
			VERTICES[-8],
			VERTICES[5],
			VERTICES[-7],
		], _color),
		Shape2D(_position, [
			VERTICES[-3],
			VERTICES[-4],
			VERTICES[-9],
			VERTICES[9],
			VERTICES[-8],
		], _color),
		Shape2D(_position, [
			VERTICES[-4],
			VERTICES[-5],
			VERTICES[-10],
			VERTICES[8],
			VERTICES[-9],
		], _color),
		Shape2D(_position, [
			VERTICES[-5],
			VERTICES[-1],
			VERTICES[-6],
			VERTICES[7],
			VERTICES[-10],
		], _color),

		Shape2D(_position, [
			VERTICES[-1],
			VERTICES[-2],
			VERTICES[-3],
			VERTICES[-4],
			VERTICES[-5],
		], _color),
	])
