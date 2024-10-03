import random
import time
from telethon import TelegramClient

# Masukkan API ID, API Hash, dan nomor telepon Telegram Anda
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone = 'YOUR_PHONE_NUMBER'

# Buat instance TelegramClient
client = TelegramClient('session_name', api_id, api_hash)

async def random_online_status():
    try:
        # Start the client
        await client.start(phone)
        
        print("Client started successfully!")
        
        while True:
            # Randomly set online status with random intervals
            online_time = random.randint(30, 120)  # Online time between 30 to 120 seconds
            await client.send_message('me', 'Setting status to online')
            await client(functions.account.UpdateStatusRequest(offline=False))  # Set status online
            print(f"Online for {online_time} seconds.")
            time.sleep(online_time)

            # Set offline for a random time, but less than 2 minutes
            offline_time = random.randint(30, 90)  # Offline time between 30 to 90 seconds
            await client.send_message('me', 'Setting status to offline')
            await client(functions.account.UpdateStatusRequest(offline=True))  # Set status offline
            print(f"Offline for {offline_time} seconds.")
            time.sleep(offline_time)
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Jalankan client
with client:
    client.loop.run_until_complete(random_online_status())
