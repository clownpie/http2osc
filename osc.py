
from txosc import osc

class OscSender():
    def __init__(self, port, host='224.0.0.69'):
        self.port = port
        self.host = host
        self.client = async.DatagramClientProtocol()
        self._client_port = reactor.listenUDP(0, self.client)

        def send_message(self, oscMessage):
            self.client.send(oscMessage, (self.host, self.port))

