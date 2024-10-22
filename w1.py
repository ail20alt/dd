<python
    import requests
import os

# Replace '{6561194254:AAHDN7Bq8Z9HHD7C9LEN-B1Z8wVWl8bIlj0}/sendPhoto' with your actual bot token
BOT_TOKEN = '{6561194254:AAHDN7Bq8Z9HHD7C9LEN-B1Z8wVWl8bIlj0}/sendPhoto'
# Replace '5570996301' with your actual chat ID
CHAT_ID = '5570996301'
# Path to the image you want to send
IMAGE_PATH = 'path/to/your/image.jpg'

def send_image_to_telegram(image_path):
    with open(image_path, 'rb') as image_file:
        url = f'https://api.telegram.org/bot{6561194254:AAHDN7Bq8Z9HHD7C9LEN-B1Z8wVWl8bIlj0}/sendPhoto'
        files = {'photo': image_file}
        data = {'chat_id': 5570996301}
        response = requests.post(url, files=files, data=data)
        return response.json()

if __name__ == "__main__":
    if os.path.exists(IMAGE_PATH):
        response = send_image_to_telegram(IMAGE_PATH)
        print(response)
    else:
        print("Image file does not exist.")









from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('11.html')

if __name__ == '__main__':
    app.run(debug=True)
    



import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the bot token (replace 'YOUR_BOT_TOKEN' with your actual bot token)
BOT_TOKEN = '6561194254:AAHDN7Bq8Z9HHD7C9LEN-B1Z8wVWl8bIlj0'

# Function to start the bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send me an image and I will forward it to the chat.')

# Function to handle image uploads
def handle_image(update: Update, context: CallbackContext) -> None:
    # Get the file from the message
    file = update.message.photo[-1].get_file()
    
    # Define the path to save the image
    file_path = os.path.join('images', f"{update.message.photo[-1].file_id}.jpg")
    
    # Download the image
    file.download(file_path)
    
    # Send the image back to the chat
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(file_path, 'rb'))

# Main function to run the bot
def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(6561194254:AAHDN7Bq8Z9HHD7C9LEN-B1Z8wVWl8bIlj0)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command and message handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.photo, handle_image))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()