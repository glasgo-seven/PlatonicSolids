class Cube :
	def __init__(self, _edge : float = 1, _position : tuple[float, float, float] = (0, 0, 0)) -> None:
		self.edge = _edge
		self.position = _position

		self.verticies = self.calculate_verticies()
		self.edges = self.calculate_edges()
		self.surfaces = self.calculate_surfaces()

	def calculate_verticies(self) -> tuple:
		x, y, z = self.position
		return (
			(x, y, z),
			(x, y + self.edge, z),
			(x + self.edge, y, z),
			(x + self.edge, y + self.edge, z),

			(x, y, z + self.edge),
			(x, y + self.edge, z + self.edge),
			(x + self.edge, y, z + self.edge),
			(x + self.edge, y + self.edge, z + self.edge)
		)

	def calculate_edges(self) -> tuple:
		return (
			(0, 1),
			(0, 2),
			(1, 3),
			(2, 3),

			(4, 5),
			(4, 6),
			(5, 7),
			(6, 7),

			(0, 4),
			(1, 5),
			(2, 6),
			(3, 7)
		)

	def calculate_surfaces(self) -> tuple:
		return (
			(0, 1, 2, 3),
			(4, 5, 6, 7),

			(0, 1, 5, 4),
			(2, 3, 7, 6),

			(0, 2, 6, 4),
			(1, 3, 7, 5)
		)





