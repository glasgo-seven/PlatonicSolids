from utils import *
from shape2d import Vertex, Shape2D

def Line(_position : Vertex = Vertex(0, 0, 0), _edge : float = 1, _color : tuple[float] = None, _rotation : tuple[float, str] = None):
	half_edge = _edge / 2
	VERTICES = [
		Vertex(
			_position.x,
			_position.y,
			_position.z - half_edge,
		),
		Vertex(
			_position.x,
			_position.y,
			_position.z + half_edge,
		),
		
	]
	return Shape2D(_position, VERTICES, _color, GL_LINES)


def Axises():
	half_edge = 4
	VERTICES = [
		Vertex(
			0,
			0,
			0,
		),
		Vertex(
			0,
			0,
			-half_edge,
		),

		Vertex(
			0,
			0,
			0,
		),
		Vertex(
			0,
			0,
			half_edge,
		),

		Vertex(
			0,
			0,
			0,
		),
		Vertex(
			0,
			-half_edge,
			0,
		),
		
		Vertex(
			0,
			0,
			0,
		),
		Vertex(
			0,
			half_edge,
			0,
		),

		Vertex(
			0,
			0,
			0,
		),
		Vertex(
			-half_edge,
			0,
			0,
		),

		Vertex(
			0,
			0,
			0,
		),
		Vertex(
			half_edge,
			0,
			0,
		),
		
	]
	return Shape2D(Vertex(0, 0, 0), VERTICES, COLORS['green'], GL_LINES)


def Square(_position : Vertex = Vertex(0, 0, 0), _edge : float = 1, _color : tuple[float] = None, _rotation : tuple[float, str] = None):
	half_edge = _edge / 2
	VERTICES = [
		Vertex(
			_position.x - half_edge,
			_position.y - half_edge,
			_position.z,
		),
		Vertex(
			_position.x + half_edge,
			_position.y - half_edge,
			_position.z,
		),
		Vertex(
			_position.x + half_edge,
			_position.y + half_edge,
			_position.z,
		),
		Vertex(
			_position.x - half_edge,
			_position.y + half_edge,
			_position.z,
		)
	]
	square = Shape2D(_position, VERTICES, _color)
	if _rotation is not None:
		square.rotate(*_rotation)
	return square


def Cirlce(_position : Vertex = Vertex(0, 0, 0), _radius : float = 1, _n_sides : int = 100, _color : tuple[float] = None):
	angle = 2 * pi / _n_sides
	VERTICES = []
	for i in range(_n_sides):
		vertex = Vertex(
			_position.x,
			_position.y + _radius,
			_position.z,
		)
		vertex.rotate(_position, i * angle, 'Ro_z')
		VERTICES.append(vertex)
	# print(VERTICES)
	return Shape2D(_position, VERTICES, _color)


