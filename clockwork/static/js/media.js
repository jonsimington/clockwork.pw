// A function to display a roster div when the nav button is pressed on the
// roster nav menu
function displayDiv(div) {
    var divs = ["gruul", "blast-furnace", "beastlord-darmac", "operator-thogar",
		"iron-maidens", "hans-and-franz", "flamebender-kagraz", "kromog",
		"blackhand", "oregorger", "tectus", "butcher", "twin-ogron",
	        "paragons", "garrosh", "gate-setting-sun", "niuzao-temple",
	        "adgetty-twitch", "apparati-twitch", "awss-twitch", "bottizelle-twitch",
	        "qoof-twitch", "yatt"];

    var numDivs = divs.length;

    // hide help text div
    document.getElementById('help-text').style.display = "none";

    // hide all divs
    for (var i = 0; i < numDivs; i++) {
	document.getElementById(divs[i]).style.display = "none";
    }
    

    // Show the specified div
    document.getElementById(div).style.display = "block";
}


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
