def greet_user(bot, update):
	print('AAA')
	print(update)
	bot.sendMessage(
		update.message.chat_id,
		'Давай общаться!\n\n'
		'Доступные команды:\n\n'
		'/wordcount текст\n'
		'/calc простые выражения 2+2=\n'
		'/word Сколько будет два плюс три?\n'
		'/moon Когда будет следующее полнолуние после 01.01.2017?'
	)
