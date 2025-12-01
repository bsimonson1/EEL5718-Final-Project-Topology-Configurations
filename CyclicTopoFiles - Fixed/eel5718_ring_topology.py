#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import time

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    
    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', stp=True, cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch('s2', stp=True, cls=OVSKernelSwitch, failMode='standalone')
    s3 = net.addSwitch('s3', stp=True, cls=OVSKernelSwitch, failMode='standalone')
    s4 = net.addSwitch('s4', stp=True, cls=OVSKernelSwitch, failMode='standalone')
    s5 = net.addSwitch('s5', stp=True, cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)

    info( '*** Add links\n')
    # s1h1 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(s1, h1, cls=TCLink , **s1h1)
    # h2s1 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(h2, s1, cls=TCLink , **h2s1)
    # h3s1 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(h3, s1, cls=TCLink , **h3s1)
    # h4s2 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(h4, s2, cls=TCLink , **h4s2)
    # h6s2 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(h6, s2, cls=TCLink , **h6s2)
    # s2h5 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(s2, h5, cls=TCLink , **s2h5)
    # h7s3 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(h7, s3, cls=TCLink , **h7s3)
    # h8s3 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(h8, s3, cls=TCLink , **h8s3)
    # h9s3 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(h9, s3, cls=TCLink , **h9s3)
    # h10s4 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(h10, s4, cls=TCLink , **h10s4)
    # h11s4 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(h11, s4, cls=TCLink , **h11s4)
    # h12s4 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(h12, s4, cls=TCLink , **h12s4)
    # s5h13 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(s5, h13, cls=TCLink , **s5h13)
    # h14s5 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(h14, s5, cls=TCLink , **h14s5)
    # s5h15 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(s5, h15, cls=TCLink , **s5h15)
    # s1s2 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(s1, s2, cls=TCLink , **s1s2)
    # s2s3 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(s2, s3, cls=TCLink , **s2s3)
    # s3s4 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(s3, s4, cls=TCLink , **s3s4)
    # s4s5 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(s4, s5, cls=TCLink , **s4s5)
    # s5s1 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    # net.addLink(s5, s1, cls=TCLink , **s5s1)
    
    
    s1h1 = {'delay':'25ms','loss':1}
    net.addLink(s1, h1, cls=TCLink , **s1h1)
    h2s1 = {'delay':'25ms','loss':1}
    net.addLink(h2, s1, cls=TCLink , **h2s1)
    h3s1 = {'delay':'25ms','loss':1}
    net.addLink(h3, s1, cls=TCLink , **h3s1)
    h4s2 = {'delay':'25ms','loss':1}
    net.addLink(h4, s2, cls=TCLink , **h4s2)
    h6s2 = {'delay':'25ms','loss':1}
    net.addLink(h6, s2, cls=TCLink , **h6s2)
    s2h5 = {'delay':'25ms','loss':1}
    net.addLink(s2, h5, cls=TCLink , **s2h5)
    h7s3 = {'delay':'25ms','loss':1}
    net.addLink(h7, s3, cls=TCLink , **h7s3)
    h8s3 = {'delay':'25ms','loss':1}
    net.addLink(h8, s3, cls=TCLink , **h8s3)
    h9s3 = {'delay':'25ms','loss':1}
    net.addLink(h9, s3, cls=TCLink , **h9s3)
    h10s4 = {'delay':'25ms','loss':1}
    net.addLink(h10, s4, cls=TCLink , **h10s4)
    h11s4 = {'delay':'25ms','loss':1}
    net.addLink(h11, s4, cls=TCLink , **h11s4)
    h12s4 = {'delay':'25ms','loss':1}
    net.addLink(h12, s4, cls=TCLink , **h12s4)
    s5h13 = {'delay':'25ms','loss':1}
    net.addLink(s5, h13, cls=TCLink , **s5h13)
    h14s5 = {'delay':'25ms','loss':1}
    net.addLink(h14, s5, cls=TCLink , **h14s5)
    s5h15 = {'delay':'25ms','loss':1}
    net.addLink(s5, h15, cls=TCLink , **s5h15)
    s1s2 = {'delay':'25ms','loss':1}
    net.addLink(s1, s2, cls=TCLink , **s1s2)
    s2s3 = {'delay':'25ms','loss':1}
    net.addLink(s2, s3, cls=TCLink , **s2s3)
    s3s4 = {'delay':'25ms','loss':1}
    net.addLink(s3, s4, cls=TCLink , **s3s4)
    s4s5 = {'delay':'25ms','loss':1}
    net.addLink(s4, s5, cls=TCLink , **s4s5)
    s5s1 = {'delay':'25ms','loss':1}
    net.addLink(s5, s1, cls=TCLink , **s5s1)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([])
    net.get('s2').start([])
    net.get('s3').start([])
    net.get('s4').start([])
    net.get('s5').start([])

    info( '*** Post configure switches and hosts\n')


    info("Testing connection")
    net.pingAll()

    CLI(net)

if __name__ == '__main__':
    myNetwork()