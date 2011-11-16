
from txosc import osc, async

def send_message(ring_leader, path):
    message = osc.Message(path, ring_leader.getuser())
    ring_leader.osc_sender


class Message():
    def __init__(self, path, *args):
        self.message = osc.Message(path, args)

    def send_message(request):
        request.oscSender.send_message(

class OscSender():
    def __init__(self, ring_leader, reactor, port, host='224.0.0.69'):
        self.port = port
        self.host = host
        self.client = async.DatagramClientProtocol()
        self._client_port = reactor.listenUDP(0, self.client)

        ring_leader.oscSender = self

        def send_message(self, oscMessage):
            self.client.send(oscMessage, (self.host, self.port))

