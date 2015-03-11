// Function to handle the nested navs
$.fn.naccordian = function () {
    
    $root = this;
    
    this.children('li').each(function () {
	
	var $this = $(this),
	    $child = $this.find('.nav-stacked');
	
	$child
	    .hide()
	    .parent()
	    .on('click', function (e) {
		var child_was_visible = $child.is(':visible');
		$root.find('.nav-stacked').not($child).hide();
		$child.show();
		if (child_was_visible && !$child.has(e.target).length) {
		    $child.hide();
		}
	    });
	
	$this.children('a').on('click', function () {
	    $root.find('.active').removeClass('active');
	    $(this).parent().addClass('active');
	});
    });
    
    this.on('click', 'a', function (e) {
	
	var $this = $(this),
	    $icon = $this.find('i'),
	    $child = $this.parent().find('.nav-stacked');
	
	
    });
};

$(function () {
    $('.nav-stacked').naccordian();
});

// Function to load a video div
function loadVideo(e) {
    var $target = $(e.currentTarget);

    var titles = $target.data('title');
    var ids = $target.data('id');
    var type = $target.data('type');

    $('#media-content').empty()

    // Assumes titles, ids are a list of 1 or more elements
    if (type == "youtube") {
	for (var i = 0; i < titles.length; i++) {
	    $('#media-content').append("<h3 class='text-center'>" + titles[i] + "</h3>");
	    $('#media-content').append("<iframe src='https://www.youtube.com/embed/vidID/' frameborder='0'></iframe>".replace("vidID", ids[i]));
	}
    }
    // Assumes titles, ids are a list of 1 element
    else if (type == "twitch") {
	$('#media-content').append("<h3 class='text-center'>" + titles + "</h3>");
	$('#media-content').append("<iframe src='http://www.twitch.tv/channel/embed' frameborder='0'></iframe>".replace("channel", ids[0]));
    }

    
}

$('.videoElement').click(loadVideo);
