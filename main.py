from datetime import datetime


alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'


def coder(message, key, encode):
    result = ''
    index = 0

    for symbol in message:
        if symbol not in alphabet:
            result += symbol
            continue

        current_letter_index = alphabet.index(symbol)

        index_in_key = index % len(key)
        number_string = key[index_in_key]
        number = int(number_string)

        if encode:
            new_letter_index = current_letter_index + number
        else:
            new_letter_index = current_letter_index - number

        new_letter_index = new_letter_index % len(alphabet)
        new_letter = alphabet[new_letter_index]

        index += 1
        result += new_letter

    return result


def main():
    the_type = input('Введіть `1` якщо Ви хочете зашифрувати, і `0` якщо ви хочете розшифрувати:\n')

    if the_type == '1':
        encode = True
    elif the_type == '0':
        encode = False
    else:
        main()
        return

    date = input('Введіть дату (dd/mm/yyyy):\n')

    try:
        date_object = datetime.strptime(date, '%d/%m/%Y')
    except:
        main()
        return

    key = date_object.strftime('%d%m%Y')

    message = input('Введіть текст:\n')
    message = message.lower()

    result = coder(message, key, encode)

    print(f'Результат: {result}')


main()
