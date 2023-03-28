import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

COLORS = {
	'red'		:	(1, 0, 0),
	'green'		:	(0, 1, 0),
	'blue'		:	(0, 0, 1),
		
	'magenta'	:	(1, 0, 1),
	'yelllow'	:	(1, 1, 0),
	'cian'		:	(0, 1, 1),
}

def square(color):
	glColor3f(*color)
	glBegin(GL_TRIANGLE_FAN)
	glVertex3f(-0.5, -0.5, 0.5)
	glVertex3f(0.5, -0.5, 0.5)
	glVertex3f(0.5, 0.5, 0.5)
	glVertex3f(-0.5, 0.5, 0.5)
	glEnd()


def cube(size):
	glPushMatrix()
	glScalef(size,size,size)
		
	square(COLORS['red'])
		
	glPushMatrix()
	glRotatef(90, 0, 1, 0)
	square(COLORS['green'])
	glPopMatrix()
		
	glPushMatrix()
	glRotatef(-90, 1, 0, 0)
	square(COLORS['blue'])
	glPopMatrix()
		
	glPushMatrix()
	glRotatef(180, 0, 1, 0)
	square(COLORS['cian'])
	glPopMatrix()
		
	glPushMatrix()
	glRotatef(-90, 0, 1, 0)
	square(COLORS['magenta'])
	glPopMatrix()
		
	glPushMatrix()
	glRotatef(90, 1, 0, 0)
	square(COLORS['yelllow'])
	glPopMatrix()
		
	glPopMatrix()

def main():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(0, 0, -4)


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		glRotatef(0.5, 1, 1, 1)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		cube(1)

		pygame.display.flip()
		pygame.time.wait(10)

main()
