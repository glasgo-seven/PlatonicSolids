import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )
surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )
colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

from shape import Shape, SHAPES, COLORS

OBJECTS = [
    Shape(_edge=10, _shape_type=SHAPES['Axises'], _color=COLORS['white'])
]

def draw(_shape : Shape):
    # glBegin(GL_QUADS)
    # for surface in _shape.surfaces:
    #     for vertex in surface:
    #         glColor3fv(_shape.color)
    #         glVertex3fv(_shape.vertices[vertex].V)
    # glEnd()
    
    glBegin(GL_LINES)
    # for edge in _shape.edges:
    for edge in range(len(_shape.edges)):
        try:
            glColor3fv(_shape.color[edge])
        except:
            glColor3fv(_shape.color)
        for vertex in _shape.edges[edge]:
            glVertex3fv(_shape.vertices[vertex].V)
    glEnd() 


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)

    OBJECTS.append(Shape(_shape_type=SHAPES['Triangle']))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        for obj in OBJECTS:
            draw(obj)
        pygame.display.flip()
        pygame.time.wait(10)

main() 