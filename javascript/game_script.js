var name = [];
var score = 0;
var tries = 3;
var lives = 10;
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

function add_point(score) {
    return score + 1;

}

function minus_point(score) {
    return score - 1;
}