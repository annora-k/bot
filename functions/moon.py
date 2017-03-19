import datetime
import ephem

def get_next_full_moon(bot, update):
	text = update.message.text.replace('?', '')
	text = text.replace('"', '')
	text = text.replace('\'', '')

	text_list = text.split()
	moon_date = None
	for word in text_list:
		try:
			moon_date = datetime.datetime.strptime(word, '%d.%m.%Y')
		except ValueError:
			pass
		
	if moon_date:
		next_moon_date = ephem.next_full_moon(moon_date)
		bot.sendMessage(update.message.chat_id, 'Следующие полнолуние: {}'.format(next_moon_date))
	else:
		next_moon_date = ephem.next_full_moon(datetime.date.today())
		bot.sendMessage(update.message.chat_id, 'Следующие полнолуние после сегодня: {}'.format(next_moon_date))
