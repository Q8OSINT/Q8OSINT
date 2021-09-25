function copyLink(linkText, port){
	$("#copy_panel").val("http://kuwaithackers.dyndns.org:"+port+linkText);
	$("#copy_panel").select();
	document.execCommand('copy');
    localStorage.setItem('copiedUrl',$("#copy_panel").val())
	alert("URL copied!");
}


$(function(){
    var port = document.getElementById("host").getAttribute("data-port");
	$("#copy_link").live("click", function(){
		copyLink($(this).parents(".app-icon").find("table tr td h6 a").attr("href"),port);
	})
})