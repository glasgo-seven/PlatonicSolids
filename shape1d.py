from util import *

from vertex import Vertex

class Shape1D:
	def __init__(self, _position : Vertex = Vertex(0, 0, 0), _vertices : list[Vertex] = list(), _color : tuple[float] = None) -> None:
		self.position : Vertex = _position
		self.vertices : list[Vertex] = _vertices
		self.color = _color

	def draw(self, _draw_edges : bool = False, _draw_vertices : bool = False) -> None:
		glBegin(GL_LINE)
		glColor3f(*self.color)
		for vertex in self.vertices:
			glVertex3f(vertex.x, vertex.y, vertex.z)
			if _draw_vertices:
				vertex.draw()
		glEnd()

	def rotate(self, _angle : float, _axis : str) -> None:
		for vertex in self.vertices:
			vertex.rotate(self.position, _angle, _axis)

	# def translate(self, _vector : list[float]) -> None:
	# 	for vertex in self.vertices:
	# 		vertex.translate(_vector)

	# def rotate(self, _angle : float, _axis : str) -> None:
	# 	for vertex in self.vertices:
	# 		vertex.rotate(self.position, _angle, _axis)

	@staticmethod
	def Line(_position : Vertex = Vertex(0, 0, 0), _edge : float = 1, _color : tuple[float] = None, _rotation : tuple[float, str] = None):
		half_edge = _edge / 2
		return Shape1D(_position, [
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
			
		], _color)

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
