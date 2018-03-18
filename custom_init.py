import sys
sys.path.insert(0,'C:\\Users\\marcosreis\\Documents\\M\\MobileApp_v1\\py')
from SpaceShip import SpaceShip
from SpaceShipRoom import SpaceShipRoom
from SpaceShipSystem import SpaceShipSystem

ss = SpaceShipSystem(powerRequired=10,missilesRequired=0,robotsRequired=0,timeRequired=10,counter=0,power=0,item=0,health=100,name='Oxygen System I',status='stopped',load=False,robot=0,missiles=0,target=None,attackSystem=False,atackPower=0,defensePower=0)
ss2 = SpaceShipSystem(powerRequired=10,missilesRequired=1,robotsRequired=0,timeRequired=10,counter=0,power=0,item=0,health=100,name='Missile System I',status='stopped',load=False,robot=0,missiles=0,target=None,attackSystem=True,atackPower=10,defensePower=0)

sr = SpaceShipRoom('Room A',ss)
sr2 = SpaceShipRoom('Room B',ss2)
s = SpaceShip('Falcon',10,20,30,40,50,False,None,room=[sr,sr2],crew=[])
s.info()