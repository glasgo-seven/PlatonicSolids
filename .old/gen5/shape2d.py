from util import *

from vertex import Vertex

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