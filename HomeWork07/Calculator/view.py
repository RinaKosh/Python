def input_number_or_expretion():
    string = str(input('Введите число или выражение '))
    try:
        number = int(string)
        return number
    except:
        return string
    
def input_number():
    while True:
        try:
            number = int(input('Введите число '))
            return number
        except:
            print('Ошибка!')

def input_operation():
     while True:
        operation = input('Введите операцию ')
        if operation in ['+','-','*','/','=']:
            return operation
        else:
            print('Введите корректную операцию!')

def print_to_console(value_text):
    print(value_text)
    
def log_off():
    print('До свидания!')
    
def print_division_by_zero():
    print('На ноль делить нельзя')
    
def print_incorrect_expretion_format():
    print('Неверный формат выражения')