phone_book = {'igor': 123,
              'dima': 145
              }


def input_error(funk):
    def inner(text_input=None):
        try:
            if len(text_input.split()) > 3:
                print('to many parameters')
                return
            if len(text_input.split()) == 3:
                text_input.split()[1] == str(text_input.split()[1])
                text_input.split()[2] == int(text_input.split()[2])
            return funk(text_input)
        except (AttributeError, IndexError, ValueError, KeyError):
            print('Enter name or phone correctly')
    return inner


def hello(_=None):
    print('How can I help you?')


def show_all(_=None):
    for k, v in phone_book.items():
        print(f'{k}:{v}')


@ input_error
def add(text_input: str):
    if text_input.split()[1] not in phone_book:
        phone_book[text_input.split()[1]] = text_input.split()[2]
        print('Its done')
    else:
        print('This contact is exist')


@ input_error
def change(text_input: str):
    if text_input.split()[1] in phone_book:
        phone_book[text_input.split()[1]] = text_input.split()[2]
        print('it was changed')
    else:
        print('no contact')


@ input_error
def phone(text_input: str):
    print(phone_book[text_input.split()[1]])


USER_INPUT = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all
}


def main():
    while True:
        user_input = input('Enter something  ')
        user_input = user_input.lower()
        if user_input == '.':
            break
        if user_input == 'good bye' or user_input == 'close' or user_input == 'exit':
            print('Good bye!')
            break
        if user_input in USER_INPUT:
            USER_INPUT[user_input]()
        elif user_input.split()[0] in USER_INPUT:
            USER_INPUT[user_input.split()[0]](user_input)


main()
