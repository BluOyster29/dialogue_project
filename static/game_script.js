var name = [];
var score = 0;
var tries = 1;
var lives = 3;
var startTime, endTime;

var playerName = "Robby Bob Socks";

function add_letter(letter){
  name.push(letter);
  return name
  
}

function read_name(){
  name = name.join('');
  return name.toString()

}

function reset_name(name){
  name = [];
  return name
}

function reset_tries(tries){
  tries = 3
  return tries
}

function reset_lives(lives){
  lives = 10
  return lives
}
function add_point(score) {
    return score + 1;

}

function minus_point(score) {
    return score - 1;
}

var startTime = start();

function sleep(miliseconds) {
    var currentTime = new Date().getTime();
 
    while (currentTime + miliseconds >= new Date().getTime()) {
    }
 }

function start() {
    startTime = new Date();
    return startTime
  };
  
var endTime = end_time();

function end(){
   var endTime = new Date();
  return endTime
}

function get_price(startTime, endTime) {
  var currentResult = ((endTime - startTime) / 1000);
  var seconds = Math.round(currentResult);
  return seconds * 2

}