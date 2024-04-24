#!/usr/bin/env python3

import logging
import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


load_dotenv()
api_key = os.getenv('bot_api_key')
gmail_key = os.getenv('gmail_api_key')
sender = os.getenv('sender')
recipients = os.getenv('recipients')
sending_bot_id = os.getenv('sending_bot_id')

bot = AsyncTeleBot(api_key)
print('Bot is running')

@bot.message_handler(func=lambda message: message.from_user.id == sending_bot_id)
async def manipulate_message(message):
    await print(message.text)

asyncio.run(bot.polling())
