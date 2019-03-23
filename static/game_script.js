var name = [];
var score = 0;
var tries = 1;
var lives = 3;
var start; 
var end;

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


function start(start) {
    start = new Date();
    return start
  };
  

function end(end){
  end = new Date();
  return end
}

function get_price(start, end) {
  var currentResult = ((end - start) / 1000);
  var seconds = Math.round(currentResult);
  return seconds * 2

}