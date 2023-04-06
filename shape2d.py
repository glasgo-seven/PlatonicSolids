from util import *

from vertex import Vertex
from shape1d import Shape1D

class Shape2D:
	def __init__(self, _position : Vertex = Vertex(0, 0, 0), _edges : list[Shape1D] = list(), _color : tuple[float] = None) -> None:
		self.position : Vertex = _position
		# self.vertices : list[Vertex] = _vertices
		self.edges : list[Shape1D] = _edges
		self.color = _color

	def draw(self, _draw_edges : bool = False, _draw_vertices : bool = False) -> None:
		glBegin(GL_TRIANGLE_FAN)
		glColor3f(*self.color)
		for edge in self.edges:
			# glVertex3f(vertex.x, vertex.y, vertex.z)
			# if _draw_vertices:
			# 	vertex.draw()
			edge.draw(_draw_edges, _draw_vertices)
			# pass
		glEnd()

	def translate(self, _vector : list[float]) -> None:
		for edge in self.edges:
			edge.translate(_vector)

	def rotate(self, _angle : float, _axis : str) -> None:
		for edge in self.edges:
			edge.rotate(_angle, _axis)

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
		square = Shape2D(_position, [
			Shape1D(_position, [
				VERTICES[0],
				VERTICES[1],
			], _color),
			Shape1D(_position, [
				VERTICES[1],
				VERTICES[2],
			], _color),
			Shape1D(_position, [
				VERTICES[2],
				VERTICES[3],
			], _color),
			Shape1D(_position, [
				VERTICES[3],
				VERTICES[0],
			], _color),
			
		], _color)
		if _rotation is not None:
			square.rotate(*_rotation)
		return square
