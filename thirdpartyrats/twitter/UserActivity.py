import os, os.path
import random
import string

import RobConfig
from assets.getTokens import *
from assets.getDirectMessages import *
from TwitterAPI import TwitterAPI
from assets.getTweets import getTweets
import re;
import cherrypy


class StringGeneratorActivity(object):
    @cherrypy.expose
    def index(self):
        consumer_key=''
        if ("consumer_key" not in cherrypy.session.keys() or cherrypy.session['consumer_key'] == ""):
            raise cherrypy.HTTPRedirect("/thirdpartyrats/twitter/tokens");
        else:
            consumer_key = cherrypy.session["consumer_key"];

        tokens_list = getTokens();

        #intitialization
        if ("messageType" not in cherrypy.session.keys()):
            cherrypy.session["messageType"]='';
        if("activityList" not in cherrypy.session.keys()):
            cherrypy.session["activityList"]='';
        if ("tweetList" not in cherrypy.session.keys()):
            cherrypy.session["tweetList"]='';
        if "msgText" not in cherrypy.session.keys():
            cherrypy.session["msgText"]='';

        if RobConfig.direct_messages == []:
            cherrypy.session["activityList"] = getDirectMessages();
        if RobConfig.tweets == []:
            cherrypy.session["tweetList"] = getTweets(cherrypy.session['screen_name']);

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
               <body onload="loadActivitySearch()">
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
                              <li class="current"><a href="/thirdpartyrats/twitter/userActivity">USER-ACTIVITY</a></li>
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
                        <div id="content" class="container_direct_message" style="width: 600px; padding-top: 10px;">
                           <h1 id="activityTitle" style="font-weight: bold; margin-left: 150px; margin-bottom: 10px; margin-top: 13px; color: #f1f1f1;">List Direct Messages</h1>
                           <form method="post" action="/thirdpartyrats/twitter/userActivity/getMessageText" name="directForm" id="directForm" style="width: 650px; padding-left: 150px;">
                              <label>Messages: </label><br>
                               <select id="dmlist" name="dmlist" size="5" style="width: 500px; margin-bottom: 6px;">"""+cherrypy.session["activityList"]+"""</select>
                               <input type="hidden" name="messageType" id="messageType" value="dm">
                               <textarea rows="10" name="directmsgsTextArea" id="directmsgsTextArea" style="width: 500px; margin-bottom: 6px;">"""+cherrypy.session["msgText"]+"""</textarea><br>
                                <br>
                              <input form="directForm" value="Load Text" name="activityButton" id="activityButton" type="submit" style="margin-left: 350px;">
                           </form>
                           <input type="radio" name="activityRadio" id="activityDM" checked=checked onchange=changeActivitySearch() value="dm" style="margin-left: 140px;"> Direct Messages &emsp;&emsp;<input type="radio" name="activityRadio" onchange=changeActivitySearch() id="activityTweet" value="tweet"> Tweets <br>
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
                     #tokenlist, #directmsgsTextArea{
                       border: 4px ridge white;
                     }
                     #directmsgsTextArea{
                       border-radius: 10px;
                     }
                  </style>

                  <!-- javascript at the bottom for fast page loading -->
                  <script type="text/javascript" src="assets/js/jquery.min.js"></script>
                <script>
                
                function handleSelectedToken(){
                    var selector = document.getElementById('tokenlist');
                    var selectedToken = selector[selector.selectedIndex].value;
                    getTokenDetails('"""+consumer_key+"""')
                }
                
                function loadActivitySearch(){
                    if(\""""+cherrypy.session["messageType"]+"""\" == "dm"){
                        document.getElementById('activityDM').checked = true;
                    } else if(\""""+cherrypy.session["messageType"]+"""\" == "tweet"){
                        document.getElementById('activityTweet').checked = true;
                    }
                    changeActivitySearch()
                }

                function changeActivitySearch(){
                    if(document.getElementById('activityDM').checked) {
                        //DM radio button is checked
                        document.getElementById('activityTitle').innerText = "List Direct Messages";
                        document.getElementById('messageType').value = "dm";
                        $('#dmlist').html(' """+cherrypy.session["activityList"]+""" ');
                    }else if(document.getElementById('activityTweet').checked) {
                        //Tweet radio button is checked
                        document.getElementById('activityTitle').innerText = "List User Tweets"
                        document.getElementById('messageType').value = "tweet";
                        $('#dmlist').html(' """+cherrypy.session["tweetList"]+""" ');
                    }
                }
                 
                 </script>
               </body>
            </html>"""

    @cherrypy.expose
    def getMessageText(self, messageType, activityButton, directmsgsTextArea):
        #No selection in the list return back
        raise cherrypy.HTTPRedirect("/thirdpartyrats/twitter/userActivity");

    @cherrypy.expose
    def getMessageText(self, messageType, activityButton, directmsgsTextArea, dmlist):
        #Parse the list item text and call to initialize the text
        r = re.compile(" ");
        p = r.split(dmlist);
        p = [x for x in p if x]; # remove empty items
        timestamp_printable = p[0]+" "+p[1]+" "+p[2]+" "+p[3]+" "+p[4];
        timestamp_no_space = timestamp_printable.replace(" ", ""); #remove spaces for variable space comparison

        if(messageType == "dm"):
            sender = p[6][:-1];
            receiver = p[8];
            cherrypy.session["messageType"] = "dm"

            def messageFilter(sender, receiver, timestamp):
                def messageFilterInternal(record):
                    return (record["sender_name"] == sender and record["recipient_name"] == receiver and record["timestamp"].replace(" ", "") == timestamp)
                return messageFilterInternal

            filterResults = filter(messageFilter(sender=sender, receiver=receiver, timestamp=timestamp_no_space),RobConfig.direct_messages)
            for record in filterResults:
                cherrypy.session["msgText"] = "Timestamp: " + str(timestamp_printable) + "\n" +"Sender: (" + record['sender_id'] + ", " + sender + ")\n" + "Receiver: (" + record['recipient_id'] + ", " + receiver + ")\n\nText:\n" + record["text"];

        elif (messageType == "tweet"):
            cherrypy.session["messageType"] = "tweet"
            timestamp_printable = timestamp_printable + " "+ p[5];
            timestamp_no_space = timestamp_printable.replace(" ",""); #remove spaces for variable space comparison
            sender = p[7];

            def messageFilter2(sender, timestamp):
                def messageFilterInternal2(record):
                    return (record["user_name"] == sender and record["timestamp"].replace(" ", "") == timestamp)
                return messageFilterInternal2

            filterResults = filter(messageFilter2(sender=sender, timestamp=timestamp_no_space), RobConfig.tweets)

            for record in filterResults:
                cherrypy.session["msgText"] = "Timestamp: " + str(timestamp_printable) + "\n" +"Sender: (" + str(record['user_id']) + ", " + sender + ")\n\nText:\n" + record["text"];
        raise cherrypy.HTTPRedirect("/thirdpartyrats/twitter/userActivity");
