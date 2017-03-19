def get_word_count(bot, update):
	symbols  = ',.?@#%:()+-=\'"'
	text = update.message.text
	text = text.replace("/wordcount", "")
	text_cleared = ''

	for symbol in text:
		if symbol not in symbols:
			text_cleared += symbol

	count = len(text_cleared.split())  
	bot.sendMessage(update.message.chat_id, 'Вы ввели {} слов'.format(count))
