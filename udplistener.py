#!/usr/bin/env python2.6

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.application.internet import MulticastServer

class MulticastServerUDP(DatagramProtocol):
    def startProtocol(self):
        print 'Started Listening'
        # Join a specific multicast group, which is the IP we will respond to
        self.transport.joinGroup('224.0.0.69')

    def datagramReceived(self, datagram, address):
        # The uniqueID check is to ensure we only service requests from ourselves
        print "Server Received:" + repr(datagram)

reactor.listenMulticast(16666, MulticastServerUDP())

reactor.run()


