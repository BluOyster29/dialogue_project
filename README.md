# Dialogue Systems Video Game project

## Introduction 
The aim of this project was to create a vxml based video game. I have chosen a simple trivia formula that makes use of the voice as the controller, simple javascript logic for logic and external audio files for multimedia. 

## The Game
The game is a simple trivia game with two rounds, there is room for expansion I just need to come up with extra wordplay games. I will explain next each vxml form.

### Form 1: Welcome
This form welcomes the player to the game and invites them to provide their name using the nato alphabet. 

### Form 2: Spelling 
This form has one grammar and it is the nato alphabet with the tag out as the letter. I chose the nato alphabet as it makes it much easier to distinguish each sound. It works quite well, I have added the option to start over and to indicate when the name is complete. I added a default name if the player gets tired writing out their name. A couple of Javascript functions collects the letters then concatenates them into a string to be read back to the player, the name is then saved to be used in the rest of the game. 

### Form 3: Difficulty 
The player can now choose the difficulty of the game, I chose casual, medium and hard. These are typical difficulties for video games and the variables are as follows:
* Casual: Player has unlimited tries and lives 
* Medium: Player has a default number of 3 tries and 5 lives
* Hard: the player has no lives and three tries, this means if they get a question wrong three times they will lose the game. 

### Scoring, lives and tries 
When the player gets a question correct they gain a point, when they get a question wrong they lose a try. If a player runs out of tries they lose a life, once a player is out of lives they lose and are sent to the 'fail' form. Tries reset at the end of every round. The score is kept until the end where it is read out to the player, my ambition is to have a way of keeping the scores on a leaderboard. 

### Round One: Tongue Twisters
The first round of games consists of a set of tongue twisters. They all have simple grammars, there is only one option and that is the correct option. If the player is wrng the \<nomatch> event will perform some if statements to see if the player has enough tries/lives etc. If the player is right they go to the next question etc. 

### Round Two: Intros Round 
I drew inspiriation from a British game show called 'Never Mind the Buzzcocks'. Two team members would sing the introduction to a song and the other player had to guess it. I wanted to make the song sound quite funny to add humour to the game, which I think it does. Again the player is told four options but there is only one option in the grammar and that is the correct answer. So if the player is wrong the \<nomatch> event will perform some logic to see if the player can continue.

### Failed Round Three: Countdown rip-off
There is a great maths part of the British show Countdown where the player is given a random large number then some smaller ones and with the smaller ones they have to perform arithmatic to get as close as possible to the number. I managed to make the javascript for generating all the random numbers but I came into difficulty with the grammar, the ASR is not sophisticated enough as well as it constantly confuses numbers. I decided to drop it but maybe I will come back to it.

### Completion
At the end of the rounds the player is brought to the completion form. The form will tell the player their score and lives and give a general well done message. I will try and give different messages depending on score. I added a small bit of javascript that keeps time and tells the player how much the sessions has cost them, this is again to add some humour, unfortunately I have a tragically dry sense of humour. The player has the option to play again or exit the game

### Fail
I have added a failure form, this is in the event the player runs out of lives. The player is told their score and lives and comiserations is given. The player can play again or exit. 

## Technicalities
The game makes use of vxml, javascript and python. Python is responsible for the backend running of the FLASK server whilst javascript performs all the client side logic such as score taking. xml/vxml are responsible for the markup of the game and acts to control the flow.

## Challenges
I found the biggest difficulty was using vxml in smart but simple ways to create entertainment. The ASR can be quite limiting so it is difficult to give the user a truly autonomous experience.

## Relation to course
I tried to keep my game simple therefore the first two labs were probably most helpful, I have not made much use of ssml this is mostly because of the ammount of time it took to implement the javascript. I have used simple grammars to create 

Future work: how could the game be developed?

## Conclusion
The game is of a very simplistic nature with a typical trivia format, the javascript serves only for point keeping. I understand that it would be more effictient if I could have stored the variables server side but I have not worked out how to do that yet, as I wanted to have seperate forms for each round to make the game a bit more organised. 

I have used basic vxml tags and functions, I have not fully explored the semantic abilities as I wanted to keep the game simple. I feel I have given the player illusions of freedom by offering multiple choices when really there is only one. The grammars, in coordination with \<nomatch> are a good combination for simple game logic as it helps to limit the input the machine can handle. 

To take the game further I would like to expand the tongue twister game to include other languages, the server sadly could only handle english and it would have been fun to experiment with tongue twisters from other languages.


