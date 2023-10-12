# Play Game
#### Video Demo:  <https://youtu.be/ybtKjLxEngA?si=EwVBf5aeeDsWshJ->
 #### Description:
This project contains three games.
Project structure:
project.py
test_project.py
requirements.txt
README.md
Libraries used in this project: Random: This module implements the generator of pseudo-random numbers for different distributions.
Art: ASCII art is also known as "computer text art". It involves the clever placement of specific typed characters or letters to create a visual shape that spans multiple lines of text.

The command to install libraries can be installed simply with this pip command:
                            pip install -r requirements.txt
There is aa requirement.txt file which contains all the used libraries.
 run: python project.py

 the project.py contains 12 functions including the main function.

getGame() function :
This function simply prompts the user and allows him to select which game he wants to play, the function also has exception handling if the user puts a string or an integer that differs from the range of the proposed games.

Rock Paper Scissors game (2 Functions):
is_win(arg1,arg2) function: this function takes two arguments, player1 and player2 where the arguments have values like 'r' for rock, 's' for scissors, and 'p' for paper.
the function does test where it compares the two values and returns a boolean true if the rules of the game have been applied p > r, r > s, and s > p and if the didn't happen it will return false.

RockPaperScissors() function :
this function take no argument instead it makes a random guess between three values (r,p,s) which is the computer guess and takes the user input and compare it using is_win(computer,player) function, finally it will print a certain message if user has won, lost or drawn.

Magic 8 Ball game (1 Function):
MagicBall() function:
This function takes no arguments, it randomizes a number out of the range from 1 to 9 and outputs a certain message corresponding to that random guess.

Tic Tac Toe game (7 functions):
DefineBoard() function :
This function simply returns a dictionary containing keys from 1 to 9 with empty values which is a basic Tic Tac Toe board.

DisplayBoard() function :
This function displays the previously created board in the screen in a more board like manner.

UpdateBoard(arg1,arg2,arg3) function:
This function takes two arguments the board, the player and the position, the position value is provided by the user which the player when making a play whether it was the 'X' or 'O' player. so the board simply updates a key value by 'X' or 'O'.

CheckSpot(arg1,arg2) function:
This function takes two arguments, the board and the position and checks whether the spot or the value of a key is empty by comparing it to a blank string which is ' '.

checkFullBoard(board) function:
This function simply takes the board dictionaty and iterating overiting while applying condition if that value is empty or not. This function returns True or False.

Winner(arg1,arg2) function:
This function takes two arguments, the board and the player ('X' or 'O') and starts comparing between the recent player and the values of the keys horizontally and vertically and diagonally following the Tic Tac Toe rules.

TicTacToe() function:
This function calls all the previous functions separately first of all it decares a new board, the current player ('X') and the next player ('O'). then there is an infinite loop that breaks whenever a particular condition is provided, Exceptions are handled by a message when the user inputs a position that differs from the board values which ranges from 1-9. After it the CheckSpot() function to tell if the value of position (key) is empty or not, after that the board will be updated using UpdateBoard(board, currentPlayer, position) after the current player and the board get passed to the function Winner(board,currentPlayer) to detect who won or not, finally we check if the board is full or not using checkFullBoard function if it is full and there is no winner the game stops and print 'game over', the value of the current play and the next player gets switched.
