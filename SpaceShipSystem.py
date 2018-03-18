class SpaceShipSystem:
	__init__(self,powerRequired='',missilesRequired='',robotsRequired='',timeRequired='',counter='',power='',item='',health='',name='unknown',status='stopped',load='',ship='',robot='',missiles='',target='',attackSystem='',atackPower='',defensePower=''):
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
		self.ship=ship
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
		elif self.ship.power < self.powerRequired:
			r=False
			print('Insuficient power!')
		elif self.ship.robot < self.robotRequired:
			r=False
			print('Insuficient robots!')
		elif self.ship.missiles < self.missilesRequired:
			r=False
			print('Insuficient missiles!')
		return r
			
	def start(self):
		self.start='started'
		self.power=self.powerRequired
		self.ship.power=self.ship.power - self.powerRequired
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