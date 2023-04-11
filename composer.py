from math import sin, pi

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import matrix

COLORS = {
	'white'		:	(1, 1, 1),
	'black'		:	(0, 0, 0),

	'red'		:	(1, 0, 0),
	'green'		:	(0, 1, 0),
	'blue'		:	(0, 0, 1),
		
	'magenta'	:	(1, 0, 1),
	'yellow'	:	(1, 1, 0),
	'yellow_c'	:	(1, 0.75, 0),
	'cyan'		:	(0, 1, 1),
}

class Vertex:
	def __init__(self, _x : float, _y : float, _z : float) -> None:
		self.x : float = _x
		self.y : float = _y
		self.z : float = _z
		self.V : tuple[float, float, float] = self.set_tuple()

	def set_tuple(self) -> tuple[float, float, float]:
		return (self.x, self.y, self.z)

	def draw(self) -> None:
		glBegin(GL_POINTS)
		glVertex3f(self.x, self.y, self.z)
		glEnd()
		
	def translate(self, _vector : list[float]) -> None:
		new_vertex : matrix.Matrix = matrix.M['T'](_vector) * matrix.Matrix(list(self.V).append(1), _is_vector=True)
		print(new_vertex.V)
		self.x = new_vertex.V[0]
		self.y = new_vertex.V[1]
		self.z = new_vertex.V[2]
		self.V = new_vertex.V

	def rotate(self, _position, _angle : float, _axis : str) -> None:
		new_vertex : matrix.Matrix = matrix.M[_axis](_angle) * matrix.Matrix((self - _position).V, _is_vector=True)
		# print(new_vertex.V)
		self.x = new_vertex.V[0] + _position.x
		self.y = new_vertex.V[1] + _position.y
		self.z = new_vertex.V[2] + _position.z
		self.V = new_vertex.V

	def rotate_any(self, _position, _yaw : float, _pitch : float, _roll : float) -> None:
		new_vertex : matrix.Matrix = matrix.Ro_Any_Matrix(_yaw, _pitch, _roll) * matrix.Matrix((self - _position).V, _is_vector=True)
		# print(new_vertex.V)
		self.x = new_vertex.V[0] + _position.x
		self.y = new_vertex.V[1] + _position.y
		self.z = new_vertex.V[2] + _position.z
		self.V = new_vertex.V

	def __sub__(self, _v):
		return Vertex(self.x - _v.x, self.y - _v.y, self.z - _v.z)


class Shape2D:
	def __init__(self, _position : Vertex = Vertex(0, 0, 0), _vertices : list[Vertex] = list(), _color : tuple[float] = None, _render_mode = GL_TRIANGLE_FAN) -> None:
		self.position : Vertex = _position
		self.vertices : list[Vertex] = _vertices
		self.color = _color
		self.render_mode = _render_mode

	def draw(self, _true, _draw_vertices : bool = False) -> None:
		glBegin(self.render_mode)
		glColor3f(*self.color)
		for vertex in self.vertices:
			glVertex3f(vertex.x, vertex.y, vertex.z)
			if _draw_vertices:
				vertex.draw()
		glEnd()

	def translate(self, _vector : list[float]) -> None:
		for vertex in self.vertices:
			vertex.translate(_vector)

	def rotate(self, _angle : float, _axis : str) -> None:
		for vertex in self.vertices:
			vertex.rotate(self.position, _angle, _axis)

	def rotate_any(self, _yaw : float, _pitch : float, _roll : float) -> None:
		for vertex in self.vertices:
			vertex.rotate_any(self.position, _yaw, _pitch, _roll)

	@staticmethod
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

	@staticmethod
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

	@staticmethod
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

	@staticmethod
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


class Shape3D:
	def __init__(self, _position : Vertex = Vertex(0, 0, 0), _vertices : list[Vertex] = list(), _surfaces : list[Shape2D] = list(), _color : tuple[float] = None) -> None:
		self.position : Vertex = _position
		self.vertices : list[Vertex] = _vertices
		self.surfaces : list[Shape2D] = _surfaces
		self.color = _color

	def draw(self, _draw_edges : bool = False, _draw_vertices : bool = False) -> None:
		for surface in self.surfaces:
			if _draw_edges:
				for i in range(len(surface.vertices) - 1):
					glBegin(GL_LINES)
					glColor3f(0,0,0)
					glVertex3f(surface.vertices[i].x, surface.vertices[i].y, surface.vertices[i].z)
					glVertex3f(surface.vertices[i + 1].x, surface.vertices[i + 1].y, surface.vertices[i + 1].z)
					glEnd()
			surface.draw(_draw_vertices)

	def translate(self, _vector : list[float]) -> None:
		for surface in self.surfaces:
			surface.translate(_vector)

	def rotate(self, _angle : float, _axis : str) -> None:
		for surface in self.surfaces:
			surface.rotate(_angle, _axis)
	
	def rotate_any(self, _yaw : float, _pitch : float, _roll : float) -> None:
		for surface in self.surfaces:
			surface.rotate_any(_yaw, _pitch, _roll)

	@staticmethod
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
	
	@staticmethod
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
	
	@staticmethod
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

	@staticmethod
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

	@staticmethod
	def Dodecahedron(_position : Vertex = Vertex(0, 0, 0), _edge : float = 1, _color : tuple[float] = None):
		fi = pi * 2 / 5
		r = _edge / (2 * sin(fi / 2))
		circumradius = (3 ** (1 / 2)) * (1 + (5 ** (1 / 2))) * _edge / 4
		y_top = _edge / 2 * (3 * (3 + 2 * (5 ** (1 / 2))) / 2 - 1 / sin(fi / 2)) ** (1 / 2)
		
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
		for i in range(5):
			vertex = Vertex(
				_position.x,
				_position.y + y_top,
				_position.z - r,
			)
			vertex.rotate(_position, fi * i, 'Ro_y')
			VERTICES.append(vertex)

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
				VERTICES[5],
				VERTICES[6],
				VERTICES[7],
				VERTICES[8],
				VERTICES[9],
			], _color),
			
		])
