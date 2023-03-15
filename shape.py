# from vector import *
from matrix import *

class Vector:
	def __init__(self, _x, _y, _z) -> None:
		self.x = _x
		self.y = _y
		self.z = _z
	
	def to_tuple(self):
		return (self.x, self.y, self.z)
	
	def to_list(self):
		return [self.x, self.y, self.z]

from math import cos, sin
AXIS = {
	'X' :	lambda _angle :
		Matrix([
			[1,	0, 				0],
			[0,	cos(_angle),	-sin(_angle)],
			[0,	sin(_angle),	cos(_angle)]
		]),
	'Y' :	lambda _angle :
		Matrix([
			[cos(_angle),	0,	sin(_angle)],
			[0,				1,	0],
			[sin(_angle),	0,	cos(_angle)]
		]),
	'Z' :	lambda _angle :
		Matrix([
			[cos(_angle),	-sin(_angle),	0],
			[sin(_angle),	cos(_angle),	0],
			[0,				0,				1]
		])
}

class Triangle:
	def __init__(self, _position, _edge : float, _type : str = '') -> None:
		self.position = Vector(*_position)
		self.edge = _edge
		self.m = (self.edge ** 2 * 3 / 4) ** (1/2)

		self.vertices = [
			Vector(self.position.x,
					self.position.y,
					self.position.z),
			Vector(self.position.x + self.edge,
					self.position.y,
					self.position.z),
			Vector(self.position.x + self.edge / 2,
					self.position.y + self.m,
					self.position.z),
		]
		self.edges = [
			(0, 1),
			(1, 2),
			(2, 0)
		]
		self.surfaces = [
			(0, 1, 2)
		]

	def rotate(self, _angle, _axis = 'Z'):
		for i in range(len(self.vertices)):
			m = Matrix([self.vertices[i].to_list()]).T()
			self.vertices[i] = Vector(*(m * AXIS[_axis](_angle)).to_vector())





