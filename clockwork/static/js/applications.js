function makeHttpObject() {
    try {return new XMLHttpRequest();}
    catch (error) {}
    try {return new ActiveXObject("Msxml2.XMLHTTP");}
    catch (error) {}
    try {return new ActiveXObject("Microsoft.XMLHTTP");}
    catch (error) {}

    throw new Error("Could not create HTTP request object.");
}

function trial(username) {
    var request = makeHttpObject();
    request.open("GET", "/application/" + username + "/trial/", false);
    request.send(null);
    alert(username + " successfully promoted to Trial rank.");
}

function accept(username) {
    var request = makeHttpObject();
    request.open("GET", "/application/" + username + "/accepted/", false);
    request.send(null);
    alert(username + " successfully promoted to Member rank.");
}

function decline(username) {
    var request = makeHttpObject();
    request.open("GET", "/application/" + username + "/declined/", false);
    request.send(null);
    alert(username + " successfully demoted  to Declined rank.");
}

// Parses URL/?<param>=<content> for param 
function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
	results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

// Opens up a user's application after someone has posted a comment to that application
$(document).ready(function(){
    var anchor = getParameterByName('app');

    // collapses all of the collapse modules
    $(".collapse").collapse('hide');

    // opens the anchored one
    $('#' + anchor).collapse('toggle');

    // move to comments section
    if (anchor) {
	window.location.hash = '#' + anchor + '-comments';
    }
});
