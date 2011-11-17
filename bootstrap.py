#!/usr/bin/env python2.6

from twisted.web.server import Site, Request
from twisted.web.resource import Resource
from twisted.internet import reactor

from webserver import EventScheduler, Index
from connectivity import OscWriter

class RequestBootstrap(Request):
    """
    basically just for hooking to a request and setting some values
    """
    def __init__(self, *args, **kw):
        Request.__init(self, args, kw)
        self.context = Context()

class Context():
    """
    holds anything that everybody might find useful
    """
    def __init__(self, user, event_writer):
        uid = self.getSession().uid
        self.user = users.getuser(uid)
        self.event_writer = osc_writer

class Users():
    """
    glorified dict
    """
    def getuser(self, session_uid):
        user = self.session_uid_to_user[session_uid]
        if not user:
            user = User(session_uid)
            self.session_uid_to_user[session_uid] = user

        return user

class User():
    """
    any relevant user information
    """
    def __init__(self, session_uid):
        self.session_uid = session_uid
        self.uid = User.uid
        User.uid += 1
        print 'new user', self.uid

    def getid(self):
        return self.uid

User.uid = 0
users = Users()

index = Index()
index.putChild('e', EventScheduler())

site = Site(index)
site.requestFactory = RequestBootstrap # hook in our request

reactor.listenTCP(8080, site) # HTTP listener

osc_writer = OscWriter(reactor, 16666) # UDP(OSC) sender/receiver

reactor.run()

