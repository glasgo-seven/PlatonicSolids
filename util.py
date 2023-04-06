from math import pi

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import matrix

COLORS = {
	'white'		:	(1, 1, 1),
	'black'		:	(0, 0, 0),

	'red'		:	(1, 0, 0),
	'green'		:	(0, 1, 0),
	'blue'		:	(0, 0, 1),
		
	'magenta'	:	(1, 0, 1),
	'yellow'	:	(1, 1, 0),
	'yellow_c'	:	(1, 0.75, 0),
	'cian'		:	(0, 1, 1),
}

ANGLES = {
	'0'		:	0,
	'1'		:	pi / 90,
	'3'		:	pi / 30,
	'5'		:	pi / 18,
	'10'	:	pi / 9,
	'15'	:	pi / 6,
	'30'	:	pi / 3,
	'45'	:	pi / 2,
	'60'	:	pi * 2 / 3,
	'90'	:	pi,
	'180'	:	pi * 2,
	'360'	:	0,
}
