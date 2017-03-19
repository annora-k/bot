import configparser

def get_config():
	config = configparser.ConfigParser()
	config.read('configs/config.ini')

	return config
