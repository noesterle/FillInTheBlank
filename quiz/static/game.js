/*******  Timer *******/
var distance = 900000; // 15 Min
// Update the count down every 1 second
function TimerFunc() {
    
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
}

/* Start Quiz */
let timerId = ''
let play = document.querySelector('#play');
let quit  = document.querySelector('#quit');

play.addEventListener('click', function() {
	timerId = setInterval(TimerFunc(), 1000);
    document.getElementById('reveal').disabled = false;
});

// Stopping the timer:
quit.addEventListener('click', function() {
	clearInterval(timerId);
    revealAll();
});