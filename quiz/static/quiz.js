function showLyrics(element, textColor){
    element.innerText = element.dataset.lyric
    element.id = "revealed"
    element.style.color = textColor
}

/* Searching and revealing */
function revealLyrics() {
    var elements = document.getElementsByClassName("lyric");
    let lyric = ''
    let found = false
    for(var i=0; i<elements.length; i++) {
        lyric = elements[i].dataset.lyric.toLowerCase()
        text = document.getElementById('reveal').value.toLowerCase()
        console.log(lyric + " " + text)
        if(lyric == text && elements[i].id == "hidden"){
            showLyrics(elements[i],"black")
            found = true
        }
    }
    if(found){
        document.getElementById('reveal').value = ""
    }
};

function revealAll() {
    var elements = document.getElementsByClassName("lyric");
    for(var i=0; i<elements.length; i++) {
        if(elements[i].id == "hidden"){
            showLyrics(elements[i],"red")
        }
    }
}