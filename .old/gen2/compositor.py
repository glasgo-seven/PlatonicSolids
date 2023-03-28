import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# from matrix import *

class Vertex():
	def __init__(self, _x : float, _y : float, _z : float) -> None:
		self.x : float = _x
		self.y : float = _y
		self.z : float = _z

class Shape2D:
	def __init__(self, _position : Vertex = Vertex(0, 0, 0), _vertices : list[Vertex] = list()) -> None:
		self.position : Vertex = _position
		self.vertices : list[Vertex] = _vertices
	
	def add_vertex(self, _vertex : Vertex) -> None:
		self.vertices.append(_vertex)

class Shape3D:
	def __init__(self, _position : Vertex = Vertex(0, 0, 0), _surfaces : list[Shape2D] = list()) -> None:
		self.position = _position
		self.surfaces : list[Shape2D] = _surfaces
	
	def add_surface(self, _surface : Shape2D) -> None:
		self.surfaces.append(_surface)

def Cube() -> Shape3D:
	return Shape3D(_surfaces=[
		Shape2D(_vertices=[
			Vertex(0, 0, 0),
			Vertex(0, 1, 0),
			Vertex(1, 1, 0),
			Vertex(1, 0, 0),
		]),
		Shape2D(_vertices=[
			Vertex(0, 0, 1),
			Vertex(0, 1, 1),
			Vertex(1, 1, 1),
			Vertex(1, 0, 1),
		]),
		Shape2D(_vertices=[
			Vertex(0, 0, 0),
			Vertex(0, 1, 0),
			Vertex(0, 1, 1),
			Vertex(0, 0, 1),
		]),
		Shape2D(_vertices=[
			Vertex(1, 0, 0),
			Vertex(1, 1, 0),
			Vertex(1, 1, 1),
			Vertex(1, 0, 1),
		]),
		Shape2D(_vertices=[
			Vertex(0, 0, 0),
			Vertex(1, 0, 0),
			Vertex(1, 0, 1),
			Vertex(0, 0, 1),
		]),
		Shape2D(_vertices=[
			Vertex(0, 1, 0),
			Vertex(1, 1, 0),
			Vertex(1, 1, 1),
			Vertex(0, 1, 1),
		]),
		
	]
	)


COLORS = {
	'red'		:	(1, 0, 0),
	'green'		:	(0, 1, 0),
	'blue'		:	(0, 0, 1),
		
	'magenta'	:	(1, 0, 1),
	'yelllow'	:	(1, 1, 0),
	'cian'		:	(0, 1, 1),
}

colors = [
	(1, 0, 0),
	(0, 1, 0),
	(0, 0, 1),
	
	(1, 0, 1),
	(1, 1, 0),
	(0, 1, 1),
]

def draw_shape_2d(_shape : Shape2D, _color : tuple[float] = (0, 0, 0)) -> None:
	glColor3f(*_color)
	glBegin(GL_TRIANGLE_FAN)

	for vertex in _shape.vertices:
		glVertex3f(vertex.x, vertex.y, vertex.z)

	glEnd()

def draw_shape_3d(_shape : Shape3D) -> None:
	glPushMatrix()

	size = 1
	glScalef(size,size,size)

	rotations = [
		(0, 0, 0, 0),
		(180, 1, 1, 0),
		(90, 1, 0, 0),
		# (-90, 1, 0, 0),
		# (-90, 0, 1, 0),
		# (90, 1, 0, 0),
	]

	for i in range(3): #range(len(_shape.surfaces)):
		glPushMatrix()
		glRotatef(*rotations[i])
		draw_shape_2d(_shape.surfaces[i], colors[i])
		glPopMatrix()

	# draw_shape_2d(COLORS['red'])
		
	# glPushMatrix()
	# glRotatef(90, 0, 1, 0)
	# draw_shape_2d(COLORS['green'])
	# glPopMatrix()
		
	# glPushMatrix()
	# glRotatef(-90, 1, 0, 0)
	# draw_shape_2d(COLORS['blue'])
	# glPopMatrix()
		
	# glPushMatrix()
	# glRotatef(180, 0, 1, 0)
	# draw_shape_2d(COLORS['cian'])
	# glPopMatrix()
		
	# glPushMatrix()
	# glRotatef(-90, 0, 1, 0)
	# draw_shape_2d(COLORS['magenta'])
	# glPopMatrix()
		
	# glPushMatrix()
	# glRotatef(90, 1, 0, 0)
	# draw_shape_2d(COLORS['yelllow'])
	# glPopMatrix()
		
	glPopMatrix()

def main():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(-0.5, -0.5, -4)


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		glRotatef(0.5, 0, 1, 0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		draw_shape_3d(Cube())

		pygame.display.flip()
		pygame.time.wait(10)


if __name__ == '__main__':
	main()