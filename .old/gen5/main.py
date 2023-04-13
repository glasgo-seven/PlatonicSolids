
from util import *
from matrix import *
from shape3d import Shape3D
from shape2d import Shape2D
from vertex import Vertex

def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(0, 0, -8)
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

	# SHAPES.append(Shape3D.Cube(Vertex(0, 0, 0), 1, COLORS['yellow_c']))

	SHAPES.append(Shape3D.Cube(Vertex(0, 0, 0), 1, 0, COLORS['yellow_c']))

	# SHAPES.append(Shape3D.Tetrahedron(Vertex(2, 0, 0), 1, COLORS['red']))
	# SHAPES.append(Shape3D.Octahedron(Vertex(0, 2, 0), 1, COLORS['cyan']))
	# SHAPES.append(Shape3D.Icosahedron(Vertex(0, -2, 0), 1, COLORS['blue']))
	# SHAPES.append(Shape3D.Dodecahedron(Vertex(0, 0, 0), 1, COLORS['yellow_c']))

	# SHAPES.append(Shape3D.Dodecahedron(Vertex(0, 0, 0), 1, COLORS['magenta']))


	# SHAPES.append(Shape2D.Line(Vertex(0, 0, 0), 1, COLORS['yellow_c']))

	# SHAPES.append(Shape2D.Cirlce(Vertex(0, 0, 0), 1, _color=COLORS['red']))

	# SHAPES.append(Shape2D.Square(Vertex(0, 0, 1), 1, COLORS['red']))
	# SHAPES.append(Shape2D.Square(Vertex(0, 0, -1), 1, COLORS['blue']))
	# SHAPES.append(Shape2D.Square(Vertex(1, 0, 0), 1, COLORS['green'], (pi/2, 'Ro_y')))
	# SHAPES.append(Shape2D.Square(Vertex(-1, 0, 0), 1, COLORS['yellow'], (pi/2, 'Ro_y')))

	clock = pygame.time.Clock()
	is_over = False

	angle_x = 0
	angle_y = 0
	angle_z = 0


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
		# SHAPES[1].rotate(radians(1), 'Ro_y')
		# SHAPES[2].rotate(radians(1), 'Ro_z')
		# SHAPES[3].rotate(radians(1), 'Ro_x')
		# SHAPES[4].rotate(radians(1), 'Ro_y')

		
		# angle_x += uniform(-1, 1)
		# angle_y += uniform(-1, 1)
		# angle_z += uniform(-1, 1)
		# SHAPES[-2].rotate_any(radians(angle_z), radians(angle_y), radians(angle_x))
		# SHAPES[1].rotate(radians(1), 'Ro_y')
			# print(shape.position.V)
			# for vertex in shape.vertices:
			# 	print(vertex.V)
			# print()

		clock.tick(30)
		pygame.display.set_caption(f'{int(clock.get_fps())}')
		pygame.display.flip()
		# pygame.time.wait(30)

if __name__ == '__main__':
	main()