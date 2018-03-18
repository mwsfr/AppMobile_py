class SpaceShip:
	# public ArrayList <Person> crew = new ArrayList<Person>()

	def __init__(self,name='unknown',fuel='',hull='',power='',robots='',missiles='',battleMode=False,scanner='',enemy='',roomList=[],crew=[]):
		self.name = name
		self.fuel=fuel
		self.hull=hull
		self.power=power
		self.robots=robots
		self.missiles=missiles
		self.battleMode=battleMode
		self.scanner=scanner
		self.enemy=enemy
		self.roomList=roomList
		self.crew=crew
	
	def showOptions(self):
		option=99
		while (option > 0):
			print('''
 Main Menu: 
   1 - Systems
   2 - Crew''')
			option = int(input('>'))