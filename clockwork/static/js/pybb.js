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

function addColor() {                                               
    document.getElementById("id_body").value += "[color=][/color]"
    document.getElementById("id_body").focus()
}  

function addBold() {                                               
    document.getElementById("id_body").value += "[b][/b]"
    document.getElementById("id_body").focus()
}  

function addItalics() {                                               
    document.getElementById("id_body").value += "[i][/i]"
    document.getElementById("id_body").focus()
}  

function addUnderline() {                                               
    document.getElementById("id_body").value += "[u][/u]"
    document.getElementById("id_body").focus()
}  

function addStrikethrough() {                                               
    document.getElementById("id_body").value += "[s][/s]"
    document.getElementById("id_body").focus()
}  

function addHR() {                                               
    document.getElementById("id_body").value += "[hr]"
    document.getElementById("id_body").focus()
}  

function addSubscript() {                                               
    document.getElementById("id_body").value += "<base>[sub]<subscript>[/sub]"
    document.getElementById("id_body").focus()
}  

function addSuperscript() {                                               
    document.getElementById("id_body").value += "<base>[sup]<superscript>[/sup]"
    document.getElementById("id_body").focus()
}  

function addList() {                                               
    document.getElementById("id_body").value += "[list][*]<item 1>[*]<item 2>[/list]"
    document.getElementById("id_body").focus()
}  

function addQuote() {                                               
    document.getElementById("id_body").value += "[quote][/quote]"
    document.getElementById("id_body").focus()
}  

function addCode() {                                               
    document.getElementById("id_body").value += "[code][/code]"
    document.getElementById("id_body").focus()
}  

function addCenter() {                                               
    document.getElementById("id_body").value += "[center][/center]"
    document.getElementById("id_body").focus()
}  

function addURL() {                                               
    document.getElementById("id_body").value += "[url=<url>]<link text>[/url]"
    document.getElementById("id_body").focus()
}  

