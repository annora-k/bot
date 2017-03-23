import logging

from telegram.ext import Updater, CommandHandler

from configs.config_reader import get_config
from functions.greet_user import greet_user
from functions.word_count import get_word_count
from functions.calc import calc
from functions.word_calc import word_calc
from functions.moon import get_next_full_moon
from functions.game_city import check_city

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG)

def main():
	config = get_config()
	updater = Updater(config['telegram']['api_token'])

	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start', greet_user))
	dp.add_handler(CommandHandler('wordcount', get_word_count))
	dp.add_handler(CommandHandler('calc', calc))
	dp.add_handler(CommandHandler('word', word_calc))
	dp.add_handler(CommandHandler('moon', get_next_full_moon))
	dp.add_handler(CommandHandler('city', check_city))


	dp.add_error_handler(show_error)

	updater.start_polling()
	updater.idle()

def show_error(bot, update, error):
	print(error)

main()
