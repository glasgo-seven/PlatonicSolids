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
		self.face : Vertex = Vertex(0, 1, 0)
		self.face_2 : Vertex = Vertex(0, .5, 0)
		self.direction : list[float] = _direction
		self.shape : Shape2D | Shape3D = _shape

	def push(self) -> None:
		"""
		Give a random uniform vector of direction
		"""
		self.direction= [
			uniform(*UNIFORM_DIRECTION_AREA),
			uniform(*UNIFORM_DIRECTION_AREA),
			uniform(*UNIFORM_DIRECTION_AREA)
		]

	def draw_face_vector(self):
		glLineWidth(2)
		glBegin(GL_LINES)
		glColor3f(*COLORS['cyan'])
		glVertex3f(self.position.x, self.position.y, self.position.z)
		glVertex3f(self.position.x + self.face.x, self.position.y + self.face.y, self.position.z + self.face.z)
		glEnd()
		glLineWidth(1)

	def draw_face_2_vector(self):
		glLineWidth(2)
		glBegin(GL_LINES)
		glColor3f(*COLORS['cyan'])
		glVertex3f(self.position.x, self.position.y, self.position.z)
		glVertex3f(self.position.x + self.face_2.x, self.position.y + self.face_2.y, self.position.z + self.face_2.z)
		glEnd()
		glLineWidth(1)
	
	def draw_y_axis(self):
		glLineWidth(2)
		glBegin(GL_LINES)
		glColor3f(*COLORS['red'])
		glVertex3f(self.position.x, self.position.y+1, self.position.z)
		glVertex3f(self.position.x, self.position.y-1, self.position.z)
		glEnd()
		glLineWidth(1)

	def draw_center(self):
		glPointSize(8)
		glBegin(GL_POINTS)
		glColor3f(*COLORS['white'])
		glVertex3f(self.position.x, self.position.y, self.position.z)
		glEnd()
		glPointSize(1)

	def draw(self, _draw_edges : bool = False, _draw_vertices : bool = False) -> None:
		self.draw_face_vector()
		self.draw_face_2_vector()
		self.draw_y_axis()
		self.draw_center()
		
		# self.shape.draw(self.position, _draw_edges, _draw_vertices)

	def rotate_object(self, _angle : float, _axis : str) -> None:
		"""
		Rotation in relation to Object Origin (Rotating only the object position and face Vector).
		"""
		self.face.rotate(Vertex(0, 0, 0), _angle, _axis)
		self.face_2.rotate(Vertex(0, 0, 0), _angle, _axis)
		self.shape.rotate(Vertex(0, 0, 0), _angle, _axis)

	def rotate_shape(self, _angle : float, _axis : str) -> None:
		"""
		Rotation in relation to Shape Origin (Rotating only the shape vertices).
		"""
		self.shape.rotate(Vertex(0, 0, 0), _angle, _axis)

if __name__ == '__main__':
	pass
