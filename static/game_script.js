//default variables for game
var name = [];
var score = 0;
var tries = 3;
var lives = 5;
var start; 
var end;
var price;
var playerName = "Robby Bob Socks";

//Function adds 100 to int making game casual
function casual(points){
  points = points + 100;
  return points
}

//function resets lives to 0 for hard mode
function hard(lives){
  lives = 0;
  return lives
}

//adds letter to list for spelling name
function add_letter(letter){
  name.push(letter);
  return name
  
}

//joins letters to string for reading out
function read_name(){
  name = name.join('');
  return name.toString()

}

//if name is wrong creates empty list
function reset_name(name){
  name = [];
  return name
}

//resets tries to default 3
function reset_tries(tries){
  tries = 3
  return tries
}

//resets lives to default 5
function reset_lives(lives){
  lives = 5
  return lives
}

//adds point to score
function add_point(score) {
    return score + 1;
}

//takes point off score
function minus_point(score) {
    return score - 1;
}

//for keeping time (not working)
function start(start) {
    start = new Date();
    return start
  };
  
function end(end){
  end = new Date();
  return end
}

function get_price(start, end, price) {
  var currentResult = ((end - start) / 1000);
  var seconds = Math.round(currentResult);
  price = seconds * 2
  return price

}