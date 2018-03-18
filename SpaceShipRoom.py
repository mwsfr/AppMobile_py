class SpaceShipRoom:
	def __init__(self,name='unknown',system=None, oxygenLevel=0, status=0):
		self.name=name
		self.system=system
		self.oxygenLevel=oxygenLevel
		self.status=status
	
	def info(self):
		if self.system == None:
			local_system=None
		else:
			local_system=self.system.name
		print('----------------------------')
		print(str(self.name)+''':
  |- system: '''+ local_system +'''
  |- oxygen: '''+ str(self.oxygenLevel) +'''%
  |- status: '''+ str(self.status) +'''%
----------------------------''')