var name = [];
var score = 0;
var tries = 1;
var lives = 3;
var startTime, endTime;
var price = 0;

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

function start() {
  startTime = new Date();
};

function end(price) {
  endTime = new Date();
  var timeDiff = endTime - startTime; //in ms
  // strip the ms
  timeDiff /= 1000;

  // get seconds 
  var seconds = Math.round(timeDiff);

  //get price

  price = seconds * 2
  return price;
}