phone_book = []

def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book
    
def add_contact(contact:list):
    global phone_book
    phone_book.append(contact)