from telegram.ext import Updater, CommandHandler, InlineQueryHandler, Dispatcher
from telegram.ext.dispatcher import run_async
import requests
import re
import os


MY_TOKEN = '951399920:AAEyHcV6BbFwekwMEd48QBhsThiYKG7a0bQ'
request_url = 'https://random.dog/woof.json'

def getURL():
    contents = requests.get(request_url).json()
    url = contents['url']
    return url

def getURLImages():
    pattern = r'([^.]*)$'  # make a string pattern
    allowed_ext = ['jpg', 'jpeg', 'png', 'gif']  # extension is allowed
    file_ext = ''
    while file_ext not in allowed_ext:
        url = getURL()
        file_ext = re.search(pattern, url).group(1).lower()
    return url

@run_async
def dog(update, context):
    image = getURLImages()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=image)

def main():
    # port = int(os.environ.get('PORT', 5000))
    updater = Updater(MY_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dog', dog))
    updater.start_polling()

    # updater.start_webhook(
    #     listen='0.0.0.0',
    #     port=port,
    #     url_path=MY_TOKEN
    # )
    # updater.bot.set_webhook("https://dogs-bot.herokuapp.com" + MY_TOKEN)
    updater.idle()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
