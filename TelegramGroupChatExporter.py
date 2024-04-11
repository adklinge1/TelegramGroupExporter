import asyncio
from datetime import datetime, timedelta
from telethon import TelegramClient, events, utils
import pandas as pd
import nltk
# Replace the values with your own API ID, API hash and phone number
# enter your api id from telegram website
api_id = "28479308"
api_hash = 'a4f1ffa4c55177e2e35cac280cfb6031'
# enter your api hash form telegram api website
#phone_number = '+972504737047'
# enter your pone number on this formate

group_name = -4153270726
# enter your channel group id -100 after this digit

# Set the time range to get messages from
start_time = datetime.now() - timedelta(hours=24)
flag=0

phone_number = input("What is your phone number?")
async def get_group_messages():
    df = pd.DataFrame({'Data':[''],'name':[''],'mobile':['']})
    df1 = pd.DataFrame({'Data':[''],'name':[''],'mobile':['']})
    # Create a Telegram client with the specified API ID, API hash and phone number
    client = TelegramClient('session_name', api_id, api_hash)
    await client.connect()

    # Check if the user is already authorized, otherwise prompt the user to authorize the client
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Enter the code: '))

    # Get the ID of the specified group
    group = await client.get_entity(group_name)
    date_today = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    
    yesterday = date_today - timedelta(days=5)
    messages = []
    messageString = ""
    # below commented code is used for  specified time range
    async for message in client.iter_messages(group, min_id=1):
        result =  await client.get_entity(message.from_id)
        print(result.first_name, message.date)    
        if str(message.date) < str(yesterday):
            break
        messages.append(str(message.message))
        messageString +=f"{message.date},{result.first_name} {result.last_name},{str(message.message)}\n"
    with open("telegramMessages.txt", 'w', encoding = 'utf-8') as file:
        lines = messageString
        for line in lines:
            file.write(line)
    df = pd.read_csv('telegramMessages.txt')
    df.to_csv('telegramMessages.csv', index=None)

     
asyncio.run(get_group_messages())
    