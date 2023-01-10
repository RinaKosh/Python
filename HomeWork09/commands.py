from aiogram import types
from bot_config import dp

import game
import messages
import user

@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await messages.print_start_message(message.from_user.id, message.from_user.username)
    await messages.print_help(message.from_user.id)
    
@dp.message_handler(commands=['help'])
async def print_help(message: types.Message):
    await messages.print_help(message.from_user.id)

@dp.message_handler(commands=['setup'])
async def setup(message: types.Message):
    user.set_user(message.from_user)
    if game.check_in_game():
        return
    await game.start_setup()
    
@dp.message_handler(commands=['stop_setup'])
async def stop_setup(message: types.Message):
    user.set_user(message.from_user)
    if game.check_in_game() or not game.check_in_setup():
        return
    await game.stop_setup()

@dp.message_handler(commands=['start_game'])
async def start_game(message: types.Message):
    user.set_user(message.from_user)
    if game.check_in_game():
        return
    await game.start_game()

@dp.message_handler()
async def play(message: types.Message):
    await game.play(message)