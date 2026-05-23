
import json
import os 



file_path = os.path.join(os.path.dirname(__file__), 'env', 'env.json')



def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


config = load_config(file_path)



#Loading Telegram Bot Token 
TELEGRAM_BOT_TOKEN = config.get("TelegramToken")
print(f"Loaded Telegram Bot Token: {TELEGRAM_BOT_TOKEN[:5]}...")  # Print only the first 5 characters for security



