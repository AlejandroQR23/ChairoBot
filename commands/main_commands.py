from telegram import update


def start(update, context):
    """Send a message when the command /inicio is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /ayuda is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def saludar(update, context):
    """The bot says hi when the command /hola is issued"""
    update.message.reply_text('Buenos dias a todos menos a Calderon')
