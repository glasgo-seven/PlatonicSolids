from sys import exit

from utils import *

from composer2d import Axises, Cage, Net, Square
from composer3d import Cube, Tetrahedron, Octahedron, Icosahedron, Dodecahedron

from app import Vertex, Object, App


if __name__ == '__main__':
	app = App()

	app.add_debug_object(Object(_position=Vertex(0, 0, 0), _shape=Cage()))
	# app.add_debug_object(Object(_position=Vertex(0, 0, 0), _shape=Net()))
	
	app.add_object(
		Object(
			_position=Vertex(1, 1, 1),
			_face=Vertex(0, 1, 0),
			_shape=Cube(Vertex(0, 0, 0), 1, COLORS['red']),
			_edge=1
			)
		)
	app.add_object(
		Object(
			_position=Vertex(-1, 0, 0),
			_face=Vertex(0, 1, 0),
			_shape=Tetrahedron(Vertex(0, 0, 0), 1.2, COLORS['green']),
			_edge=1.2
			)
		)
	app.add_object(
		Object(
			_position=Vertex(-2, 0, 0),
			_face=Vertex(0, 1, 0),
			_shape=Octahedron(Vertex(0, 0, 0), .9, COLORS['cyan']),
			_edge=.9
			)
		)
	app.add_object(
		Object(
			_position=Vertex(1, 0, 0),
			_face=Vertex(0, 1, 0),
			_shape=Icosahedron(Vertex(0, 0, 0), .75, COLORS['yellow_c']),
			_edge=.75
			)
		)
	app.add_object(
		Object(
			_position=Vertex(2, 0, 0),
			_face=Vertex(0, 1, 0),
			_shape=Dodecahedron(Vertex(0, 0, 0), .65, COLORS['magenta']),
			_edge=.65
			)
	)
	
	for shape in app.SHAPES:
		shape.push()
		shape.spin()
	
	app.run(_debug=True)