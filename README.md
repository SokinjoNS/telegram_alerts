# Telegram Alerts Module

The __telegram_alerts.py__ is a comprehensive alerting module designed for a Telegram bot application. It not only facilitates sending formatted alerts about cryptocurrency volume changes on exchanges like Binance and Kucoin but also integrates with Dextools and Dexscreener URL listeners for broader monitoring capabilities. Utilizing additional modules for formatting and determining alert levels, this script stands as a central hub for notification dispatch within the bot ecosystem.

## Features

__- Versatile Alerting:__ Supports a wide range of alerts including exchange volume changes, Dextools and Dexscreener link detections, and direct address alerts.

__- Dynamic Message Formatting:__ Leverages the __formatting_btk__ module to format numerical values for easier readability.

__- Alert Level Analysis:__ Integrates with __alert_levels_tg__ to assess and communicate the significance of volume changes.

__- Secure Configuration:__ Manages sensitive information such as API keys and bot tokens through a dedicated __credentials_telegram.json__ file.

# Dependencies

__- Python 3.6+:__ Required for running the script.

__- Requests:__ For making HTTP requests to the Telegram API.

__- formatting_btk:__ A custom module for formatting numbers.

__- alert_levels_tg:__ A custom module for determining and describing alert levels based on predefined criteria.

## Installation

__1. Ensure Python and Pip are installed:__

Verify Python 3.6+ and pip are installed on your system by running __python --version__ and __pip --version__.

__2. Install Dependencies:__

Install the Requests library and ensure __formatting_btk__ and __alert_levels_tg__ modules are accessible within your project environment:

```bash
pip install requests
```

__3. Configure Credentials:__

Edit __credentials_telegram.json__ to include your Telegram bot's credentials. This file should be securely stored and properly referenced by the script.

```bash
{
  "Telegram_bot_token": "INSERT YOUR TELEGRAM BOT TOKEN HERE (operational bot-1)",
  "Telegram_chat_id": "INSERT THE TELEGRAM CHAT ID HERE WHERE YOU WANT TO RECEIVE TELEGRAM BOT NOTIFICATIONS (operational chat_id-1)"
  "bot_token_1": "insert your_bot_token_here (operational bot-2)",
  "chat_id_1": "insert your_listener_chat_id_here (operational chat_id-2)",
  "response_chat_id": "insert your_response_chat_id_here",
  "api_id": "insert_your_api_id_here",
  "api_hash": "insert_your_api_hash_here",
  "dextools_api_key": "insert_your_dextools_api_key_here"
}
```

## Usage

The script is designed to be imported and utilized by other components within the bot application:

```bash
from telegram_alerts import handle_and_send_message

# Example alert details
alert_details = {
    'exchange': 'Binance',
    'symbol': 'BTC/USDT',
    'curr_volume': 10234.56,
    'prev_volume_mean': 9786.43,
    'level': 'High',
    'chart_url': 'https://example.com/chart'
}

credentials = load_telegram_credentials()
send_telegram_message(alert_details)
```

This will format and send an alert message to the specified Telegram chat or channel based on the provided details.

## Contributing

Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Support

For issues, questions, or contributions, please open an issue in the GitHub repository.

Feedback and contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
