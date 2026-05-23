
import json

file_path = r"C:\Users\L123110\OneDrive - Eli Lilly and Company\Desktop\easier\api\env\env.json"

def load_config(config_file):
    with open(file_path, 'r') as f:
        return json.load(f)


config = load_config(file_path)



#Loading Telegram Bot Token 
TELEGRAM_BOT_TOKEN = config.get("TelegramToken")

