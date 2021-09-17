from commands.command_docs import get_commands
from commands.translator import translate
import requests

from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    """Send a message when the command /inicio is issued."""
    update.message.reply_text("Hola!")


def help(update: Update, context: CallbackContext):
    """Send a message when the command /ayuda is issued."""
    update.message.reply_text(get_commands())


def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def saludar(update: Update, context: CallbackContext):
    """The bot says hi when the command /hola is issued"""
    update.message.reply_text("Buenos dias a todos menos a Calderon")


def enviar_gato(update: Update, context: CallbackContext):
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    data = response.json()[0]
    update.message.reply_photo(data["url"])


def traducir(update: Update, context: CallbackContext):
    [target, text] = context.args
    origin = "es" if target == "en" else "en"
    translated_text = translate(text, origin, target)
    update.message.reply_text(f"{text} - {translated_text}")
