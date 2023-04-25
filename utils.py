from math import pi, sin, cos, radians
from random import randint, random, uniform
from time import sleep

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from console import *

DEFAULT_RESOLUTION = (800, 800)
FPS_CAP = 100
FPS_COUNT = 0
CAM_POSITION = (0, 0, -14)
LIGHT_POSITION = -CAM_POSITION[2]

UNIFORM_DIRECTION_CAP = 0.1
UNIFORM_DIRECTION_AREA = (-UNIFORM_DIRECTION_CAP, UNIFORM_DIRECTION_CAP)
BORDER_COLLITION_CAP = 4.0

COLORS = {
	'white'		:	(1, 1, 1),
	'gray'		:	(.75, .75, .75),
	'dark_gray'	:	(.5, .5, .5),
	'black'		:	(0, 0, 0),

	'red'		:	(1, 0, 0),
	'green'		:	(0, 1, 0),
	'g_cage'	:	(0, 1, 0),
	'blue'		:	(0, 0, 1),
		
	'magenta'	:	(1, 0, 1),
	'yellow'	:	(1, 1, 0),
	'yellow_c'	:	(1, 0.75, 0),
	'cyan'		:	(0, 1, 1),
}