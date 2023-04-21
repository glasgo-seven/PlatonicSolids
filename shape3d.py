from utils import *
from shape2d import Vertex, Shape2D

class Shape3D:
	def __init__(self, _position : Vertex = Vertex(0, 0, 0), _vertices : list[Vertex] = list(), _surfaces : list[Shape2D] = list(), _color : tuple[float] = None, _direction : list[float] = None) -> None:
		self.position : Vertex = _position
		self.vertices : list[Vertex] = _vertices
		self.surfaces : list[Shape2D] = _surfaces
		self.color = _color
		self.direction : list[int] = [uniform(*UNIFORM_DIRECTION_AREA), uniform(*UNIFORM_DIRECTION_AREA), uniform(*UNIFORM_DIRECTION_AREA)] if not _direction else _direction
		# self.direction : list[float] = [0, 0, 0]

	def draw(self, _object_position : Vertex, _draw_edges : bool = False, _draw_vertices : bool = False) -> None:
		for surface in self.surfaces:
			if _draw_edges:
				for i in range(len(surface.vertices) - 1):
					glBegin(GL_LINES)
					glColor3f(*COLORS['black'])
					glVertex3f(
						_object_position.x + surface.vertices[i].x,
						_object_position.y + surface.vertices[i].y,
						_object_position.z + surface.vertices[i].z
					)
					glVertex3f(
						_object_position.x + surface.vertices[i + 1].x,
						_object_position.y + surface.vertices[i + 1].y,
						_object_position.z + surface.vertices[i + 1].z
					)
					glEnd()
			surface.draw(_object_position, _draw_vertices)

	def translate(self, _vector : list[float]) -> None:
		for surface in self.surfaces:
			surface.translate(_vector)
		self.position.translate(_vector)

	def rotate(self, _object_position : Vertex, _angle : float, _axis : str) -> None:
		for surface in self.surfaces:
			surface.rotate(_object_position, _angle, _axis)
	
	def rotate_any(self, _yaw : float, _pitch : float, _roll : float) -> None:
		for surface in self.surfaces:
			surface.rotate_any(_yaw, _pitch, _roll)

	def collide(self):
		collision = [1, 1, 1]
		if self.position.x >= 8 or self.position.x <= -8:
			collision[0] = -1
		if self.position.y >= 8 or self.position.y <= -8:
			collision[1] = -1
		if self.position.z >= 8 or self.position.z <= -8:
			collision[2] = -1
		
		self.direction = [
			self.direction[0] * collision[0],
			self.direction[1] * collision[1],
			self.direction[2] * collision[2]]
