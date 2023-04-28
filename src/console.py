def clear_console() -> None :
	from os import system, name
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def clear_screen() -> None :
	print('\x1b[H\x1b[3J', end='')
	print('\n'*64)
	print('\x1b[H\x1b[3J', end='')


RESET_COLOR = '0'

FOREGROUND_COLORS = {
	'black'		: '30',
	'red'		: '31',
	'green'		: '32',
	'yellow'	: '33',
	'blue'		: '34',
	'purple'	: '35',
	'cian'		: '36',
	'white'		: '37'
}
FOREGROUND_COLORS_STRONG = {
	'black'		: '90',
	'red'		: '91',
	'green'		: '92',
	'yellow'	: '93',
	'blue'		: '94',
	'purple'	: '95',
	'cian'		: '96',
	'white'		: '97'
}

BACKGROUND_COLORS = {
	'on_black'	: '40',
	'on_red'	: '41',
	'on_green'	: '42',
	'on_yellow'	: '43',
	'on_blue'	: '44',
	'on_purple'	: '45',
	'on_cian'	: '46',
	'on_white'	: '47'
}
BACKGROUND_COLORS_STRONG = {
	'on_black'	: '100',
	'on_red'	: '101',
	'on_green'	: '102',
	'on_yellow'	: '103',
	'on_blue'	: '104',
	'on_purple'	: '105',
	'on_cian'	: '106',
	'on_white'	: '107'
}

def set_color(fg : str = None, bg : str = None) -> None:
	if fg:
		print(f"\x1b[{fg}m", end='')
	if bg:
		print(f"\x1b[{bg}m", end='')

def reset_color() -> None:
	print(f"\x1b[{RESET_COLOR}m", end='')

def colored(*msgs : tuple[str], fg : str = None, bg : str = None) -> None:
	set_color(fg, bg)
	print(*msgs)
	reset_color()

def as_colored(text : str, fg : str = RESET_COLOR, bg : str = RESET_COLOR) -> str :
	return f"\x1b[{fg};{bg}m{text}\x1b[0m"


# def error(msg : str) -> None :
# 	print(f"\x1b[{FOREGROUND_COLORS['red']}m{msg}\x1b[0m")

def error(*msgs : tuple[str]) -> None:
	colored(*msgs, fg=FOREGROUND_COLORS_STRONG['red'])

def as_error(text : str) -> str :
	return as_colored(text, fg=FOREGROUND_COLORS_STRONG['red'])

# def alert(msg : str) -> None :
# 	print(f"\x1b[{FOREGROUND_COLORS['yellow']}m{msg}\x1b[0m")

def alert(*msgs : tuple[str]) -> None:
	colored(*msgs, fg=FOREGROUND_COLORS_STRONG['yellow'])

def as_alert(text : str) -> str :
	return as_colored(text, fg=FOREGROUND_COLORS_STRONG['yellow'])


if __name__ == '__main__':
	abc = 123
	print(abc)
	print(*[1, 2, 3, 4, 5])

	alert(abc)
	alert(abc, 'abc')

	error(abc)
	error(abc, 'abc')
