from math import radians, degrees, pi

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from composer import *
from matrix import *

def main():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(0, 0, -6)
	# glRotatef(225, 0, 1, 0)

	# glMatrixMode (GL_PROJECTION)
	# glLoadIdentity()
	# glFrustum(-0.1,0.1, -0.1,0.1, 0.2,1000)
	# glMatrixMode (GL_MODELVIEW)
	# glLoadIdentity()
	
	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LESS)

	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_COLOR_MATERIAL)
	glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 4, 1))

	# glEnable(GL_LIGHT4)
	# glLightfv(GL_LIGHT4, GL_DIFFUSE, (0.4, 0.7, 0.2))
	# glLightfv(GL_LIGHT4, GL_POSITION, (0.0, 0.0, 4, 1.0))
	# glLightf(GL_LIGHT4, GL_SPOT_CUTOFF, 30)
	# glLightfv(GL_LIGHT4, GL_SPOT_DIRECTION, (0.0, 0.0, -1.0))
	# glLightf(GL_LIGHT4, GL_SPOT_EXPONENT, 15.0)

	SHAPES : list[Shape2D | Shape3D] = list()
	SHAPES.append(Shape2D.Axises())

	# shape = Shape3D.Cube()
	# SHAPES.append(Shape2D.Square(Vertex(0, 0, -2), .25, COLORS['white']))
	SHAPES.append(Shape3D.Cube(Vertex(-2, 0, 0), 1, COLORS['yellow_c']))
	SHAPES.append(Shape3D.Tetrahidron(Vertex(2, 0, 0), 1, COLORS['red']))

	# SHAPES.append(Shape2D.Line(Vertex(0, 0, 0), 1, COLORS['yellow_c']))
	

	# SHAPES.append(Shape2D.Square(Vertex(0, 0, 1), 1, COLORS['red']))
	# SHAPES.append(Shape2D.Square(Vertex(0, 0, -1), 1, COLORS['blue']))
	# SHAPES.append(Shape2D.Square(Vertex(1, 0, 0), 1, COLORS['green'], (pi/2, 'Ro_y')))
	# SHAPES.append(Shape2D.Square(Vertex(-1, 0, 0), 1, COLORS['yellow'], (pi/2, 'Ro_y')))

	clock = pygame.time.Clock()
	is_over = False

	while not is_over:
		dX = 0
		dY = 0
		dZ = 0
		angle = 0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				is_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP2:
					dX += 1
					angle = 15
				if event.key == pygame.K_KP8:
					dX -= 1
					angle = 15

				if event.key == pygame.K_KP6:
					dY += 1
					angle = 15
				if event.key == pygame.K_KP4:
					dY -= 1
					angle = 15
				
				if event.key == pygame.K_KP7:
					dZ += 1
					angle = 15
				if event.key == pygame.K_KP9:
					dZ -= 1
					angle = 15

		glRotatef(angle, dX, dY, dZ)
		# glRotatef(.5, 1, 1, 1)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		# shape.translate([1, 0, 0])
		# shape.rotate(.04, 'Ro_y')
		for shape in SHAPES:
			shape.draw(True, False)
			shape.rotate(radians(1), 'Ro_y')
			# print(shape.position.V)
			# for vertex in shape.vertices:
			# 	print(vertex.V)
			# print()

		clock.tick(40)
		pygame.display.set_caption(f'{int(clock.get_fps())}')
		pygame.display.flip()
		# pygame.time.wait(30)

if __name__ == '__main__':
	main()