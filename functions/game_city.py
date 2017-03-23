import importlib
import random

import data.city as city

last_city_letter = None

def get_city():
	choice = random.choice(city.cities)
	city.cities.remove(choice)
	return choice

def get_city_letter(city):
	letters = 'ьъый'
	if city[-1] in letters:
		if city[-2] in letters:
			return city[-3]
		else:
			return city[-2]
	else:
		return city[-1]


def check_city(bot, update):
	global last_city_letter

	text = update.message.text
	text = text.replace('/city', '')
	user_city = text.replace(' ', '')

	if not user_city:
		importlib.reload(city)

		bot_city = get_city()

		last_city_letter = get_city_letter(bot_city)

		bot.sendMessage(update.message.chat_id, 'Город {}, тебе на {}'.format(bot_city, last_city_letter.upper()))
	else:
		if user_city in city.cities:
			if last_city_letter and user_city[0] != last_city_letter.upper():
				bot.sendMessage(update.message.chat_id, 'Не жульничай! тебе на {}'.format(last_city_letter.upper()))
				return

			city.cities.remove(user_city)

			last_city_letter = get_city_letter(user_city)

			if not city.cities:
				bot.sendMessage(update.message.chat_id, 'Городов больше нет. Ты выиграл, чтобы начать заново введи /city')

			for city_list in city.cities:
				if city_list[0] == last_city_letter.upper():
					bot_city = city_list
					city.cities.remove(bot_city)
					last_city_letter = get_city_letter(bot_city)
					if not city.cities:
						bot.sendMessage(update.message.chat_id, 'Я загадал город {}, но больше городов нет. Ты проиграл, чтобы начать заново введи /city'.format(bot_city))
					else:
						bot.sendMessage(update.message.chat_id, 'Город {}, тебе на {}'.format(bot_city, last_city_letter.upper()))
					break
		else:	
			bot.sendMessage(update.message.chat_id, 'Города {} не существует, попробуй еще раз'.format(user_city))
