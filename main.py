from utils import *
from vertex import Vertex
from shape2d import Shape2D
from shape3d import Shape3D
from composer2d import Axises
from composer3d import Dodecahedron


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

	SHAPES : list[Shape2D | Shape3D] = list()
	SHAPES.append(Axises())
	SHAPES.append(Dodecahedron(Vertex(0, 0, 0), 1, COLORS['yellow_c']))

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

		for shape in SHAPES:
			shape.draw(True, False)
		# SHAPES[1].rotate(radians(1), 'Ro_y')
		SHAPES[1].translate([.01, .01, .01])

		clock.tick(30)
		pygame.display.set_caption(f'{int(clock.get_fps())}')
		pygame.display.flip()
		# pygame.time.wait(30)

if __name__ == '__main__':
	main()