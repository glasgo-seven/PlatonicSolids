def reshu(a, b):
	x = 1 if a%2 == 0 or b%2 == 0 else 0
	return int(abs(b - a) / 2 + x)

def reshu_x(a, b):
	n = 0
	for x in range(a, b + 1):
		if x % 2 == 0 :
			n += 1
	return n

def reshu_a() -> int:
	x = int(input())
	s = 0
	while x != 0:
		if x % 4 == 0 and x % 10 == 8:
			s += x
		x = int(input())
	return s


if __name__ == '__main__':
	# a = int(input('a: '))
	# b = int(input('b: '))
	# print(reshu(a, b))
	# print(reshu_x(a, b))
	print(reshu_a())