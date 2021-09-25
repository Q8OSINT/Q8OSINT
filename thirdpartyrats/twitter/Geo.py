import os, os.path
import random
import string
from assets.getTokens import *
import pandas as pd
import folium
import cherrypy



class StringGeneratorGeo(object):
    @cherrypy.expose
    def index(self):
        tokens_list = getTokens()

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
                    <link rel="stylesheet" type="text/css" href="assets/css/style.css" />
                    <link rel='stylesheet' id='theme53935-css' href='http://livedemo00.template-help.com/wordpress_53935/wp-content/themes/theme53935/main-style.css' type='text/css' media='all'/>
                    <!-- modernizr enables HTML5 elements and feature detects -->
                    <script type="text/javascript" src="assets/js/modernizr-1.5.min.js"></script>
                    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.js"></script>
                    <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
                    
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.css"/>
                                        
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
                    
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
                              <li><a href="/thirdpartyrats/twitter/postTweet">TWEETS</a></li>
                              <li><a href="/thirdpartyrats/twitter/getContacts">CONTACTS</a></li>
                              <li><a href="/thirdpartyrats/twitter/userActivity">USER-ACTIVITY</a></li>
                              <li class="current"><a href="/thirdpartyrats/twitter/geoTagging">GEO-TAG</a></li>
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
                             <article id="center_bar" class="center_bar">
                                <div class="d-block d-block-system g-main">
                                   <!--Google Maps -->
                                   <div style="text-align: left;">
                                      <h1 style="font-weight: bold; margin-bottom: 20px; margin-top: 23px; color: #f1f1f1;">Geo Tagging </h1>
                                      <script>
                                         function getLocationDetails(e){
                                             e.preventDefault()
                                             var select = document.getElementById('locationlist');
                                             var locationPoint = select.options[select.selectedIndex].text;
                                             
                                             /** parse location point and pass to map **/
                                             var parseArray = locationPoint.split(':');
                                             
                                             var parseArray2 = parseArray[1].split(' ');
                                             var parseArray3 = parseArray[2].split(' ');
                                             
                                             var lat = parseArray2[1];
                                             var long = parseArray3[1];
                                             //window.localStorage["lat"] = lat;
                                             //window.localStorage["long"] = long;
                                             
                                            //checking map
                                            var container = L.DomUtil.get('latlongmap');
                                            if (container != null) {
                                                container._leaflet_id = null;
                                            }

                                            var gl_map = L.map(
                                                "latlongmap", {
                                                center: [lat, long],
                                                crs: L.CRS.EPSG3857,
                                                zoom: 12,
                                                zoomControl: true,
                                                preferCanvas: false,
                                                }
                                            );

                                        var tile_layer = L.tileLayer(
                                            "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
                                            "attribution": "",
                                            "detectRetina": false,
                                            "maxNativeZoom": 18,
                                            "maxZoom": 18,
                                            "minZoom": 0,
                                            "noWrap": false,
                                            "opacity": 1,
                                            "subdomains": "abc",
                                            "tms": false
                                            }
                                        ).addTo(gl_map);
                                        L.marker([lat, long]).addTo(gl_map);
                                      }
                                      </script>
                                      <div id="latlongmap" style="width:55%; height:285px; float: left;"></div>
                                      <form method="post" action="javascript:;" onsubmit="getLocationDetails(event)" style="width: 35%; margin-left: 2%; float: left;">
                                         <select size="10" id="locationlist" name="locationlist" style="width: 100%; height: 245px;">
                                            <option>lat: 29.28538087 long: 48.00550236 datetime:</option>
                                            <option>lat: 29.32861328 long: 47.98127228 datetime:</option>
                                         </select>
                                         <input type="submit" value="Load Location" style="margin-left: 62px;" />
                                      </form>
                                   </div>
                                </div>
                             </article>
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
                       #latlongmap{
                         border: 4px ridge white;
                         border-radius: 10px;
                       }
                       #dmTextArea{
                         border-radius: 10px;
                       }
                    </style>
                    
                <script>               
                function handleSelectedToken(){
                    var selector = document.getElementById('tokenlist');
                    var selectedToken = selector[selector.selectedIndex].value;
                    getTokenDetails('"""+consumer_key+"""')
                }
               </script>

                    <!-- javascript at the bottom for fast page loading -->
                    <script type="text/javascript" src="assets/js/jquery.min.js"></script>
                 </body>
              </html>"""
