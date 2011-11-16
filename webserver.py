#!/usr/bin/env python2.6

from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

class Event(Resource):

    def __init__(self, eventType):
        Resource.__init__(self)
        self.eventType = eventType

    def render_GET(self, request):
        request.setHeader("context-type", "text/plain")
        return self.eventType + '+'

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
    def render_GET(self, request):
        return "welcome home"

root = RingLeader()
root.putChild('e', EventScheduler())

factory = Site(root)

reactor.listenTCP(8080, factory)
reactor.run()

