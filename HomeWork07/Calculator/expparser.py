def is_operator(char):
    return char in ['-', '+', '/', '*', '=']

def trim_space(string):
    return ''.join(string.split())
    
def check_not_valid(string: str):
    invalid = False
    for i in range(len(string)):
        char = string[i]
        if not is_operator(char) and not char.isdigit():
            invalid = True
            break
        if i + 1 < len(string):
            next_char = string[i + 1]
            if is_operator(char) and is_operator(next_char):
                invalid = True
                break
    if invalid:
        return invalid
    
    return invalid

def parse(string):
    result = []
    value = ''
    for i in range(len(string)):
        char = string[i]
        if is_operator(char):
            print(char, value)
            result.append(int(value))
            result.append(char)
            value = ''
        else:
            value += char
    return result
    