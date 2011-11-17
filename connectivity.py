
from txosc import osc, async

def write_event(context, path):
    print path, context.getuser().uid
    #message = osc.Message(path, context.getuser())
    #context.event_writer.write_event(message)

class OscWriter():
    def __init__(self, reactor, port, host='224.0.0.69'):
        self.port = port
        self.host = host
        self.client = async.DatagramClientProtocol()
        self._client_port = reactor.listenUDP(0, self.client)

        def write_event(self, oscMessage):
            self.client.send(oscMessage, (self.host, self.port))

