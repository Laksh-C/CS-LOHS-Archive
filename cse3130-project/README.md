# CSE3130-Project

## Description:
This project represents a Brick Breaker game simulator. Its purpose is to explore inheritance and polymorphism through pygame. 

## Planning Components:
![Brick Index Planning](media/Brick%20Index%20Planning.PNG)
_This image shows the arrangement of the indexes of all the bricks in the BRICKS array._

![Layout Planning](media/Layout%20Planning.PNG)
_This images shows the proposed layout for the game. It shows the welcome text, lives remaining, as well as the planned out extra features which were lives and a blue/red paddle to signify direction of ball bouncing._

## Special Features
I included two special features into my program. The first of which being a Life remaining feature. The user is given 3 lives (chances) to destroy all the bricks. A life is deducted if the ball touches the bottom edge of the window. If all 3 lives are lost, then the game is over. 

The second extra feature I included was I divided the paddle into two colors. One is blue and the other is red. If the ball bounces on the blue portion, then the ball will reflect, and it's trajectory will be towards the right, regardless of its original trajectory. If the ball bounces on the red portion, then the ball will reflect towards the left. This allows the user to be able to work around tricky bricks and offers the user more chances to destroy the bricks efficiently.

## How to run the program
In order to run this game, you will be required to install pygame. 
### **How to install Pygame on a Windows computer:**
1) Open the cmd (command line interface) on your Windows computer.
2) type in ```py -m pip install pygame```
3) Press enter

### **How to install Pygame on a Mac computer:**
1) Open the Terminal command line interface on your Mac computer.
2) type in ```python 3 -m pip install pygame```
3) press enter

After you have installed pygame, you can run the program. The file you need to run is the main.py file.

## Reflection
While developing this project, I truly learned the process of eliminating bugs. Pygame is a library that does not work well with the built-in debugger on pycharm; therefore, other methods such as 
```python
try:
    CODE 
except:
    CODE
```
needed to be used. I also found myself using print statements to test individual processes. For example, when coding the blue/red left/right bouncing feature on the paddle, I printed "red" or "blue" on the interface to see whether the program was able to detect which side of the paddle it was bouncing on. 

Another thing I learnt was the true value of drawing and visualizing wireframes and the overall layout. I faced difficulty in rendering the bricks and was going down an extremely inefficient path of trying to hardcode the values of the bricks. However, when I drew out the layout, I was able to recognize patterns which allowed me to utilize for loops. 

What I found particularly challenging was working out the logic for having the ball reflect off of the bricks, depending on the orientation the ball collided with the brick in. I had gone through many iterations of trying to code a solution without finding much success. Then I went to look at one of my app game kit projects from Computing Science 10 and I was able to understand how I implemented collisions back then. After reviewing my notes and past projects, I was able to easily overcome that challenge. 

Antoher thing that I am particularly fond of is the animations that I included in the text. The welcome text, the game over text, and the "You Win" text all pulse and flash in colors. I had found a YouTube tutorial on how to make texts flash colors and I modified to suit my purpose. This allowed me to appreciate just how much of a collaborative industry IT is. Programmers build upon each other. In a workplace industry environment, it isn't really about competition amongst employees to become the best programmer, its about being able to harmonize and cooperate with the talents of others to build a product that is brilliant. It reminded me of the anecdote of how Henry Ford did not invent the engine or the wheel, rather he put those inventions together...he built upon them...to come up with an invention that hundreds of millions of individuals use today. Computer science is an industry that allows you to use other people's inventions (whilst maintaining integrity and honesty ofcourse) to reach your goals exponentially faster. 