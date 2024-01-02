# Tic-tac-toe for terminal


Tic-tac-toe, also called noughts and crosses, is a classic game in which two players ("X" and "O"), in alternating rounds, select a space to place their symbol, to complete a sequence of 3 adjacent spaces or block their opponent from doing so. Based on this, I created the code to replicate this game on the terminal.
## How to play:
First you need to select the symbol. The first player seletcs and the second player stays with the symbol remaining.

<img src="/assets/gif-select-symbol.gif">

After that, it's time to make a move. The defaults are 'number+letter' to access the board coordinates. It works with both lowercase and uppercase letters and spaces between them, but it does not work if the pattern is 'letter+number'. Another thing is that the board only updates when the player enters a correct coordinate, otherwise a printout appears on the terminal of what the user did wrong.

<img src="/assets/gif-moves.gif">

At the end of the game there are three possible outcomes: player "X" wins, player "O" wins and draws, or in good Portuguese ("dar velha"). When you reach any of these results, you can choose to leave the game, or play another game.
## Nexts improvements:
- It is my wish to implement a version with the minimax algorithm in which it will be possible for a player to play against the "computer". 
- Also, at the end of the game, to add a standard action of starting a new game just by pressing "enter" on the keyboard.
## How to install:
- Open the terminal and navigate to the directory where you want to clone the repository. Then, execute the following command to clone the repository: `https://github.com/me15degrees/tictactoe-for-terminal.git`.
- Now, navigate to the cloned repository directory and create a virtual environment. You can use the following command: `cd tictactoe-for-terminal` `python -m venv venv`. 
- If you use mac/linux this command will activate your virtual environment: `source venv/bin/activate`.
- If you use windows: `venv\Scripts\activate`.
- Now that you are in the virtual environment, you can install the project dependencies. Use the following command: `pip install -r requirements.txt`.
- Now, run `python main.py` to start the game!

##
<div align="center">
Follow me:
  
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/maria-eduarda-nascimento-andrade-bb0b86213/)
  [![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=flat&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCh6sgz1ij_my64lX8rQnPXg)
  [![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=flat&logo=spotify&logoColor=white)](https://open.spotify.com/user/223w3q4xdm4pquahzl5xhfpia?si=t08g7SlVRvqhF0LseXTyXg&nd=1&dlsi=87356229bcf14264)
  [![Last.fm](https://img.shields.io/badge/Last.fm-D51007?style=flat&logo=last.fm&logoColor=white)](https://www.last.fm/user/me15degrees)
  

</div>











