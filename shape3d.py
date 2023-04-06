from util import *

from vertex import Vertex
from shape1d import Shape1D
from shape2d import Shape2D

class Shape3D:
	def __init__(self, _position : Vertex = Vertex(0, 0, 0), _surfaces : list[Shape2D] = list(), _color : tuple[float] = None) -> None:
		self.position : Vertex = _position
		self.surfaces : list[Shape2D] = _surfaces
		self.color = _color

	def draw(self, _draw_edges : bool = False, _draw_vertices : bool = False) -> None:
		for surface in self.surfaces:
			# if _draw_edges:
			# 	for i in range(len(surface.vertices) - 1):
			# 		glBegin(GL_LINES)
			# 		glColor3f(0,0,0)
			# 		glVertex3f(surface.vertices[i].x, surface.vertices[i].y, surface.vertices[i].z)
			# 		glVertex3f(surface.vertices[i + 1].x, surface.vertices[i + 1].y, surface.vertices[i + 1].z)
			# 		glEnd()
			surface.draw(_draw_edges, _draw_vertices)

	def translate(self, _vector : list[float]) -> None:
		for surface in self.surfaces:
			surface.translate(_vector)

	def rotate(self, _angle : float, _axis : str) -> None:
		for surface in self.surfaces:
			surface.rotate(_angle, _axis)

	@staticmethod
	def Cube(_position : Vertex = Vertex(0, 0, 0), _edge : float = 1, _color : tuple[float] = None):
		half_edge = _edge / 2
		'''
				7			6
			4			5
					.
				3			2
			0			1
		y
		z	x
		'''
		VERTICES = [
			Vertex(
				_position.x - half_edge,
				_position.y - half_edge,
				_position.z - half_edge,
			),
			Vertex(
				_position.x + half_edge,
				_position.y - half_edge,
				_position.z - half_edge,
			),
			Vertex(
				_position.x + half_edge,
				_position.y - half_edge,
				_position.z + half_edge,
			),
			Vertex(
				_position.x - half_edge,
				_position.y - half_edge,
				_position.z + half_edge,
			),
			
			Vertex(
				_position.x - half_edge,
				_position.y + half_edge,
				_position.z - half_edge,
			),
			Vertex(
				_position.x + half_edge,
				_position.y + half_edge,
				_position.z - half_edge,
			),
			Vertex(
				_position.x + half_edge,
				_position.y + half_edge,
				_position.z + half_edge,
			),
			Vertex(
				_position.x - half_edge,
				_position.y + half_edge,
				_position.z + half_edge,
			),
			

		]
		return Shape3D(_position, [
			Shape2D(_position, [
				VERTICES[0],
				VERTICES[1],
				VERTICES[2],
				VERTICES[3],
			], _color),
			Shape2D(_position, [
				VERTICES[4],
				VERTICES[5],
				VERTICES[6],
				VERTICES[7],
			], _color),

			Shape2D(_position, [
				VERTICES[0],
				VERTICES[1],
				VERTICES[5],
				VERTICES[4],
			], _color),
			Shape2D(_position, [
				VERTICES[2],
				VERTICES[3],
				VERTICES[7],
				VERTICES[6],
			], _color),

			Shape2D(_position, [
				VERTICES[0],
				VERTICES[3],
				VERTICES[7],
				VERTICES[4],
			], _color),
			Shape2D(_position, [
				VERTICES[1],
				VERTICES[2],
				VERTICES[6],
				VERTICES[5],
			], _color),
			
		])

