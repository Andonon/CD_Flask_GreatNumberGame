# CD_Flask_GreatNumberGame

Assignment: Great Number Game
Create a site that when a user loads it creates a random number between 1-100 and stores the number in session. Allow the user to guess at the number and tell them when they are too high or too low. If they guess the correct number tell them and offer to play again.

In order to generate a random number you can use the "random" python module:

import random # import the random module

<i>The random module has many useful functions. This is one that gives a random number in a range </i>

random.randrange(0, 101) 
<i> random number between 0-100</i>

In order to remove something from the session, you must "pop" it off of the session dictionary.

<i> Set session like so:</i>
session['someKey'] = 50
<i>Remove something from session like so:</i>
session.pop('someKey')

<img src="http://s3.amazonaws.com/General_V88/boomyeah/company_209/chapter_2240/handouts/chapter2240_3241_great-number-game.png" width=200px>

Note: There are many different ways to do this assignment. When you finish the basic functionality, find a peer and compare your code!