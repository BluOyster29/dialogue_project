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

function end_time(){
    var endTime = new Date();
    return endTime
}

function timeDiff(startTime, endTime) {
    
    
    // strip the ms
    var currentResult = ((endTime - startTime) / 1000);

    // get seconds 
    var seconds = Math.round(currentResult);


    return seconds * 2
}


console.log(startTime);
console.log(endTime);
console.log(timeDiff(startTime, endTime));