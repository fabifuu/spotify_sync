import src.config as config
from pushover import Client

config = config.load()
client = Client(config['pushover']['user_key'], api_token=config['pushover']['api_token'])


def send_notification(title, message):
    client.send_message(message, title=title)

