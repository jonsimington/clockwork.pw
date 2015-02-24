function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
    results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

// fill in message recipient box based on URL
$(document).ready(function(){
    var recipient_name = getParameterByName('recipient');
    
    if (recipient_name) {
	document.getElementById("id_recipient").value = recipient_name;
    }
});
