#!/usr/bin/python

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

from mininet.topo import Topo

class AnilloSimple(Topo):
    def build(self, n=4):
        #Hosts
        h1 = self.addHost('h1', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', mac='00:00:00:00:00:02')
        h3 = self.addHost('h3', mac='00:00:00:00:00:03')
        h4 = self.addHost('h4', mac='00:00:00:00:00:04')
        h5 = self.addHost('h5', mac='00:00:00:00:00:05')
        h6 = self.addHost('h6', mac='00:00:00:00:00:06')
        h7 = self.addHost('h7', mac='00:00:00:00:00:07')
        h8 = self.addHost('h8', mac='00:00:00:00:00:08')

        #Switches
        s1 = self.addSwitch('s1', mac='00:00:00:00:00:09')
        s2 = self.addSwitch('s2', mac='00:00:00:00:00:10')
        s3 = self.addSwitch('s3', mac='00:00:00:00:00:11')
        s4 = self.addSwitch('s4', mac='00:00:00:00:00:12')

        #Links      self.addLink(src, dst, src_port, dst_port)
        self.addLink(h1, s1,    1,  9 )
        self.addLink(h2, s1,    2,  10)
        self.addLink(h3, s2,    3,  11)
        self.addLink(h4, s2,    4,  12)
        self.addLink(h5, s3,    5,  13)
        self.addLink(h6, s3,    6,  14)
        self.addLink(h7, s4,    7,  15)
        self.addLink(h8, s4,    8,  16)

        self.addLink(s1, s2,    17, 21)
        self.addLink(s2, s3,    18, 22)
        self.addLink(s3, s4,    19, 23)
        self.addLink(s4, s1,    20, 24)
"""

"""
class DosCaminos(Topo):
    def build(self):
        #Hosts
        h1 = self.addHost('h1', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', mac='00:00:00:00:00:02')
        h3 = self.addHost('h3', mac='00:00:00:00:00:03')
        h4 = self.addHost('h4', mac='00:00:00:00:00:04')
        h5 = self.addHost('h5', mac='00:00:00:00:00:05')
        h6 = self.addHost('h6', mac='00:00:00:00:00:06')

        #Switches
        s1 = self.addSwitch('s1', mac='00:00:00:00:00:07')
        s2 = self.addSwitch('s2', mac='00:00:00:00:00:08')
        s3 = self.addSwitch('s3', mac='00:00:00:00:00:09')
        s4 = self.addSwitch('s4', mac='00:00:00:00:00:10')
        s5 = self.addSwitch('s5', mac='00:00:00:00:00:11')

        #Links      self.addLink(src, dst, src_port, dst_port)
        self.addLink(h1, s1,    1,  7 )
        self.addLink(h2, s1,    2,  8 )
        self.addLink(h3, s2,    3,  9 )
        self.addLink(h4, s2,    4,  10)
        self.addLink(h5, s5,    5,  11)
        self.addLink(h6, s5,    6,  12)

        self.addLink(s1, s2,    13, 19)
        self.addLink(s2, s4,    14, 20)
        self.addLink(s4, s3,    15, 21)
        self.addLink(s3, s1,    16, 22)
        self.addLink(s5, s3,    17, 23)
        self.addLink(s5, s1,    18, 24)

topos = { 'doscaminos': ( lambda: DosCaminos() ),'anillo': ( lambda: AnilloSimple() )}