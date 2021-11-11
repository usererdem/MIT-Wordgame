# MIT-Wordgame
Hello, I made this project/game as an assignment to learn and understand the fundamentals of programming.

I took the 'Introduction to Computer Science and Programming in Python' class from MIT Open Courseware. 

This project/game is an assignment from that class.


The Game Explanation: 

It is a Word game like scrabble, every letter has specific points, your goal is to get the highest score.

When you open the game:

1- Game is going to give an input --> Enter total number of hands: 
You can simply select how many hands you want to play by writing the hand amount in number format. (1,2,3,4,5,6 etc.)
After finishing your hand if you chose more than one hand it will start the new round.

2- The game will deal with a hand of 7 letters including one unique letter that you can use as any letter and print for the player to see.
Example: Current Hand: o u f f k b *
Current Hand: o u f f k b * --> example word from the current hand --> bo*k which is going to accept book so unique letter is going to work as the letter o in this case.

3- The game is going to ask --> Would you like to substitute a letter? --> You can type yes if you want to change a letter
a. If you type yes --> The game asks: Which letter would you like to replace: --> type the letter you want --> after you write, the specific letter is going to get replaced.
b. If you type no the game will continue with the same hand dealt.

4- The game will ask for the player to Enter a word, or write '!!' to indicate that you are finished.

5- After you finished, your total score will be printed and the game is going to ask if you want to replay the same hand --> you can type yes to replay the hand or no to continue.

6- You will receive your endgame score at the end of the game.

Here is a Game Example: 

Loading word list from file...
   83667 words loaded.

Enter total number of hands: 2
Current Hand: u i v g g r * 

Would you like to substitute a letter?(type yes or no): yes

Which letter would you like to replace: g
Current Hand: u i v g r * f 

Enter word, or '!!' to indicate that you are finished: fiv*
fiv* earned 171 points. Total =  171 points 

Current Hand: u g r 

Enter word, or '!!' to indicate that you are finished: rug
rug earned 84 points. Total =  255 points 

Run out of letters. Total Score:  255 points

Would you like to replay the hand?(type yes or no): no
Current Hand: u o x c h z * 

Would you like to substitute a letter?(type yes or no): no
Current Hand: u o x c h z * 

Enter word, or '!!' to indicate that you are finished: !!
Total Score:  0 points

Would you like to replay the hand?(type yes or no): yes
Current Hand: u o x c h z * 

Enter word, or '!!' to indicate that you are finished: uox
That is not a valid word. Please choose another word. 
Current Hand: c h z * 

Enter word, or '!!' to indicate that you are finished: hcz
That is not a valid word. Please choose another word. 
Current Hand: * 

Enter word, or '!!' to indicate that you are finished: *
* earned 0 points. Total =  0 points 

Run out of letters. Total Score:  0 points
In 2 amount of hands. You have made 255 points.
Your EndGame score is:  255
