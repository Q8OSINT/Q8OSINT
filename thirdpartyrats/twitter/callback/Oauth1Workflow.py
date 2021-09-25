
from TwitterAPI import TwitterAPI
from datetime import datetime
import time
import base64
import random
import http.cookies
import requests
from callback.CallbackEnum import *;
import callback.GlobalFunctions;
import cherrypy;
from requests_oauthlib import OAuth1Session

OAUTH_CALLBACK = "http://kuwaithackers.dyndns.org:9999/thirdpartyrats/twitter/apps/callback";
REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
SIGNIN_URL = 'https://api.twitter.com/oauth/authenticate'

resource_owner_key = "";
resource_owner_secret = "";

@cherrypy.expose
def getRequestToken(consumer_key, consumer_secret):
    """Get an resource token for a given consumer key and secret.
    Args:
        consumer_key (str):
            Your application consumer key.
        consumer_secret (str):
            Your application consumer secret.
    Returns:
        (None)
    """
    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret, callback_uri=OAUTH_CALLBACK)
    cherrypy.session['oauth_client'] = oauth_client; #save

    print('\n[*] get oauth request tokens...\n')
    resp = oauth_client.fetch_request_token(REQUEST_TOKEN_URL)
    print("Request response: "+ str(resp));

    cherrypy.session['resource_owner_key'] = resp.get("oauth_token");
    cherrypy.session['resource_owner_secret'] = resp.get("oauth_token_secret");

    return getAuthorizationUrl();

@cherrypy.expose
def getAuthorizationUrl():
    oauth_client = cherrypy.session['oauth_client']; #restore
    if (oauth_client == ""):
        raise Exception("[!] oauth client is uninitialized.");
    url = oauth_client.authorization_url(AUTHORIZATION_URL)
    print("url::"+url)
    return url;

@cherrypy.expose
def getAccessToken(consumer_key, consumer_secret, oauth_verifier):

    if(oauth_verifier == ""):
        raise Exception("[!] oauth verifier is empty.");

    oauth = OAuth1Session(consumer_key,
                          client_secret=consumer_secret,
                          resource_owner_key=cherrypy.session['resource_owner_key'],
                          resource_owner_secret=cherrypy.session['resource_owner_secret'],
                          verifier=oauth_verifier)
    oauth_tokens = oauth.fetch_access_token(ACCESS_TOKEN_URL)
    return oauth_tokens;

"""
session.post(url, data=sessData)

date_default_timezone_set('Asia/Kuwait')
time_now = datetime.now()
time_now = str(time_now.strftime("%H%i%s%m%d%Y"))

base64_str = base64.b64encode(str(md5.md5(str(microtime())).hexdigest()))

cybercookie = "Kuwait,Chalk:" + time_now + "Sig:" + base64_str.rstrip()

nonce = str(random.randint(10000, 999999))

# time = datetime.datetime.now() + datetime.timedelta(days=1)

setcookie = http.cookies.SimpleCookie()

setcookie['name'] = "KuwaitCyberCrimeDetectionCookie" + nonce
setcookie['value'] = cybercookie
setcookie['path'] = '/'
setcookie['expires'] = int(time.time()) + 2592000000

# setcookie("KuwaitCyberCrimeDetectionCookie"+nonce, cybercookie, int(time.time())+2592000000,"/")
redirect(url)
"""