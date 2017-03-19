def word_calc(bot, update):

	numbers = {
		'один': 1,
		'два': 2,
		'три': 3,
		'четыре': 4,
		'пять': 5,
		'шесть': 6,
		'семь': 7,
		'восемь': 8,
		'девять': 9,
		'десять': 10
	}

	text = update.message.text 
	text = text.lower()
	text = text.replace("?", "")
	text = text.split()
	
	words = []
	for word in text:
		if numbers.get(word):
			words.append(numbers[word])

	if len(words) == 2:
		a, b = words
		result = None
		if 'плюс' in text:
			result = a + b
		elif 'минус' in text:
			result = a - b
		elif 'умножить' in text:
			result = a * b
		elif 'разделить' in text:
			result = a / b

		if result:
			bot.sendMessage(update.message.chat_id, result)
		else:
			bot.sendMessage(update.message.chat_id, 'Не понял')
	else:
		bot.sendMessage(update.message.chat_id, 'Должно быть два числа')
