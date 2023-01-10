from aiogram import types

user = {}

def set_user(user_data: types.User):
    global user
    user = user_data
    
def get_user():
    global user
    return user