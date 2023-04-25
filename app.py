from utils import *

from object import Vertex, Shape2D, Shape3D, Object

class App:
	def __init__(self, _resolution : tuple[int, int] = DEFAULT_RESOLUTION) -> None:
		pygame.init()
		self.display = _resolution
		pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
		gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 50.0)
		glTranslatef(*CAM_POSITION)
		# glRotatef(225, 0, 1, 0)
	
		glEnable(GL_DEPTH_TEST)
		glDepthFunc(GL_LESS)

		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glEnable(GL_COLOR_MATERIAL)
		glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, LIGHT_POSITION, 1))

		self.SHAPES_DEBUG : list[Object] = list()
		self.SHAPES : list[Object] = list()

	def add_debug_object(self, _object : Object) -> None:
		self.SHAPES_DEBUG.append(_object)

	def add_object(self, _object : Object) -> None:
		self.SHAPES.append(_object)
		print(_object)

	def draw_objects(self, _debug):
		if _debug:
			for shape in self.SHAPES_DEBUG:
				shape.draw(True, False)

		for shape in self.SHAPES:
			# print(f'POS: {shape.position.V}\nDIR: {shape.direction}')
			# alert(shape.vertices[0].V)
			# shape.translate(shape.direction)
			# shape.rotate(radians(1), 'Ro_y')
			# shape.collide()

			# print(shape.face.length(), shape.face.V)
			# alert(shape.position)
			# error(shape.shape.position)
			# for vertex in shape.shape.vertices:
			# 	print(vertex)
			print()

			shape.draw(True, True)
			# shape.rotate_object(radians(1), 'Ro_z')
			# shape.rotate_shape(radians(1), 'Ro_y')
			# if _debug:
			shape.translate()
			shape.rotate()
			shape.collide()

			print(shape)
			


	def run(self, _debug : bool = False):
		clock = pygame.time.Clock()
		is_over = False

		global FPS_COUNT

		while not is_over:
			dX = 0
			dY = 0
			dZ = 0
			angle = 0
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					is_over = True
					pygame.quit()
					quit()
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

			FPS_COUNT += 1

			self.draw_objects(_debug)
			# if _debug:
			# 	is_over = True

			clock.tick(FPS_CAP)
			pygame.display.set_caption(f'{int(clock.get_fps())} [{FPS_COUNT}]')
			pygame.display.flip()

			# pygame.time.wait(30)
			# sleep(2)

if __name__ == '__main__':
	pass