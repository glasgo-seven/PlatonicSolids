from utils import *
from vertex import Vertex
from shape2d import Shape2D
from shape3d import Shape3D
from composer2d import Axises, Square
from composer3d import Cube, Tetrahedron, Octahedron, Icosahedron, Dodecahedron
from object import Object


def main():

	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(*CAM_POSITION)
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
	glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, LIGHT_POSITION, 1))

	SHAPES_DEBUG : list[Shape2D | Shape3D] = list()
	# SHAPES_DEBUG.append(Axises())
	# SHAPES_DEBUG.append(
	# 	Square(Vertex(0, 8, 0), 16, COLORS['dark_gray'], (pi/2, 'Ro_x'))
	# )
	# SHAPES_DEBUG.append(
	# 	Square(Vertex(0, -8, 0), 16, COLORS['dark_gray'], (pi/2, 'Ro_x'))
	# )
	# SHAPES_DEBUG.append(
	# 	Square(Vertex(8, 0, 0), 16, COLORS['dark_gray'], (pi/2, 'Ro_y'))
	# )
	# SHAPES_DEBUG.append(
	# 	Square(Vertex(-8, 0, 0), 16, COLORS['dark_gray'], (pi/2, 'Ro_y'))
	# )

	SHAPES : list[Object] = list()
	# SHAPES.append(Cube(Vertex(-4, 0, 0), 1, COLORS['red']))
	# SHAPES.append(Tetrahedron(Vertex(-2, 0, 0), 1.2, COLORS['cyan']))
	# SHAPES.append(Octahedron(Vertex(2, 0, 0), 0.95, COLORS['green']))
	# SHAPES.append(Icosahedron(Vertex(-4, 0, 0), 0.7, COLORS['magenta']))
	# SHAPES.append(Dodecahedron(Vertex(6, 0, 0), 0.5, COLORS['yellow']))

	SHAPES.append(
		Object(
			_position=Vertex(-.5, 0, 0),
			_face=Vertex(0, 1, 0),
			_direction=None,
			_shape=Cube(Vertex(0, 0, 0), 0.5, COLORS['red'])
			)
		)

	# SHAPES.append(Cube(Vertex(-1, 0, 0), 1, COLORS['red']))
	# SHAPES.append(Square(Vertex(1, 0, 0), 1, COLORS['green']))
	
	# SHAPES.append(
	# 	Object(
	# 		_position=Vertex(0, 0, 0),
	# 		_face=Vertex(1, 0, 0),
	# 		_direction=None,
	# 		_shape=Cube(Vertex(0, 0, 0), 0.5, COLORS['green'])
	# 		)
	# 	)
	# SHAPES.append(
	# 	Object(
	# 		_position=Vertex(1, -1, 0),
	# 		_face=Vertex(1, 0, 0),
	# 		_direction=None,
	# 		_shape=Cube(Vertex(0, 0, 0), 0.5, COLORS['blue'])
	# 		)
	# 	)
	


	clock = pygame.time.Clock()
	is_over = False

	angle_x = 0
	angle_y = 0
	angle_z = 0
	# A = [.01, .01, .01]
	global FPS_COUNT

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
				if event.key == pygame.K_UP:
					dX += 1
					angle = 15
				if event.key == pygame.K_DOWN:
					dX -= 1
					angle = 15

				if event.key == pygame.K_LEFT:
					dY += 1
					angle = 15
				if event.key == pygame.K_RIGHT:
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

		for shape in SHAPES_DEBUG:
			shape.draw(True, False)

		for shape in SHAPES:
			# print(f'POS: {shape.position.V}\nDIR: {shape.direction}')
			# alert(shape.vertices[0].V)
			# shape.translate(shape.direction)
			# shape.rotate(radians(1), 'Ro_y')
			# shape.collide()

			print(shape.face.length(), shape.face.V)
			alert(shape.position)
			error(shape.shape.position)
			# for vertex in shape.shape.vertices:
			# 	print(vertex)
			print()

			shape.draw(True, True)
			shape.rotate_object(radians(1), 'Ro_z')
			


		# SHAPES[1].rotate(-pi/4, 'Ro_y')
		# SHAPES[1].rotate(radians(1), 'Ro_y')
		# SHAPES[2].rotate(radians(1), 'Ro_x')
		# SHAPES[1].translate([.01, .01, .01])

		FPS_COUNT += 1

		clock.tick(FPS_CAP)
		pygame.display.set_caption(f'{int(clock.get_fps())} [{FPS_COUNT}]')
		pygame.display.flip()
		# pygame.time.wait(30)
		# sleep(2)

if __name__ == '__main__':
	main()