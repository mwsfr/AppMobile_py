class SpaceShip:
	# public ArrayList <Person> crew = new ArrayList<Person>()

	def __init__(self,name='unknown',fuel=0,hull=0,power=0,robots=0,missiles=0,battleMode=False,enemy=None,room=[],crew=[]):
		self.name = name
		self.fuel=fuel
		self.hull=hull
		self.power=power
		self.robots=robots
		self.missiles=missiles
		self.battleMode=battleMode
		self.enemy=enemy
		self.room=room
		self.crew=crew
	
	def showOptions(self):
		option=99
		while (option > 0):
			print('''
 Main Menu: 
   1 - Systems
   2 - Crew''')
			option = int(input('>'))
			
	def info(self):
		rooms=''
		for i in self.room:
			rooms= rooms + i.info()
		r=str(self.name)+'''
  |- fuel: '''+str(self.fuel)+'''
  |- hull: '''+str(self.hull)+'''
  |- power: '''+str(self.power)+'''
  |- robots: '''+str(self.robots)+'''
  |- missiles: '''+str(self.missiles)+'''
  |- battleMode: '''+str(self.battleMode)+'''
  |- enemy: '''+str(self.enemy)+'''
  |- crew: '''+str(self.crew)+''''''+str(rooms)
		print(r)