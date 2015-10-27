import urllib2
import socket
import socks
from stem import Signal 
from stem.control import Controller
import time


def connectTor():
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150, True)
	socket.socket = socks.socksocket

def newIdentity():
	socks.setdefaultproxy()
	with Controller.from_port(port = 9151) as controller:
		controller.authenticate()
		controller.signal(Signal.NEWNYM)
		
	
def main():
	while True:
		connectTor()
		print urllib2.urlopen('http://ip.42.pl/raw').read()
		newIdentity()
		# anything less you will get a repeated IP
		time.sleep(7)
    

if __name__ == "__main__":
	main()
