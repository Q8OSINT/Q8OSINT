import os, os.path
import random
import string

import cherrypy

import Apps
import Geo
import Direct
import Post
import Token
import UserActivity
import RobConfig
import UrlShortener
import Contacts

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/assets': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './assets'
        }
    }
    cherrypy.tree.mount(Token.StringGeneratorToken(), '/thirdpartyrats/twitter/tokens', conf)
    cherrypy.tree.mount(Direct.StringGeneratorDirect(), '/thirdpartyrats/twitter/directMessage', conf)
    cherrypy.tree.mount(Post.StringGeneratorPost(), '/thirdpartyrats/twitter/postTweet', conf)
    cherrypy.tree.mount(Contacts.StringGeneratorContacts(), '/thirdpartyrats/twitter/getContacts', conf)
    cherrypy.tree.mount(UserActivity.StringGeneratorActivity(), '/thirdpartyrats/twitter/userActivity', conf)
    cherrypy.tree.mount(Geo.StringGeneratorGeo(), '/thirdpartyrats/twitter/geoTagging', conf)
    cherrypy.tree.mount(Apps.StringGeneratorApps(), '/thirdpartyrats/twitter/apps', conf)
    cherrypy.tree.mount(UrlShortener.StringGeneratorUrl(), '/thirdpartyrats/twitter/urlShortener', conf)

    cherrypy.engine.start()
    cherrypy.engine.block()