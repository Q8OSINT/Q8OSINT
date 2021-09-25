import os, os.path
import random
import string
from assets.getTokens import *
from TwitterAPI import TwitterAPI

import cherrypy


class StringGeneratorPost(object):
    @cherrypy.expose
    def index(self):
        tokens_list = getTokens();
        consumer_key=''
        if ("consumer_key" not in cherrypy.session.keys() or cherrypy.session['consumer_key'] == ""):
            raise cherrypy.HTTPRedirect("/thirdpartyrats/twitter/tokens");
        else:
            consumer_key = cherrypy.session["consumer_key"];

        return """<!DOCTYPE html>
               <html>
               <head>
                  <title> روب ROB </title>
                  <meta name="description" content="website description" />
                  <meta name="keywords" content="website keywords, website keywords" />
                  <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
                  <meta http-equiv="Pragma" content="no-cache">
                  <meta http-equiv="Expires" content="-1">
                  <meta http-equiv="CACHE-CONTROL" content="NO-CACHE">
                  <link rel="stylesheet" type="text/css" href="assets/css/style.css" />
                  <link rel='stylesheet' id='theme53935-css' href='http://livedemo00.template-help.com/wordpress_53935/wp-content/themes/theme53935/main-style.css' type='text/css' media='all'/>
                  <!-- modernizr enables HTML5 elements and feature detects -->
                  <script type="text/javascript" src="assets/js/modernizr-1.5.min.js"></script>
               </head>
                  <body>
                     <div id="main">
                        <header>
                           <div id="logo">
                              <a href="Token.html"><img id="logo1" src="assets/images/kuwaithackers.jpeg" alt="ROB روب""><img id="logo2" src="assets/images/logo.png" alt="ROB روب""></a>
                           </div>
                           <!--close welcome-->          
                        </header>
                        <nav>
                           <div id="menubar">
                              <ul id="nav">
                              <li><a href="/thirdpartyrats/twitter/tokens">TOKEN</a></li>
                              <li><a href="/thirdpartyrats/twitter/directMessage">DIRECT-MESSAGE</a></li>
                              <li class="current"><a href="/thirdpartyrats/twitter/postTweet">TWEETS</a></li>
                              <li><a href="/thirdpartyrats/twitter/getContacts">CONTACTS</a></li>
                              <li><a href="/thirdpartyrats/twitter/userActivity">USER-ACTIVITY</a></li>
                              <li><a href="/thirdpartyrats/twitter/geoTagging">GEO-TAG</a></li>
                              <li><a href="/thirdpartyrats/twitter/apps">TWITTER-APPS</a></li>
                              <li><a href="/thirdpartyrats/twitter/urlShortener">URL-SHORTENER</a></li>
                              </ul>
                           </div>
                           <!--close menubar-->  
                        </nav>
                        <div id="site_content">
                           <div class="sidebar_container">
                              <div class="sidebar">
                                 <div style="text-align: center;">
                                    <span style="font-weight: bold;">
                                       <h2>&#1604;&#1608;&#1581;&#1577;
                                          &#1575;&#1604;&#1578;&#1581;&#1603;&#1605; &#1604;&#1578;&#1591;&#1576;&#1610;&#1602;&#1575;&#1578;
                                          &#1578;&#1608;&#1578;&#1610;&#1585;&nbsp;&nbsp;&nbsp;<br>Captured tokens
                                       </h2>
                                    </span>
                                    <br>
                                    <br>
                                    <br>
                               <form method="post" action="javascript:;">
                                  <select size="12" id="tokenlist" name="tokenlist" style="width: 70%; padding: 10px; margin-bottom: 10px;">
                                  """+tokens_list+"""
                                  </select>
                                  <br>
                                  <input onclick="handleSelectedToken()" type="submit" value="Load Token"/>
                               </form>
                                    <br>
                                 </div>
                              </div>
                              <!--close sidebar-->    
                           </div>
                           <!--close sidebar_container-->  
                           <div id="content" class="container_direct_message" style="padding-top: 10px;">
                              <form method="post" action="executePost" name="tweet" id="tweetform" style="margin-left: 150px;">
                                 <h1 style="font-weight: bold; margin-bottom: 10px; margin-top: 13px; color: #f1f1f1;">Post Tweet </h1>
                                 <label>Message: </label><br><br>
                                 <textarea rows="12" id="dmTextArea" name="dmTextArea" style="width: 380px; margin-bottom: 6px;"></textarea>
                                 <br>
                                  <input form="tweetform" type="submit" style="width: 110px; margin-left: 150px;" value="Submit"/>
                              </form>
                           </div>
                           <!--close content-->   
                        </div>
                        <!--close site_content-->    
                        <footer>
                        </footer>
                     </div>
                     <!--close main-->
                     <style type="text/css">
                        #tokenlist option{
                          font-size: 16px;
                          font-family: "Open Sans", sans-serif;
                        }
                        #tokenlist, #dmTextArea{
                          border: 4px ridge white;
                        }
                        #dmTextArea{
                          border-radius: 10px;
                        }
                     </style>
                     <!-- javascript at the bottom for fast page loading -->
                     <script type="text/javascript" src="assets/js/jquery.min.js"></script>
                     <script type="text/javascript" src='assets/js/getTokenDetails.js'></script>
                    <script>
                    function handleSelectedToken(){
                    var selector = document.getElementById('tokenlist');
                    var selectedToken = selector[selector.selectedIndex].value;
                    getTokenDetails('"""+consumer_key+"""')
                    }
                    </script>
                  </body>
               </html>"""

    @cherrypy.expose
    def executePost(self, dmTextArea=None):
        #check if cherrypy session is initialized otherwise reload token
        if(cherrypy.session['consumer_key']==""):
            raise cherrypy.HTTPRedirect("/thirdpartyrats/twitter/tokens");
        else:
            api = TwitterAPI(cherrypy.session['consumer_key'] ,cherrypy.session['consumer_secret'],cherrypy.session['oauth_token'],cherrypy.session['oauth_secret'])
            r = api.request('statuses/update', {'status': dmTextArea})
            raise cherrypy.HTTPRedirect("/thirdpartyrats/twitter/postTweet")

