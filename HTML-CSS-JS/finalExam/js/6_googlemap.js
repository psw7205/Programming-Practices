function myMap() {
    var myLatLng = {
        lat: 37.550916576175766,
        lng: 127.07578221189056
    }

    var map = new google.maps.Map(document.getElementById("googleMap"), {
        center: myLatLng,
        zoom: 16
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
    });
    marker.setMap(map);

    var infowindow = new google.maps.InfoWindow({
        content: "Here is DaeYang AI Center"
    });

    infowindow.open(map, marker);

    google.maps.event.addListener(marker, 'mouseover', function () {
        var infowindow = new google.maps.InfoWindow({
            content: "DaeYang AI Center"
        });

        infowindow.open(map, marker);
    })
}