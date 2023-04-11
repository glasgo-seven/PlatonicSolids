from util import *

class Vertex:
	def __init__(self, _x : float, _y : float, _z : float) -> None:
		self.x : float = _x
		self.y : float = _y
		self.z : float = _z
		self.V : tuple[float, float, float] = self.set_tuple()

	def set_tuple(self) -> tuple[float, float, float]:
		return (self.x, self.y, self.z)

	def draw(self) -> None:
		glBegin(GL_POINT)
		glColor3f(*COLORS['white'])
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

	def __sub__(self, _v):
		return Vertex(self.x - _v.x, self.y - _v.y, self.z - _v.z)