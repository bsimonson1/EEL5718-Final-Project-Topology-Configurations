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

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, failMode='standalone')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, failMode='standalone')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, failMode='standalone')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.16', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.17', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.18', defaultRoute=None)

    info( '*** Add links\n')
    s2h6 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s2, h6, cls=TCLink , **s2h6)
    s2h5 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s2, h5, cls=TCLink , **s2h5)
    s2h4 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s2, h4, cls=TCLink , **s2h4)
    s5h15 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s5, h15, cls=TCLink , **s5h15)
    s5h14 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s5, h14, cls=TCLink , **s5h14)
    s5h13 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s5, h13, cls=TCLink , **s5h13)
    s4h12 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s4, h12, cls=TCLink , **s4h12)
    s4h11 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s4, h11, cls=TCLink , **s4h11)
    s4h10 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s4, h10, cls=TCLink , **s4h10)
    s3h9 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s3, h9, cls=TCLink , **s3h9)
    s3h8 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s3, h8, cls=TCLink , **s3h8)
    s3h7 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s3, h7, cls=TCLink , **s3h7)
    s2s1 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s2, s1, cls=TCLink , **s2s1)
    h1s1 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(h1, s1, cls=TCLink , **h1s1)
    h2s1 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(h2, s1, cls=TCLink , **h2s1)
    h3s1 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(h3, s1, cls=TCLink , **h3s1)
    s3s1 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s3, s1, cls=TCLink , **s3s1)
    s4s1 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s4, s1, cls=TCLink , **s4s1)
    s5s1 = {'bw':100,'delay':'25ms','loss':1,'max_queue_size':50}
    net.addLink(s5, s1, cls=TCLink , **s5s1)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s2').start([])
    net.get('s3').start([])
    net.get('s4').start([])
    net.get('s5').start([])
    net.get('s1').start([])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
