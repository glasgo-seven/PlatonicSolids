from vertex import Vertex
from utils import *

class Shape2D:
	def __init__(self, _position : Vertex = Vertex(0, 0, 0), _vertices : list[Vertex] = list(), _color : tuple[float] = None, _render_mode = GL_TRIANGLE_FAN) -> None:
		self.position : Vertex = _position
		self.vertices : list[Vertex] = _vertices
		self.color = _color
		self.render_mode = _render_mode

	def draw(self, _object_position : Vertex, _true, _draw_vertices : bool = False) -> None:
		glBegin(self.render_mode)
		glColor3f(*self.color)
		for vertex in self.vertices:
			glVertex3f(
				_object_position.x + vertex.x,
				_object_position.y + vertex.y,
				_object_position.z + vertex.z)
			if _draw_vertices:
				vertex.draw()
		glEnd()

	def translate(self, _vector : list[float]) -> None:
		for vertex in self.vertices:
			vertex.translate(_vector)
		self.position.translate(_vector)

	def rotate(self, _object_position : Vertex, _angle : float, _axis : str) -> None:
		for vertex in self.vertices:
			vertex.rotate(_object_position, _angle, _axis)

	def rotate_any(self, _yaw : float, _pitch : float, _roll : float) -> None:
		for vertex in self.vertices:
			vertex.rotate_any(self.position, _yaw, _pitch, _roll)
