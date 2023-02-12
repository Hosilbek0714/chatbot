from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
import requests

url = "https://5f1c-91-90-218-203.in.ngrok.io/webhooks/rest/webhook"

@dp.message_handler()
async def bot_start(message: types.Message): 
    res = requests.post(url, json={"message": str(message)})
    await message.answer(str(res.json()))
    