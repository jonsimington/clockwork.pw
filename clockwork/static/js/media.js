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
function loadVideo(title, id, type) {
    $('#media-content').empty()
    console.log(title + " " + id + " " + type)
    if (type == "youtube") {
	$('#media-content').html("<h3 class='text-center'>" + title + "</h3><iframe src='https://www.youtube.com/embed/vidID/' frameborder='0'></iframe>".replace("vidID", id))
    }
    else if (type == "twitch") {
	$('#media-content').html("<h3 class='text-center'>" + title + "</h3><iframe src='http://www.twitch.tv/channel/embed' frameborder='0'></iframe>".replace("channel", id))
    }
}
