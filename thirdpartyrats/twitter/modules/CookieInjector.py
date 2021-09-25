
import math;
from datetime import datetime;
import random;
import cherrypy;

from modules.AESCipher import *;


def CookieInjector():
    print("Cookie injection!!!");
    nonce = str(math.floor(random.random()*100000000000000000))

    now = datetime.now();
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S");

    #encrypt tracking cookie value
    msg = 'Kuwait'+nonce;
    robcookie = AESCipher('kUw@1tHack3rZ!!!').encrypt(msg).decode('utf-8')
    cherrypy.response.cookie['KuwaitCyberCrimeCookie'] = robcookie;
    cherrypy.response.cookie['KuwaitCyberCrimeCookie']['Expires'] = 10000000000000000;
    cherrypy.response.cookie['KuwaitCyberCrimeCookie']['Path'] = '/';

    #decrypt cookie
    #AESCipher('kUw@1tHack3rZ!!!').decrypt(robcookie).decode('utf-8')
