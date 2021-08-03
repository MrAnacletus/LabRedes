#!/usr/bin/python
from mininet.topo import Topo

"""
Comandos:
    Correr el POX:
        cd pox
        sudo ./pox.py --verbose openflow.spanning_tree --no-flood --hold-down openflow.discovery forwarding.l2_learning
    Run:
    Anillo simple:
        sudo mn --custom /home/shinobu/WorkSpace/Mininet/Lab/topos.py --topo anillo --controller remote --switch ovsk --mac
    Dos caminos:
        sudo mn --custom /home/shinobu/WorkSpace/Mininet/Lab/topos.py --topo doscaminos --controller remote --switch ovsk --mac
    Clean:
        sudo mn -c
    Change a connection:
        link s1 h1 down
        link s1 h1 up
        links
"""


class Net(Topo):
	def build(self):
		
		s1 = self.addSwitch('s1')
		h1 = self.addHost('h1', mac="00:00:00:00:00:01")
		h2 = self.addHost('h2', mac="00:00:00:00:00:02")
		self.addLink(h1,s1,1,1)
		self.addLink(h2,s1,1,2)
		
		s2 = self.addSwitch('s2')
		h3 = self.addHost('h3', mac="00:00:00:00:00:03")
		h4 = self.addHost('h4', mac="00:00:00:00:00:04")
		self.addLink(h3,s2,1,1)
		self.addLink(h4,s2,1,2)
		
		s5 = self.addSwitch('s5')
		h5 = self.addHost('h5', mac="00:00:00:00:00:05")
		h6 = self.addHost('h6', mac="00:00:00:00:00:06")
		self.addLink(h5,s5,1,1)
		self.addLink(h6,s5,1,2)
		
		s3 = self.addSwitch('s3')
		s4 = self.addSwitch('s4')
		
		self.addLink(s1, s2, 4, 3)
		self.addLink(s1, s3, 6, 5)
		self.addLink(s2, s4, 4, 3)
		self.addLink(s4, s3, 4, 3)
		self.addLink(s3, s5, 4, 3)
		self.addLink(s5, s1, 4, 3)

topos = {'topo_dos_caminos': (lambda:Net())}
