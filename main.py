import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# verticies = (
#     (0, 0, 0),
#     (0, 1, 0),
#     (1, 0, 0),
#     (1, 1, 0),
    
#     (0, 0, 1),
#     (0, 1, 1),
#     (1, 0, 1),
#     (1, 1, 1)
# )

# edges = (
#     (0,1),
#     (0,2),
#     (1,3),
#     (2,3),
    
#     (4,5),
#     (4,6),
#     (5,7),
#     (6,7),
    
#     (0,4),
#     (1,5),
#     (2,6),
#     (3,7)
#     )

# colors = (
# #   (r,g,b)
#     (0,0,1),
#     (0,1,0),

#     (0,1,1), # yellow
#     (1,0,0),

#     (1,0,1),
#     (1,1,0),
#     )

# surfaces = (
#     (0,1,3,4),
#     (4,5,7,6),
    
#     (0,1,5,4),
#     (2,3,7,6),
    
#     (0,2,6,4),
#     (1,3,7,5)
#     )

from shape import Triangle

def Cube(shape):
    glBegin(GL_QUADS)
    x = 0
    for surface in shape.surfaces:
        for vertex in surface:
            # glColor3fv((0,0,0))
            glVertex3fv(shape.vertices[vertex].to_tuple())
        x += 1
    glEnd()

    glBegin(GL_LINES)
    for edge in shape.edges:
        for vertex in edge:
            glVertex3fv(shape.vertices[vertex].to_tuple())
    glEnd() 

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(-0.5, -0.5, -5)
    shape = Triangle((0,0,0), 1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # glRotatef(.1, 1, 1, 1)
        shape.rotate(30)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube(shape)
        pygame.display.flip()
        pygame.time.wait(10)

main() 