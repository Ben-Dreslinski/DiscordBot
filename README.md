# Discord (Bingo) Bot

## How it Works

Given a list of (at minimum) 25 events, the bot will randomize this list and take the first 25 to create a board from these strings. For example, if you were to fill the list with Events 1-25 as separate strings, this is one board that could be created:

![Example board](https://cdn.discordapp.com/attachments/854066615788109837/858904120336318474/github1new.png)

Obviously the more events you have in the list, the more unique boards you'll get. Since there are only 25 for this example, the same events will always be on the board, but the chance of having an identical board after generating two is practically zero.

## How to Play

The commands are accessible through discord via the '-commands' command if forgotten, but here's what it consists of as of this release:

* -green \<column> \<row>
* -red \<column> \<row>
* -showboard 
* -starttime
* -newboard
 
The usage of these commands is straight forward, but here are some examples given the board above:
  
If a user were to type "-green I 3", the bot would send this board, updating the third square in the second column: 
  
![Updated board](https://cdn.discordapp.com/attachments/854066615788109837/858903988722991115/github2new.png)
  
Say I actually didn't mean to update that square, I can send "-red I 3" to undo the previous update and make it red again.

There is also error checking to make sure that a green square cannot be made green and vice-versa w/ red to prevent the need to create a new board and save (however miniscule) resources.

Once bingo is gotten, whether it be row, column, or diagonal, said line will light up yellow to make it easier on the eyes, and a newboard can be created by the "-newboard" command.

## How to Deploy

This package only needs a few changes to run into your server and off of your bot:

1. Paste your bot's discord token directly into the [token.0](https://github.com/Ben-Dreslinski/DiscordBot/blob/main/lib/bot/token.0) file, no quotes or brackets needed.
2. Paste your discord id into the OWNER_IDS set in the [bot class](https://github.com/Ben-Dreslinski/DiscordBot/blob/main/lib/bot/__init__.py) (line 8) file, no quotes or brackets needed.
3. Paste your channel and guild (server) ids into the the "stdout" and "guild" fields, respectively, in the [bot class](https://github.com/Ben-Dreslinski/DiscordBot/blob/main/lib/bot/__init__.py) (lines 37 and 38).
4. Put a minimum of 25 comma-separated events (strings) into the "possibleSquares" field in the [bingo class](https://github.com/Ben-Dreslinski/DiscordBot/blob/main/lib/bingo/__init__.py) (line 9). A little bit of trial and error may be required using the newline, "\n", character depending on how long the strings are.

Small note: the "-starttime" command refers to UTC since that happens to be the timezone the server I use is in, feel free to change that to wherever your bot is hosted.
