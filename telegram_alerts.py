import requests
import json
from formatting_btk import format_number
from alert_levels_tg import get_volume_alert_details

# List to store message details temporarily
message_storage = []

def load_telegram_credentials():
    with open('credentials_telegram.json') as f:
        credentials = json.load(f)
    return credentials

def send_telegram_message(alert_details):
    credentials = load_telegram_credentials()
    bot_token = credentials['Telegram_bot_token']
    chat_id = credentials['Telegram_chat_id']
    
    # Formulate the message based on alert_details
    message = f"*{alert_details['exchange']} Alert*\n"
    message += f"Symbol: {alert_details['symbol']}\n"
    message += f"Current Volume: {format_number(alert_details['curr_volume'])}\n"
    message += f"Mean Volume (24h): {format_number(alert_details['prev_volume_mean'])}\n"
    message += f"Alert Level: {alert_details['level']}\n"
    message += f"[View Chart]({alert_details['chart_url']})"

    # Add message details to storage list
    message_storage.append(alert_details)

    # Send the message to Telegram
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}&disable_web_page_preview=True'
    response = requests.get(send_text)
    
    # Return the response
    return response.json()
