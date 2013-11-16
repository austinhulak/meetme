function getLocation() {
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        $('#demo').html("Geolocation is not supported by this browser.");
    }
}


function showPosition(position) {
    var message = "Latitude: " + position.coords.latitude + "<br>Longitude: " + position.coords.longitude;

    $('#demo').html(message);
}
