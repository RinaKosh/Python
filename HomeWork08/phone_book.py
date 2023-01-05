phone_book = []

def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book
    
def add_contact(contact):
    global phone_book
    phone_book.append(contact)
    
def remove_contact(id):
    global phone_book
    name = phone_book[id-1][0]
    confirm = input(f'Вы дейстивтельно хотите удалить контакт {name}? (y/n) ')
    if confirm.lower() == 'y':
        phone_book.pop(id-1)
        return True
    return False
        
def update_contact(id, contact_updated):
    global phone_book
    contact = phone_book[id-1]
    if contact_updated[0]:
        contact[0] = contact_updated[0]
    if contact_updated[1]:
        contact[1] = contact_updated[1]
    if contact_updated[2]:
        contact[2] = contact_updated[2]
    phone_book[id-1] = contact
    
def search(string):
    global phone_book
    search_result = []
    
    for i in range(len(phone_book)):
        contact = phone_book[i]
        [name, phone, comment] = contact
        if string in name or string in phone or string in comment:
            search_result.append(contact)
    
    return search_result