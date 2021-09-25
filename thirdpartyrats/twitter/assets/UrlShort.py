import cherrypy
from TwitterAPI import TwitterAPI
import time;
import RobConfig;
from enum import Enum
import urllib3
import sys
import pyshorteners

class UrlShort(Enum):
    TINYURL = 1
    ISGDURL = 2
    CHILPIT = 3
    CLCKRU  = 4
    DAGD    = 5
    NULLPTR = 6
    OSDB    = 7
    QPSRU   = 8


    @cherrypy.expose
    def getShortenedUrl(url,type):
        #url= "http://www.yahoo.com"
        #type = UrlShort.TINYURL;
        shorturl = "";
        s = pyshorteners.Shortener()

        if(type == UrlShort.TINYURL):
            shorturl = s.tinyurl.short(url)
        elif(type == UrlShort.ISGDURL):
            shorturl = s.isgd.short(url)
        elif(type == UrlShort.CHILPIT):
            shorturl = s.chilpit.short(url)
        elif(type == UrlShort.CLCKRU):
            shorturl = s.clckru.short(url)
        elif(type == UrlShort.DAGD):
            shorturl = s.dagd.short(url)
        elif(type == UrlShort.NULLPTR):
            shorturl = s.nullpointer.short(url)
        elif(type == UrlShort.OSDB):
           shorturl = s.osdb.short(url)
        elif (type == UrlShort.QPSRU):
            shorturl = s.qpsru.short(url)

        return shorturl;

    @cherrypy.expose
    def reverseLookup(urlString):
        if(urlString == "tinyurl"):
            return UrlShort.TINYURL;
        elif(urlString == "isgdurl"):
            return UrlShort.ISGDURL;
        elif(urlString == "chilpit"):
            return UrlShort.CHILPIT;
        elif(urlString == "clckru"):
            return UrlShort.CLCKRU;
        elif(urlString == "dagd"):
            return UrlShort.DAGD;
        elif(urlString == "nullptr"):
            return UrlShort.NULLPTR;
        elif(urlString == "osdb"):
            return UrlShort.OSDB;
        elif(urlString == "qpsru"):
            return UrlShort.QPSRU;

    @cherrypy.expose
    def shorten(apiurl, url):
        http = urllib3.PoolManager()
        urllib3.disable_warnings()
        r = http.request('GET', apiurl + url)
        return r.data;

