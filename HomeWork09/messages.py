from bot_config import bot

async def print_help(user_id: int):
    await bot.send_message(user_id, 'Команды бота для игры в конфетки:'
                           f'\n/help - справка'
                           f'\n/setup - задать стартовое количество конфеток'
                           f'\n/start_game - начать игру')
    
async def print_setup_message(user_id: int, total: int):
    await bot.send_message(user_id, f'Текущее количество конфеток: {total}\n'
                           'Пожалуйста, укажи число конфеток \n'
                           'или напиши /stop_setup для выхода из настройки')
    
async def print_current_total(user_id: int, total: int):
    await bot.send_message(user_id, f'Текущее количество конфеток: {total}\n')
    
async def print_first_turn(user_id: int, username: str):
    await bot.send_message(user_id, f'Первым ходит {username}')
    
async def print_input_error(user_id: int):
    await bot.send_message(user_id, 'Укажи число, а не что-то странное')
    
async def print_turn_log(user_id: int, username: str, picked: int, total: int):
    await bot.send_message(user_id, f'{username} взял {picked} конфеток\n'
                           f'На столе осталось {total} конфет')
    
async def print_winner(user_id: int, username: str):
    await bot.send_message(user_id, f'Выиграл {username}')
    
async def print_start_message(user_id: int, username: str):
    await bot.send_message(user_id, text=f'{username}, привет!\n'
                           f'Добро пожаловать в бот для игры в конфетки\n')
    
async def print_invalid_pick(user_id: int):
    await bot.send_message(user_id, 'Можно взять от 1 до 28 конфет')