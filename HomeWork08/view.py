

def main_menu():
    print('\nВыберите пункт меню: ')
    print('1. Показать телефонную книгу')
    print('2. Открыть файл телефонной книги')
    print('3. Сохранить файл телефонной книги')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выход\n')
    return choice_main_menu()
    
def choice_main_menu():
    while True:
        try:
            choice = int(input('Выберите команду из меню: '))
            if choice in range(0,8):
                print()
                return choice
            else:
                print('Указанный пункт отсутствует, повторите попытку!')
        except:
            print('Ошибка ввода! Некорректные данные!')
            
def print_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    else:
        print('Телефонная книга пуста или не загружена')

def log_off():
    print('До свидания, до новых встреч!')
    
def load_success():
    print('Телефонная книга загружена')
    
def save_success():
    print('Телефонная книга сохранена')
    
def input_new_contact():
    name=input('Введите имя контакта: ')
    phone=input('Введите телефон: ')
    comment=input('Введите коментарий к контакту: ')
    
    return [name, phone, comment]