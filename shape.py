# from vector import *
# from matrix import Matrix
# from engine_3d import matrix
# from engine_3d import vector

import matrix
import vector

from math import cos, sin
AXIS = {
	'X' :	lambda _angle :
		matrix.Matrix([
			[1,	0, 				0],
			[0,	cos(_angle),	-sin(_angle)],
			[0,	sin(_angle),	cos(_angle)]
		]),
	'Y' :	lambda _angle :
		matrix.Matrix([
			[cos(_angle),	0,	sin(_angle)],
			[0,				1,	0],
			[sin(_angle),	0,	cos(_angle)]
		]),
	'Z' :	lambda _angle :
		matrix.Matrix([
			[cos(_angle),	-sin(_angle),	0],
			[sin(_angle),	cos(_angle),	0],
			[0,				0,				1]
		])
}

class Triangle:
	def __init__(self, _position, _edge : float, _type : str = '') -> None:
		self.position : vector.Vector = vector.Vector(*_position)
		self.edge : float = _edge
		self.m : float = (self.edge ** 2 * 3 / 4) ** (1/2)

		self.vertices : list[vector.Vector] = [
			vector.Vector(self.position.x,
					self.position.y,
					self.position.z),
			vector.Vector(self.position.x + self.edge,
					self.position.y,
					self.position.z),
			vector.Vector(self.position.x + self.edge / 2,
					self.position.y + self.m,
					self.position.z),
		]
		self.edges : list[tuple[int]] = [
			(0, 1),
			(1, 2),
			(2, 0)
		]
		self.surfaces : list[tuple[int]] = [
			(0, 1, 2)
		]

	def rotate(self, _angle, _axis = 'Z'):
		for i in range(len(self.vertices)):
			vertex_matrix = matrix.Matrix(
				self.vertices[i].to_matrix_content()
			)
			self.vertices[i] = vector.Vector(
				(AXIS[_axis](_angle) * vertex_matrix).to_vector_content()
			)
		print('ROTATION DONE')





