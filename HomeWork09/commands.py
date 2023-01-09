from aiogram import types
from bot_config import dp, bot

total = 150

@dp.message_handler(commands=['start'])

async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                           f', Hello!')
    
    print(f'{message.from_user.id} - {message.from_user.username}')
    
@dp.message_handler()
async def anything(message: types.Message):
    global total
    text, first_ = message
    if message.text.isdigit():
        if 0 < int(message.text) < 29:
            total -= int(message.text)
            await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                   f' взял со стола {message.text} конфет. '
                                   f'На столе осталось {total}')