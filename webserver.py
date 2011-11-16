#!/usr/bin/env python2.6

from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

from osc import OscSender

class Event(Resource):

    def __init__(self, eventType):
        Resource.__init__(self)
        self.eventType = eventType

    def render_GET(self, request):
        # TODO figure some way to hook into request and set requestgetuser
        user = ring_leader.getuser(request)
        request.setHeader("context-type", "text/plain")
        ring_leader.oscSender.send(

        return self.eventType + '+' + str(user.uid)

    def render_POST(self, request):
        return self.eventType + '-'

class EventScheduler(Resource):
    def getChild(self, name, request):
        if name == '':
            return self

        return Event(name)

    def render_GET(self, request):
        return 'et phone home'

class RingLeader(Resource):
    def __init__(self):
        Resource.__init__(self)
        self.uid_to_user = {}

    def getuser(self, request):
        if hasattr(request, 'user'):
            print 'existing user %s' % request.user.getid()
            return request.user

        uid = request.getSession().uid
        user = self.uid_to_user.get(uid)
        if not user:
            user = User(uid)
            self.uid_to_user[user.getid()] = user

        request.user = user
        return user

    def render_GET(self, request):
        return "welcome home number " + request.user.getid()

class User():
    def __init__(self, session_uid):
        self.session_uid = session_uid
        self.uid = User.uid
        User.uid += 1
        print 'new user', self.uid

    def getid(self):
        return self.uid

User.uid = 0

ring_leader = RingLeader()
ring_leader.putChild('e', EventScheduler())

factory = Site(ring_leader)
reactor.listenTCP(8080, factory)

ring_leader.oscSender = OscSender(reactor, 16666) # adds UDP listener to reactor

reactor.run()

