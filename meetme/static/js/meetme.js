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

    spinner.show();

    return setInterval(function () {
        var newPos = "-" + (++current % count * 26) + "px 0px";
        spinner.css({"background-position": newPos});
    }, 50);
}


function button_click_ajax(button_id, ajax_url, data, success){
	var button = $(button_id);
        var buttonWidth = button.width();

        button.width(buttonWidth);
        button.css({"text-align": "center"});
        button.html('<div id="spinner"></div>');

        var spinner = $('#spinner');
        var spinInterval = spin();

        $.ajax({
            url: ajax_url,
            type: 'POST',
            data: data,

            success: function (data) {
                clearInterval(spinInterval);

                spinner.hide();
                $(button_id)
                    .html("Done!")
                    .removeClass("btn-info")
                    .addClass("btn-success");
		if (success){
			success($.parseJSON(data));
		}
            }
        });
}

function checkResponse(responseId){
      $.ajax({
            url: '/check_response/'+responseId+'/',
            type: 'GET',

            success: function (data) {
		var jsonData = $.parseJSON(data);
		if (jsonData.text){
	                clearInterval(responseInterval);
			$('#response_text').html(jsonData.text);
		}
            }
        });
}

var responseInterval = null;

$(function () {
	
    var request_button_id = '#request'
    $(request_button_id).click(function () {
	var theButton = $(this);
	button_click_ajax(request_button_id, '/make_request/', {
		account_id: localId,
		time_range: $('#time-range-input').attr('value')
	}, 
	function(data){
		var template = $('#template');
		theButton.replaceWith(template.html());
		spin();
		responseInterval = setInterval(function(){
			checkResponse(data.reservation_id);	
		}, 3000);
	});
    });

    $('.time-range').click(function(){
	$('#time-range-input').attr("value",  $(this).html());
	$('.time-range').removeClass('active');
	$(this).addClass('active');
    });

    var avail_button_id = '#im_available'
    $(avail_button_id).click(function () {
	button_click_ajax(avail_button_id, '/im_available/', {category_id: categoryId}, function(){
	document.location = document.location.href;
});
    });

    $('a').click(function() {
        document.location = $(this).attr('href');
        return false;
    });
});


