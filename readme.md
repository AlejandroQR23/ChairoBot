# Telegram Bot

This is a simple implementation for a telegram bot written in python.

## How to use

Fork or download the code. Then you may want to create a virtual environment for running the Python code.
You can do this by running this command on your terminal (on the code folder):

```
python -m venv env
```

It will create the virtual environment you'll use to install the dependencies for the project. Now just run the environment with the next command:

```
source env/bin/activate
```

In order to create your own Telegram Bot, after cloning or downloading the code, you must get a TOKEN from the BotFather on Telegram. Just follow the instrucciones the bot gives you and create a .env file with your token like this:

```
BOT_TOKEN = your_token
```

## Dependencies

This project uses the next Python dependencies:

- [python-telegram-bot](https://python-telegram-bot.readthedocs.io/en/stable/)
- [bs4](https://www.crummy.com/software/BeautifulSoup/)
- [requests](https://docs.python-requests.org/en/latest/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

## Commands

- inicio: Sends a starting message
- ayuda: Sends a message with all the commands information
- hola: Sends a greetings message
- gato: Sends a random picture of a cat
- traducir: Translates a word. Receives a languajes code ("es", "en", etc) and the word to translate

## Disclaimer

This bot was built as a family joke, so it may contain some local jokes that could offend someone, altough that was never the intention.
