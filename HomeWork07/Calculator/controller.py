import view
import model
import expparser as parser

expresion = []

def input_first():
    global expresion
    data = view.input_number_or_expretion()
    try:
        if data == int(data):
            model.set_first(int(data))
    except:
        string = parser.trim_space(data)
        if (parser.check_not_valid(string)):
            view.print_incorrect_expretion_format()
            return
        expresion = parser.parse(string)
    
def input_second():
    while True:
        number = view.input_number()
        if number == 0 and model.get_operation() == '/':
            view.print_division_by_zero()
        else:
            model.set_second(number)
            break

def input_operation():
    oper = view.input_operation()
    model.set_operation(oper)

def solution():
    oper = model.get_operation()
    if oper == '+':
        model.addition()
    elif oper == '-':
        model.difference()
    elif oper == '*':
        model.multiplication()
    elif oper == '/':
        model.division()
    
    model.set_first(model.get_result())
    return 
    
def line_calculator():
    while True:
        input_operation()
        if model.get_operation() == '=':
            view.log_off()
            break
        input_second()
        solution()
        result_string = f'{model.get_first()} {model.get_operation()} {model.get_second()} = {model.get_result()}'
        view.print_to_console(result_string)

def expresion_calculator():
    model.set_first(expresion[0])
    for i in range(1, len(expresion)):
        part = expresion[i]
        if (parser.is_operator(part)):
            model.set_operation(part)
            if model.get_operation() == '=':
                break
        else:
            model.set_second(int(part))
            solution()
    result = []
    for i in range(len(expresion)):
        result.append(str(expresion[i]))
    result.append(str(model.get_result()))
    result_string = ' '.join(result)
    view.print_to_console(result_string)
    view.log_off()
    
def start():
    input_first()
    if (expresion == []):
        line_calculator()
    else:
        expresion_calculator()
    