def greet_user(bot, update):
	print('AAA')
	print(update)
	bot.sendMessage(update.message.chat_id, text = 'Давай общаться')
