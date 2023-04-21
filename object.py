from utils import *
from shape3d import Vertex, Shape2D, Shape3D

class Object:
	def __init__(self,
			_position : Vertex = Vertex(0, 0, 0),
			_face : Vertex = Vertex(0, 0, 1),
			_direction : list[float] = None,
			_shape : Shape2D | Shape3D = None
			) -> None:
		self.position : Vertex = _position
		self.face : Vertex = _face
		self.direction : list[float] = _direction
		self.shape : Shape2D | Shape3D = _shape

	def push(self) -> None:
		self.direction= [
			uniform(*UNIFORM_DIRECTION_AREA),
			uniform(*UNIFORM_DIRECTION_AREA),
			uniform(*UNIFORM_DIRECTION_AREA)
		]

	def draw(self, _draw_edges : bool = False, _draw_vertices : bool = False) -> None:
		glLineWidth(2)
		glBegin(GL_LINES)
		glColor3f(*COLORS['white'])
		glVertex3f(self.position.x, self.position.y, self.position.z)
		glVertex3f(self.position.x + self.face.x, self.position.y + self.face.y, self.position.z + self.face.z)
		glEnd()
		glLineWidth(1)

		glLineWidth(2)
		glBegin(GL_LINES)
		glColor3f(*COLORS['white'])
		glVertex3f(self.position.x, self.position.y+1, self.position.z)
		glVertex3f(self.position.x, self.position.y-1, self.position.z)
		glEnd()
		glLineWidth(1)

		glPointSize(16)
		glBegin(GL_POINTS)
		glColor3f(*COLORS['white'])
		glVertex3f(self.position.x, self.position.y, self.position.z)
		glEnd()
		glPointSize(1)
		
		self.shape.draw(self.position, _draw_edges, _draw_vertices)

	def rotate_object(self, _angle : float, _axis : str) -> None:
		# self.face.rotate(self.position, _angle, _axis)
		self.shape.rotate(self.position, _angle, _axis)

if __name__ == '__main__':
	pass
