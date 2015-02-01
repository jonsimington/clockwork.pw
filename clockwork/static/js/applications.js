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
