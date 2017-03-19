def calc(bot, update):
	
	expression = update.message.text.replace('/calc', ' ')
	expression = expression.replace(' ', '')
	
	if expression[-1] == '=':
		result = None
		expression = expression.replace('=', '')
		if '-' in expression:
			a, b = expression.split('-')
			result = int(a) - int(b)
		elif '+' in expression:
			a, b = expression.split('+')
			result = int(a) + int(b)
		elif '*' in expression:
			a, b = expression.split('*')
			result = int(a) * int(b)
		elif '/' in expression:
			a, b = expression.split('/')
			try:
				result = int(a) / int(b)
			except ZeroDivisionError:
				bot.sendMessage(update.message.chat_id, 'Нельзя делить на ноль')

		if result:
			bot.sendMessage(update.message.chat_id, result)

	else:
		bot.sendMessage(update.message.chat_id, 'Это не выражение')
		