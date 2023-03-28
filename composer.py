import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import matrix

COLORS = {
	'red'		:	(1, 0, 0),
	'green'		:	(0, 1, 0),
	'blue'		:	(0, 0, 1),
		
	'magenta'	:	(1, 0, 1),
	'yellow'	:	(1, 1, 0),
	'yellow_c'	:	(1, 0.75, 0),
	'cian'		:	(0, 1, 1),
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

	def rotate(self, _angle : float, _axis : str) -> None:
		new_vertex : matrix.Matrix = matrix.M[_axis](_angle) * matrix.Matrix(self.V, _is_vector=True)
		print(new_vertex.V)
		self.x = new_vertex.V[0]
		self.y = new_vertex.V[1]
		self.z = new_vertex.V[2]
		self.V = new_vertex.V

class Shape2D:
	def __init__(self, _position : Vertex = Vertex(0, 0, 0), _vertices : list[Vertex] = list(), _color : tuple[float] = None) -> None:
		self.position : Vertex = _position
		self.vertices : list[Vertex] = _vertices
		self.color = _color

	def draw(self, _draw_vertices : bool = False) -> None:
		glBegin(GL_TRIANGLE_FAN)
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
			vertex.rotate(_angle, _axis)

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

	@staticmethod
	def Cube(_position : Vertex = Vertex(0, 0, 0), _edge : float = 1):
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
			], COLORS['yellow_c']),
			Shape2D(_position, [
				VERTICES[4],
				VERTICES[5],
				VERTICES[6],
				VERTICES[7],
			], COLORS['yellow_c']),

			Shape2D(_position, [
				VERTICES[0],
				VERTICES[1],
				VERTICES[5],
				VERTICES[4],
			], COLORS['yellow_c']),
			Shape2D(_position, [
				VERTICES[2],
				VERTICES[3],
				VERTICES[7],
				VERTICES[6],
			], COLORS['yellow_c']),

			Shape2D(_position, [
				VERTICES[0],
				VERTICES[3],
				VERTICES[7],
				VERTICES[4],
			], COLORS['yellow_c']),
			Shape2D(_position, [
				VERTICES[1],
				VERTICES[2],
				VERTICES[6],
				VERTICES[5],
			], COLORS['yellow_c']),
			
		])
	
	@staticmethod
	def Tetrahidron(_position : Vertex = Vertex(0, 0, 0), _edge : float = 1):
		pass
	
	@staticmethod
	def Octahidron(_position : Vertex = Vertex(0, 0, 0), _edge : float = 1):
		pass

