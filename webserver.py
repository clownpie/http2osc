#!/usr/bin/env python2.6

from twisted.web import server, resource
from twisted.internet import reactor

class Event(resource.Resource):
    def render_GET(self, request):
        request.setHeader("context-type", "text/plain")
        return ""

root = Resource()
root.putChild('e', Event())

factory = server.Site(root)

reactor.listenTCP(8080, factory)
reactor.run()
