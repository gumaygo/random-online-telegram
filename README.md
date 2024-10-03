Random Telegram Online Status Bot
This project is a Python bot that uses the Telethon library to set your Telegram account status as online or offline at random intervals. It ensures that your Telegram account stays online for a random period between 30 to 120 seconds and goes offline for a random period between 30 to 90 seconds, ensuring that it's never offline for more than 2 minutes.

The project uses environment variables stored in a .env file to manage sensitive information like the API ID, API Hash, and phone number.

Features:
Randomly switches your Telegram status between online and offline.
Online duration is set randomly between 30 to 120 seconds.
Offline duration is set randomly between 30 to 90 seconds (never offline for more than 2 minutes).
Manages API credentials securely with a .env file for easy configuration.
Built using the Telethon library.
Prerequisites:
Python 3.x
Telethon library
python-dotenv library