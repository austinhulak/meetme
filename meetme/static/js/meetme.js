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

function spin() {
    var spinner = $('#spinner');
    var count = 12;
    var current = 0;

    return setInterval(function () {
        var newPos = "-" + (++current % count * 26) + "px 0px";
        spinner.css({"background-position": newPos});
    }, 50);
}


