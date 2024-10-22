import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update
import openai

# Set up the OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to generate a response using OpenAI
def generate_response(user_input: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response['choices'][0]['message']['content']

# Function to handle incoming messages
def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    bot_response = generate_response(user_input)
    update.message.reply_text(bot_response)

# Main function to start the bot
def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater("6561194254:AAHDN7Bq8Z9HHD7C9LEN-B1Z8wVWl8bIlj0")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()