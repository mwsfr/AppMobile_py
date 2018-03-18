class SpaceShipRoom:
	def __init__(self,name='unknown',system=None, oxygenLevel=0, status=0):
		self.name=name
		self.system=system
		self.oxygenLevel=oxygenLevel
		self.status=status
	
	def info(self):
		if self.system == None:
			local_system=None
			local_system_info=''
		else:
			local_system=self.system.name
			local_system_info=self.system.info()
		r='''
  |- room: '''+str(self.name)+'''
       |- oxygen: '''+ str(self.oxygenLevel) +'''%
       |- status: '''+ str(self.status) +'''%
       |- system: '''+ str(local_system) + str(local_system_info)
		return r