class SpaceShip:
	# public ArrayList <SpaceShipRoom> roomList = new ArrayList<SpaceShipRoom>()
	# public ArrayList <Person> crew = new ArrayList<Person>()

	def __init__(self,name='unknown',fuel='',hull='',power='',robots='',missiles='',battleMode='',scanner='',enemy=''):
		self.name = name
		self.fuel=fuel
		self.hull=hull
		self.power=power
		self.robots=robots
		self.missiles=missiles
		self.battleMode=battleMode
		self.scanner=scanner
		self.enemy=enemy
	
	def showOptions(self):
		option=99
		while (option > 0):
			print('''
 Main Menu: 
   1 - Systems
   2 - Crew''')
			option = int(input('>'))