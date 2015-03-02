// A function to display a roster div when the nav button is pressed on the
// roster nav menu
function displayDiv(div) {
    var classes = ["deathknights", "druids", "hunters", "mages", "monks",
		   "paladins", "priests", "rogues", "shamans", "warlocks",
		   "warriors"];

    var numClasses = classes.length;

    // clear all other divs
    for (var i = 0; i < numClasses; i++) {
	document.getElementById(classes[i]).style.display = "none";
    }

    // Show the specified div
    document.getElementById(div).style.display = "block";
}
