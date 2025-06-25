messages = dict()

def add_message(firstname, lastname, email, message):
    messages[email] = {"firstname":firstname, "lastname":lastname, "message":message}