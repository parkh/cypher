from datetime import datetime


alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'


def coder(text, key, encode):
    result = ''
    index = 0

    for symbol in text:
        if symbol not in alphabet:
            result += symbol
            continue

        index_in_alphabet = alphabet.index(symbol)
        index_in_key = index % len(key)
        digit_from_key = key[index_in_key]
        digit_from_key = int(digit_from_key)

        if encode:
            new_index = index_in_alphabet + digit_from_key
        else:
            new_index = index_in_alphabet - digit_from_key
        new_index = new_index % len(alphabet)
        new_symbol = alphabet[new_index]

        index += 1
        result += new_symbol

    return result


def main():
    option = input('Введіть `1` якщо Ви хочете зашифрувати, і `0` якщо ви хочете розшифрувати: ')
    print('\n')
    if option == '1':
        encode = True
    elif option == '0':
        encode = False
    else:
        main()
        return


    date = input('Введіть дату (dd/mm/yyyy): ')
    print('\n')
    try:
        date_object = datetime.strptime(date, '%d/%m/%Y')
    except:
        main()
        return
    key = date_object.strftime('%d%m%Y')


    text = input('Введіть текст: ')
    print('\n')
    text = text.lower()

    result = coder(text, key, encode)
    print(f'Результат: {result}\n')


main()
