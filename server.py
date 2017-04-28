#!/usr/bin/python
import sys
from twisted.web.static import File
from twisted.python import log
from twisted.web.server import Site
from twisted.internet import reactor

from autobahn.twisted.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol

from autobahn.twisted.resource import WebSocketResource


class SomeServerProtocol(WebSocketServerProtocol):
    def onConnect(self, request):
    	print("connected")

    def onMessage(self, payload, isBinary):
    	print('response>'+payload)
	msg=raw_input('browser>')
	if(msg=='exit'):
		exit()
	self.sendMessage(msg)

if __name__ == "__main__":
    #log.startLogging(sys.stdout)

    # static file server seving index.html as root
    root = File(".")

    factory = WebSocketServerFactory(u"ws://192.168.1.11:8080")
    factory.protocol = SomeServerProtocol
    resource = WebSocketResource(factory)
    # websockets resource on "/ws" path
    root.putChild(u"ws", resource)

    site = Site(root)
    reactor.listenTCP(8080, site)
    reactor.run()
