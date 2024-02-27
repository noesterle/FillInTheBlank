function showLyrics(element, textColor){
    element.innerText = element.dataset.lyric
    element.id = "revealed"
    element.style.color = textColor
}

function increaseScore() {
    total_score = Number(document.getElementById('total').innerText)
    curr_score_el = document.getElementById('score')
    curr_score = curr_score_el.innerText
    new_score = 1 + Number(curr_score)
    curr_score_el.innerText = new_score

    perc_el = document.getElementById('percentage')
    perc_el.innerText = ((new_score/total_score)*100).toFixed(2)
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
            increaseScore()
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