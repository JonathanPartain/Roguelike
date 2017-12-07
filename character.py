from Tilemap import Tilemap
level = Tilemap()

class Character:
	
	
	def __init__(self, hp, attack, pos_x, pos_y):
		self.hp = hp
		self.attack = attack
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.inventory = []
		
		
