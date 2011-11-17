from twisted.web.resource import Resource

import connectivity

class Event(Resource):

    def __init__(self, eventType):
        Resource.__init__(self)
        self.eventType = eventType

    def render_GET(self, request):
        request.setHeader("context-type", "text/plain")
        connectivity.write_event(request.context, self.eventType)
        return '{"response": "ok"}'

    def render_POST(self, request):
        return self.eventType + '-'

class EventScheduler(Resource):
    def getChild(self, name, request):
        if name == '':
            return self

        return Event(name)

    def render_GET(self, request):
        return 'et phone home'

class Index(Resource):
    def render_GET(self, request):
        return 'welcome home'

