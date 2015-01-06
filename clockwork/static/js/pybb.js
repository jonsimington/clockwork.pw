function quote_selected(user) {
    var selection = '';
    if(window.getSelection){
	selection = window.getSelection();
    }else if(document.getSelection){
	selection = document.getSelection();
    }else if(document.selection){
	selection = document.selection.createRange().text;
    }
    document.getElementById("id_body").value += "[quote=" + '"' +  user + '"' +  "]" + selection + "[/quote]"
    
    document.getElementById("id_body").focus()
}
