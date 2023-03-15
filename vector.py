class Vector3:
	def __init__(self, _x : float, _y : float, _z : float) -> None:
		self.x = _x
		self.y = _y
		self.z = _z
		self.V = tuple(_x, _y, _z)

	def __add__(self, _V : Vector) -> Vector:
		return Vector((self.x + _V.x, self.y + _V.y, self.z + _V.z))
