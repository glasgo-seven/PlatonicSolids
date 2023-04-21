from utils import *
from vertex import Vertex
from shape2d import Shape2D
from shape3d import Shape3D
from composer2d import Axises
from composer3d import Cube, Tetrahedron, Octahedron, Icosahedron, Dodecahedron


def main():

	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(0, 0, -10)
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
	glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 8, 1))

	SHAPES : list[Shape2D | Shape3D] = list()
	SHAPES.append(Axises())
	# SHAPES.append(Cube(Vertex(-4, 0, 0), 1, COLORS['red']))
	# SHAPES.append(Tetrahedron(Vertex(-2, 0, 0), 1.2, COLORS['cyan']))
	# SHAPES.append(Octahedron(Vertex(2, 0, 0), 0.95, COLORS['green']))
	# SHAPES.append(Icosahedron(Vertex(-4, 0, 0), 0.7, COLORS['magenta']))
	# SHAPES.append(Dodecahedron(Vertex(6, 0, 0), 0.5, COLORS['yellow']))

	SHAPES.append(Cube(Vertex(-2, 2, 0), 0.5, COLORS['red']))


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

		SHAPES[0].draw(True, False)
		for shape in SHAPES[1:]:
			print(f'POS: {shape.position.V}\nDIR: {shape.direction}')
			alert(shape.vertices[0].V)
			shape.translate(shape.direction)
			shape.rotate(radians(1), 'Ro_y')
			shape.collide()
			shape.draw(True, False)
			
		# SHAPES[1].rotate(-pi/4, 'Ro_y')
		# SHAPES[1].rotate(radians(1), 'Ro_y')
		# SHAPES[2].rotate(radians(1), 'Ro_x')
		# SHAPES[1].translate([.01, .01, .01])

		FPS_COUNT += 1

		clock.tick(FPS_CAP)
		pygame.display.set_caption(f'{int(clock.get_fps())} [{FPS_COUNT}]')
		pygame.display.flip()
		# pygame.time.wait(30)

if __name__ == '__main__':
	main()