# Connect Four

PROJECT CONNECT FOUR
AUTHOR: mfilipesa24
Release date: 13/11/2024
Version 1.0.

**************************************************************************************************************************************************
1. Project's Aim

The aim of the "Connect Four" project is to replicate a Connect Four game.
Connect Four is a game played between two players ("Player 1" and "Player 2", for simplification purposes), each player having a specific symbol.
It is a 1v1 type of game, where each player takes turns to win the game.

A Connect Four game, in its classical form, has 6 rows and 7 columns, with a total of 42 possible positions.
Players must fill the columns, in a bottom-to-top approach, aiming to obtain a four-symbol alignment of their respective symbols in each
row, column or diagonal of the game board. The first player to achieve such an alignment wins the game.

Note: It is assumed that players will not be choose the same symbol.

**************************************************************************************************************************************************
2. How To Execute The Project

To play our Connect Four game, ensure you have the following Python files in the same directory:
- connect_four.py
- board.py
- player.py

Next, using your command terminal, execute the "connect_four.py" file.
If you are working with a Windows operating system, you may need to type the following command: "winpty python[version] [filename]"
All our commands have been checked and successfully verified using the "Git Bash" terminal.

To exit a Connect Four game at any stage of time during the execution of "connect_four.py" type "exit" and then press "Enter" on your keyboard. You
will see a terminal notification confirming that "Program stopped."

To execute any game command, press "Enter" after typing it.

**************************************************************************************************************************************************

3. How To Play The Game

  3.1. General Instructions

  A Connect Four game can end with either a victory for one of the players, or a tie, with a terminal notification informing the players of the
  game outcome once it ends. Before the game starts, each player is asked to provide the game symbol they wish to use. Once the game symbols
  have been defined, the game begins with players entering their move inputs on their assigned turns. Only valid player's moves will be accepted.

  The first player to align four symbols in a row, column, or diagonal on the game board wins the game. When it is no longer possible to achieve
  a four-symbol alignment for any player in the ongoing game instance, the game ends in a tie.

  Note: For simplification purposes while designing our project, it was decided that Player 1 would always be the first player to start the game.
  However, since Connect Four is a solved game type where the first player can always win by making the right moves, to mitigate rigging risks,
  both players can switch their roles as "Player 1" or "Player 2" in each game.

  3.2. Move Input

  A player's move input must be a number comprised between 1 and 7, representing one of the seven columns of the board, in a left-to-right motion.
  Each column can hold six different positions. Any other input will be invalid. In such cases, the player will receive a notification and will be
  prompted to to re-enter a different move, until a valid move is obtained.

  It is also necessary that the chosen column by the player is still not filled, meaning it contains at least one empty position at the top. If the
  column provided by the player is already filled, the player will receive a a notification regarding that fact in the terminal, and will be asked
  to re-enter a different move, using another column.

  If the current player's chosen column is still not filled, the first empty position found in that column, moving upward, and starting from the
  bottom of the column, will be filled with the current player's symbol.

  3.3. Game view 

    From columns 1 to 7:
        1   2   3   4   5   6   7
       -------------------------->
     | [ ] [ ] [ ] [ ] [ ] [ ] [ ] |
     | [ ] [ ] [ ] [ ] [ ] [ ] [ ] |
     | [ ] [ ] [ ] [ ] [ ] [ ] [ ] |
     | [ ] [ ] [ ] [ ] [ ] [ ] [ ] |
     | [ ] [ ] [ ] [ ] [ ] [ ] [ ] |
     | [ ] [ ] [ ] [ ] [ ] [ ] [ ] |

  If Player 1 choses "X" for symbol and Player 2 choses "0" for symbol, with Player 1 chosing "3" and Player 2 chosing "3", at the end of the
  first turn, the outcome will be as follows:

       -------------------------->
     | [ ] [ ] [ ] [ ] [ ] [ ] [ ] |
     | [ ] [ ] [ ] [ ] [ ] [ ] [ ] |
     | [ ] [ ] [ ] [ ] [ ] [ ] [ ] |
     | [ ] [ ] [ ] [ ] [ ] [ ] [ ] |
     | [ ] [ ] [0] [ ] [ ] [ ] [ ] |
     | [ ] [ ] [X] [ ] [ ] [ ] [ ] |

**************************************************************************************************************************************************
4. Versions and Modifications

The Connect Four project is launched as a single version 1.0, at the time of the release date.

**************************************************************************************************************************************************
5. Code Interpretation

For maintenance purposes and to facilitate code interpretation, relevant comments have been added into to the core files of the project.
These comments do not interfere with program's execution, but merely provide an insight into the code mechanics used.

**************************************************************************************************************************************************  
6. Terms of Liability

The author is not responsible for any modifications made by users to the available release version of the project and its files.

**************************************************************************************************************************************************  





