from telegram.ext import Updater, CommandHandler, InlineQueryHandler, Dispatcher
from telegram.ext.dispatcher import run_async
import requests
import re
import os


MY_TOKEN = ''  # go to @botfather to make a new bot then paste the token here
request_url = 'https://random.dog/woof.json'

def getURL():
    contents = requests.get(request_url).json()
    url = contents['url']
    return url

def getURLImages():
    pattern = r'([^.]*)$'  # make a pattern to get the file extension
    allowed_ext = ['jpg', 'jpeg', 'png', 'gif']  # extension is allowed
    file_ext = ''
    while file_ext not in allowed_ext:
        url = getURL()
        file_ext = re.search(pattern, url).group(1).lower()
    return url

# run dog command asynchorously
@run_async
def dog(update, context):
    image = getURLImages()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=image)

def main():
    updater = Updater(MY_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dog', dog))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
