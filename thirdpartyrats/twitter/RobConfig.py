import cherrypy;
import urllib.request
import socket

direct_messages = []
tweets = []

#Network connection config
machine_ip = ""
try:
    #Local ip via wifi
    hostname = socket.gethostname()
    machine_ip = socket.gethostbyname(hostname)
except:
    #Local ip via lan
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    machine_ip = s.getsockname()[0]

public_ip = urllib.request.urlopen('https://ident.me').read().decode('utf-8')

cherrypy.config.update({
    'server.socket_host' : machine_ip,
    'server.socket_port' : 9999,
})

