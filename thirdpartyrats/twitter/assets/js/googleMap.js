

function getGoogleMaps(lat = 29.28538087, long = 48.00550236){

	var area = $("#locationlist option:selected").text().trim();
	
	if(area != ""){

		lat = area.split("lat: ")[1].split(" long:")[0];
		long = area.split("long: ")[1].split(" datetime")[0];

	}

	var latlng = new google.maps.LatLng(lat, long);
	var myOptions = {
	    zoom: 16,
	    center: latlng,
	    mapTypeId: google.maps.MapTypeId.ROAD
	};
	map = new google.maps.Map(document.getElementById("latlongmap"),
	    myOptions);
	geocoder = new google.maps.Geocoder();
	marker = new google.maps.Marker({
	    position: latlng,
	    map: map
	});

	map.streetViewControl = false;
	infowindow = new google.maps.InfoWindow({
	    content: "(" + lat + "," + long + ")"
	});

	google.maps.event.addListener(marker, 'click', function(event) {
	    infowindow.open(map, marker);
	});
}