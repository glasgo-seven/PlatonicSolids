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
from matrix import Matrix

OBJECTS = [
    Shape(_edge=10, _shape_type=SHAPES['Axises'])
]

def draw_old(_shape : Shape):
    glBegin(GL_LINES)
    # for edge in _shape.edges:
    for edge in _shape.edges:
        for vertex in edge:
            glVertex3fv(_shape.vertices[vertex].V)
    glEnd()

def draw_surfaces(_shape : Shape):
    glBegin(GL_QUADS)
    # glBegin(GL_POLYGON)
    for surface in range(len(_shape.surfaces)):
        for vertex in _shape.surfaces[surface]:
            try:
                glColor3fv(_shape.colors[surface])
            except:
                glColor3fv(_shape.colors)
            glVertex3fv(_shape.vertices[vertex].V)
    glEnd()

def draw_edges(_shape : Shape):
    glBegin(GL_LINES)
    # for edge in _shape.edges:
    for edge in range(len(_shape.edges)):
        for vertex in _shape.edges[edge]:
            try:
                glColor3fv(_shape.colors[edge])
            except:
                glColor3fv(*_shape.colors)
            glVertex3fv(_shape.vertices[vertex].V)
    glEnd()

def draw_vertices(_shape : Shape):
    glBegin(GL_POINTS)
    for vertex in range(len(_shape.vertices)):
        try:
            glColor3fv(_shape.colors[vertex])
        except:
            glColor3fv(*_shape.colors)
        glVertex3fv(_shape.vertices[vertex].V)
    glEnd()

def draw(_shape : Shape):
    if _shape.surfaces is not None:
        draw_surfaces(_shape)
    elif _shape.edges is not None:
        draw_edges(_shape)
    elif _shape.vertices is not None:
        draw_vertices(_shape)


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -4)

    # OBJECTS.append(Shape(_shape_type=SHAPES['Triangle']))
    # OBJECTS.append(Shape(Matrix((-1, -1, 0), _is_vector=True), _shape_type=SHAPES['Point'], _color=COLORS['yellow']))
    # OBJECTS.append(Shape(Matrix((-2, 0, 0), _is_vector=True), _edge=1, _shape_type=SHAPES['Square']))
    OBJECTS.append(Shape(Matrix((0, 0, 0), _is_vector=True), _edge=1, _shape_type=SHAPES['Cube']))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        for obj in OBJECTS:
            draw(obj)

        pygame.display.flip()
        pygame.time.wait(10)

main() 