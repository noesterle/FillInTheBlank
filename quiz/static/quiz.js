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
            elements[i].innerText = elements[i].dataset.lyric
            elements[i].id = "revealed"
            elements[i].style.color = "black"
            found = true
        }
    }
    if(found){
        document.getElementById('reveal').value = ""
    }
};

/*******  Timer *******/
var distance = 900000; // 15 Min
// Update the count down every 1 second
var countdown = setInterval(function() {
    
  // Find the distance between now and the count down date
    
  // Time calculations for days, hours, minutes and seconds
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
  // Output the result in an element with id="demo"
  document.getElementById("timer").innerHTML = minutes + "m " + seconds + "s ";
    
  // If the count down is over, write some text 
  if (distance < 0) {
    clearInterval(countdown);
    document.getElementById("demo").innerHTML = "EXPIRED";
  }
  
  distance = distance - 1000;
}, 1000);