from aiogram import types
from random import randint
import messages
import user

total = 150
flag = False

player_counter = 0
bot_counter = 0

in_game = False
in_setup = False

def set_in_game(state: bool):
    global in_game
    in_game = state
    
def check_in_game():
    global in_game
    return in_game

def set_in_setup(state: bool):
    global in_setup
    in_setup = state
    
def check_in_setup():
    global in_setup
    return in_setup
    
async def set_total(new_total: int):
    global total
    total = new_total
    user_data = user.get_user()
    await messages.print_current_total(user_data.id, new_total)
    
def get_total():
    global total
    return total

async def start_game():
    global flag
    if check_in_game():
        return
    user_data = user.get_user()
    flag = bool(randint(0, 1))
    set_in_game(True)
    if flag:
        await messages.print_first_turn(user_data.id, user_data.username)
    else:
        await messages.print_first_turn(user_data.id, 'Бот')
        await bot_turn()

async def play(message: types.Message):
    user_data = user.get_user()
    if check_in_setup():
        if message.text.isdigit():
            await set_total(int(message.text))
        else:
            await messages.print_input_error(user_data.id)
        return
        
    if check_in_game():
        if message.text.isdigit():
            await player_turn(int(message.text))
        else:
            await messages.print_input_error(user_data.id)
        return
        
async def bot_turn():
    picked = randint(1,29)
    await bot_pick(picked)
    if check_winner():
        await print_winner()
    
async def player_turn(picked: int):
    user_data = user.get_user()
    if 1 < picked < 28:
        await player_pick(picked)
        if check_winner():
            await print_winner()
        else:
            await bot_turn()
    else:
        await messages.print_invalid_pick(user_data.id)
    
async def bot_pick(picked: int):
    global flag
    global bot_counter
    global total
    bot_counter += picked
    total -= picked
    flag = True
    user_data = user.get_user()
    await messages.print_turn_log(user_data.id, 'Бот', picked, total)
    
async def player_pick(picked: int):
    global flag
    global player_counter
    global total
    player_counter += picked
    total -= picked
    flag = False
    user_data = user.get_user()
    await messages.print_turn_log(user_data.id, user_data.username, picked, total)
    
async def print_winner():
    global flag
    user_data = user.get_user()
    if flag:
        await messages.print_winner(user_data.id, user_data.username)
    else:
        await messages.print_winner(user_data.id, 'Бот')
    set_in_game(False)
        
def check_winner():
    global total
    
    return total <= 28

async def start_setup():
    global total
    set_in_setup(True)
    user_data = user.get_user()
    await messages.print_setup_message(user_data.id, total)
    
async def stop_setup():
    global total
    user_data = user.get_user()
    await messages.print_current_total(user_data.id, total)
    set_in_setup(False)