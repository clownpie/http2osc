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
        Request.__init__(self, *args, **kw)
        self.context = Context(self)

class Context():
    """
    holds anything that everybody might find useful
    """
    def __init__(self, request):
        self.event_writer = osc_writer
        self.request = request

    def getuser(self):
        if not hasattr(self, 'user'):
            session_uid = self.request.getSession().uid
            self.user = users.getuser(session_uid)

        return self.user

class Users():
    """
    glorified dict
    """
    def __init__(self):
        self.session_uid_to_user = {}

    def getuser(self, session_uid):
        if session_uid not in self.session_uid_to_user:
            user = User(session_uid)
            self.session_uid_to_user[session_uid] = user

        return self.session_uid_to_user[session_uid]

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

