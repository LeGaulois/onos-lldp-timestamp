#!/usr/bin/python
# -*- coding: utf-8 -*-



from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.topolib import TreeTopo
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.topo import Topo
import sys

class reoptopo(Topo):
    """
    Creation d'une topologie perso
    constitue de 2 switch de tete et de n switchs
    d'accés. Chaque switchs d'accés est relié à:
        - 2 hotes
        - aux 2 switchs de têtes
    """
    def __init__(self, number=4, **opts):
        Topo.__init__(self, **opts)
        switchs = []

        for i in range(2):
            switchs.append(self.addSwitch('s%s' % (i) ) )
            
        self.addLink(switchs[0],switchs[1])
        self.addLink(switchs[0],switchs[1])
        
        hostnumber=0

        for i in range(number):
            switchs.append(self.addSwitch('sw-%s' % (i) ) )
            
            for k in range(2):
                h = self.addHost('h%s' % (hostnumber))
                self.addLink(switchs[-1], switchs[k])
                self.addLink(switchs[-1], h)
                hostnumber+=1
        


if __name__ == '__main__':
    setLogLevel('info')
    
    if( (len(sys.argv)>1) and ( type(sys.argv[1] is int ))):
        numbersw = int(sys.argv[1])
    else:
        numbersw=4

    mytopo = reoptopo(number=numbersw)    

    net = Mininet( topo=mytopo,controller=None,build=False )
    net.addController("c0",
                      controller=RemoteController,
                      ip="127.0.0.1",
                      port=6633)
    net.start()
    CLI( net )
    net.stop()
