class SpaceShipSystem:
	def __init__(self,powerRequired=0,missilesRequired=0,robotsRequired=0,timeRequired=0,counter=0,power=0,item=0,health=0,name='unknown',status='stopped',load=False,robot=0,missiles=0,target=None,attackSystem=False,atackPower=0,defensePower=0):
		self.powerRequired=powerRequired
		self.missilesRequired=missilesRequired
		self.robotsRequired=robotsRequired
		self.timeRequired=timeRequired
		self.counter=counter
		self.power=power
		self.item=item
		self.health=health
		self.name=name
		self.status=status
		self.load=load
		self.robot=robot
		self.missiles=missiles
		self.target=target
		self.attackSystem=attackSystem
		self.atackPower=atackPower
		self.defensePower=defensePower	

	def isReadyToStart(self):
		r = True
		if self.health<100:
			r=False
			print(self.name+' is damaged!')
		#elif self.ship.power < self.powerRequired:
		#	r=False
		#	print('Insuficient power!')
		#elif self.ship.robot < self.robotRequired:
		#	r=False
		#	print('Insuficient robots!')
		#elif self.ship.missiles < self.missilesRequired:
		#	r=False
		#	print('Insuficient missiles!')
		return r
			
	def start(self):
		self.status='started'
		self.power=self.powerRequired
		#self.ship.power=self.ship.power - self.powerRequired
		print(self.name+' started')
	
	def initialOptions(self):
		option=99
		while option>0:
			print(self.name+''' Menu:
  1 - Start''')
			option=int(input('> '))
			if option==1 and self.isReadyToStart():
				self.start()
				option=0
				
	def readyOption(self):
		option=99
		while option>0:
			print(self.name+''' Menu:
  1 - Stop system''')
			if self.attackSystem:
				print('''2 - Select target
  3 - Fire''')
		option=int(input('> '))
		
		
	def showOptions(self):
		if self.status=='stopped':
			self.initialOptions()
		else:
			self.readyOption()
	
	def info(self):
		r='''
           |- health: '''+str(self.health)+'''
           |- status: '''+str(self.status)+'''
           |- power: '''+str(self.power)+'''
           |- robot: '''+str(self.robot)+'''
           |- missiles: '''+str(self.missiles)+'''
           |- atackPower: '''+str(self.atackPower)+'''
           |- defensePower: '''+str(self.defensePower)+'''
           |- timeRequired: '''+str(self.timeRequired)+'''
           |- powerRequired: '''+str(self.powerRequired)+'''
           |- missilesRequired: '''+str(self.missilesRequired)+'''
           |- robotsRequired: '''+str(self.robotsRequired)+'''
           |- load: '''+str(self.load)+'''
           |- target: '''+str(self.target)
		return r