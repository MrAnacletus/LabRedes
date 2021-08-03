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
		self.addLink(h1,s1,17,1)
		self.addLink(h2,s1,18,2)
		
		s2 = self.addSwitch('s2')
		h3 = self.addHost('h3', mac="00:00:00:00:00:03")
		h4 = self.addHost('h4', mac="00:00:00:00:00:04")
		self.addLink(h3,s2,19,5)
		self.addLink(h4,s2,20,6)
		
		s3 = self.addSwitch('s3')
		h5 = self.addHost('h5', mac="00:00:00:00:00:05")
		h6 = self.addHost('h6', mac="00:00:00:00:00:06")
		self.addLink(h5,s3,21, 9)
		self.addLink(h6,s3,22,10)
		
		s4 = self.addSwitch('s4')
		h7 = self.addHost('h7', mac="00:00:00:00:00:07")
		h8 = self.addHost('h8', mac="00:00:00:00:00:08")
		self.addLink(h7,s4,23,13)
		self.addLink(h8,s4,24,14)
		
		self.addLink(s1, s2, 3, 4)
		self.addLink(s2, s3, 7, 8)
		self.addLink(s3, s4, 11, 12)
		self.addLink(s4, s1, 15, 16)

topos = {'topo_circular': (lambda:Net())}
