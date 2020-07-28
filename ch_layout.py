import os
import colorama

colorama.init(strip=False)

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def banner():
    print('{}'.format(colorama.Fore.BLUE))
    print("      __                         __                    __ ")
    print(" ____/ /  ___ ____  ___ ____    / /__ ___ _____  __ __/ /_")
    print("/ __/ _ \/ _ `/ _ \/ _ `/ -_)  / / _ `/ // / _ \/ // / __/")
    print("\__/_//_/\_,_/_//_/\_, /\__/__/_/\_,_/\_, /\___/\_,_/\__/ ")
    print("                  /___/   /___/      /___/                ")
    print("")
    print('{}                      by paran0id'.format(colorama.Fore.BLUE))
    print("----------------------------------------------------------")
    print('{}'.format(colorama.Fore.CYAN))

def ch_layout(text):
    en_chars = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
    ru_chars = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"
    trans_table = dict(zip(ru_chars, en_chars))
    return u''.join([trans_table.get(letter, letter) for letter in text])

def dialog():
    print('{}Перевести с русской раскладки на английскую:'.format(colorama.Fore.YELLOW))
    print('{}1. Файл с Вашего компьютера'.format(colorama.Fore.YELLOW))
    print('{}2. Строку, вводимую в консоль'.format(colorama.Fore.YELLOW))
    answer = None
    res = None
    while answer != '1' and answer != '2':
        answer = input('{}Выберите один из предложенных вариантов: '.format(colorama.Fore.YELLOW))
    if answer == '1':
        trans_file()
    elif answer == '2':
        trans_console()

def trans_file():
    file = ''
    out = 'output.txt'
    while file == '':
        file = input('Введите полный путь к исходному файлу: ')
    if os.path.isfile(file):
        f = open(file, 'r')
        f_out = open(out, 'w')
        for line in f:
            f_out.write(ch_layout(line))
        f.close()
        f_out.close()
        print('{}Результат сохранен в файле {} директории {}'.format(colorama.Fore.GREEN,out,os.path.dirname(os.path.abspath(__file__))))
    else:
        print('{}Указанного файла не существует. Попробуйте снова.'.format(colorama.Fore.RED))
        trans_file()

def trans_console():
    text = ''
    while text == '':
        text = input("Введите строку: ")
    try:
        res = ch_layout(text)
        print('{}Результат: {}'.format(colorama.Fore.GREEN,res))
    except Exception:
        print('{}Что-то пошло не так... Попробуйте ввести текст снова.'.format(colorama.Fore.RED))
        trans_console()

clear_screen()
banner()
dialog()
