from math import pi, sin, cos, radians
from random import randint, random, uniform

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from console import *

FPS_CAP = 20
FPS_COUNT = 0
UNIFORM_DIRECTION_CAP = 0.05
UNIFORM_DIRECTION_AREA = (-UNIFORM_DIRECTION_CAP, UNIFORM_DIRECTION_CAP)

COLORS = {
	'white'		:	(1, 1, 1),
	'black'		:	(0, 0, 0),

	'red'		:	(1, 0, 0),
	'green'		:	(0, 1, 0),
	'blue'		:	(0, 0, 1),
		
	'magenta'	:	(1, 0, 1),
	'yellow'	:	(1, 1, 0),
	'yellow_c'	:	(1, 0.75, 0),
	'cyan'		:	(0, 1, 1),
}