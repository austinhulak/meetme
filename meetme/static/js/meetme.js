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


$(function () {
    var requestButton = $('#request');

    requestButton.click(function () {
        var buttonWidth = requestButton.width();

        requestButton.width(buttonWidth);
        requestButton.css({"text-align": "center"});
        requestButton.html('<div id="spinner"></div>');

        var spinner = $('#spinner');
        var spinInterval = spin();

        $.ajax({
            url: '/make_request/',
            type: 'POST',
            data: {
                account_id: localId
            },

            success: function () {
                clearInterval(spinInterval);

                spinner.hide();
                $('#request')
                    .html("Done!")
                    .removeClass("btn-info")
                    .addClass("btn-success");
            }
        });
    });
});
