# TwitterOrange
This bot will remind Donald Trump everyday that his face is orange.

# How to run:
 - Get a Twitter Developer account(make a new twitter account). It takes a couple of days to verify
 - Clone this repo.
 - Create a new Application on twitter, and once you are done go to Keys and Tokens under the application page.
 - In the clone make a file called `KEYS_AND_TOKENS.py` and add these four variables in the file: `CONSUMER_KEY`, `CONSUMER_SECRET`, `ACCESS_TOKEN`, `ACCESS_TOKEN_SECRET`, and appropriately declare the variables with the Keys and Tokens provided by twitter
 - If you have forked the repo and are using the bot, MAKE SURE THAT THE `KEYS_AND_TOKENS.py` FILE DOES NOT BECOME PUBLIC, since that will give people access to your account.
 - Go to [Python Anywhere](pythonanywhere.com), and make an account make a new directory for this project and add the `bot.py` and `KEYS_AND_TOKENS.py` file to the directory. 
 - Open up the console, and run `pip install tweepy`. 
 - Once thats done run `python bot.py`, and you're good to go!
