## tictactoe-for-terminal
Tic-tac-toe is a classic game in which two players ("X" and "O"), in alternating rounds, select a space to place their symbol, to complete a sequence of 3 adjacent spaces or block their opponent from doing so. Based on this, I created the code to replicate this game on the terminal.
## How to play:
First you need to select the symbol. The first player seletcs and the second player stays with the symbol remaining.

<img src="/assets/gif-select-symbol.gif">

After that, it's time to make a move. The defaults are 'number+letter' to access the board coordinates. It works with both lowercase and uppercase letters and spaces between them, but it does not work if the pattern is 'letter+number'. Another thing is that the board only updates when the player enters a correct coordinate, otherwise a printout appears on the terminal of what the user did wrong.

<img src="/assets/gif-select-symbol.gif">

At the end of the game there are three possible outcomes: player "X" wins, player "O" wins and draws, or in good Portuguese ("dar velha"). When you reach any of these results, you can choose to leave the game, or play another game.
## Nexts improvements:
- It is my wish to implement a version with the minimax algorithm in which it will be possible for a player to play against the "computer". 
- Also, at the end of the game, to add a standard action of starting a new game just by pressing "enter" on the keyboard.
## How to install:
- Install Git: If you don't have Git installed yet, you can download and install it from the official Git website.
- Open the terminal and navigate to the directory where you want to clone the repository. Then, execute the following command to clone the repository: `git@github.com:me15degrees/tictactoe-for-terminal.git`. Make sure to replace username and repository with the correct values.
- Now, navigate to the cloned repository directory and create a virtual environment. It's necessary for the requirements that isn't global. In the terminal, you can use the following command: `cd tictactoe-for-terminal` 
`python -m venv venv`. This last command creates a virtual environment named "venv" in your project directory called tictactoe-for-terminal.
- If you use mac/linux this command will activate your virtual environment: ´source venv/bin/activate`.
- If you use windows: `venv\Scripts\activate`.
- Now that you are in the virtual environment, you can install the project dependencies. If the rich_menu package is listed in the repository's requirements.txt file, you can use the following command: `pip install -r requirements.txt`.
- Now, run `python main.py`to start the game!










