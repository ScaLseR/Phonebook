import re
phonebook = {}

#создание префиксного дерева поиска
def get_tree(key: str, value: str) -> None:
    current = phonebook
    for character in key:
        if character not in current:
            current[character] = {}
        current = current[character]
    if key.isalpha():
        current['value'] = value
    else:
        if 'value' not in current:
            current['value'] = {value}
        else:
            current['value'].add(value)

#вывод результатов поиска по дереву
def tree_in_console(level: dict, find: str) -> None:
    if 'value' in level:
        if [dig for dig in find if dig in '1234567890']:
            print(*level['value'], find)
        else:
            print(find, *level['value'])
    for k, v in level.items():
        if k == 'value':
            continue
        tree_in_console(v, find+k)

#поиск по префиксному дереву по 1 wildcard, фио или телефон
def search_tree(find):
    current = phonebook
    for character in find:
        if character in current:
            current = current[character]
    tree_in_console(current, find)

#создание словаря для поиска по полному совпадению фио или телефона
def full_dicts_fo_search(digit: bool, tree: bool) -> None:
    with open("./1_WildcardSearchData.txt", "r") as file:
        for line in file:
            name, phone = line.strip().split(',')
            if tree == False:
                if digit == True:
                    phonebook[phone] = name
                else:
                    if phonebook.get(name) == None:
                        phonebook[name] = {phone}
                    else:
                        phonebook[name].add(phone)
            else:
                if digit == True:
                    get_tree(phone, name)
                else:
                    get_tree(name, phone)

#поиск по 1 wildcard фио или телефон
def dicts_to_search_wildcart(find: str, digit: bool) -> None:
    with open("./1_WildcardSearchData.txt", "r") as file:
        for line in file:
            name, phone = line.strip().split(',')
            if digit == True:
                rez = re.match(r'{}'.format(find), phone)
                if rez != None:
                    phonebook[phone] = name
            else:
                rez = re.match(r'{}'.format(find), name)
                if rez != None:
                    if phonebook.get(name) == None:
                        phonebook[name] = {phone}
                    else:
                        phonebook[name].add(phone)

#простой поиск по фио или телефону
def find_name_phone(find: str, digit: bool) -> None:
    if phonebook.get(find) != None:
        if digit == True:
            print(phonebook[find] + ' ' + find)
        else:
            print(find, ', '.join(phonebook[find]))
    else:
        print('Введенной фамилии нет в справочнике!')

#печать конечного словаря при поиске по 1 wildcard
def phonebook_on_console(digit: bool) -> None:
    if digit == True:
        for key, value in phonebook.items():
            print(value, ' ', key)
    else:
        for key, value in phonebook.items():
            print(key, ' ', *value)

#реверс местами ключи и значения первого поиска wildcard по номеру телефона и поиск с последующим выводом по wildcard фио
def reverse_dicts_find_name(f_name: str) -> None:
    ph_t = {}
    for phone, name in phonebook.items():
        if ph_t.get(name) == None:
            ph_t[name] = {phone}
        else:
            ph_t[name].add(phone)
    for key in ph_t:
        rez = re.match(r'{}'.format(f_name), key)
        if rez != None:
            print(key, ', '.join(ph_t[key]))

#основная логика
def select_find():
    find = input('Введите имя или телефон: ')
    if find.endswith('*'):
        tree = True
        #поиск по wildcard фио или телефона с помощью префиксного дерева
        if find.count('*') == 1:
            find = find.strip('*')
            if find.isalpha():
                digit = False
                full_dicts_fo_search(digit, tree)
            else:
                digit = True
                full_dicts_fo_search(digit, tree)
            search_tree(find)

        #перекрестный поиск по телефону и фио по нескольким wildcart
        elif find.count('*') >= 2:
            f1, f2 = find.split(' ')
            if [dig for dig in f1 if dig in '1234567890']:
                f_name = f2
                f_phone = f1
            else:
                f_name = f1
                f_phone = f2
            f_phone = f_phone.replace('*', '.*')
            f_name = f_name.replace('*', '.*')
            dicts_to_search_wildcart(f_phone, True)
            reverse_dicts_find_name(f_name)
    else:
        #поиск по полному совпадению фио или телефона
        tree = False
        if [dig for dig in find if dig in '1234567890']:
            digit = True
            full_dicts_fo_search(digit, tree)
            find_name_phone(find, digit)
        else:
            digit = False
            full_dicts_fo_search(digit, tree)
            find_name_phone(find, digit)

if __name__ == "__main__":
    select_find()
