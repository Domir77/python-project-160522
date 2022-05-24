# модуль работы со справкой

from shutil import get_terminal_size as gts
from math import floor, ceil

h = """Правила игры:

Список команд:

"""


# опишите функцию: что она делает?
def show_help():
    print(h)

# опишите функцию: что она делает?
def show_message(text=''):
    width = gts()[0] - 1
    half_width = (width - len(text) - 2)/2

    m = f"""\n{'|'*width}
{'|' + ' '*(width-2) + '|'}
{'|'+ ' ' * ceil(half_width) + text.upper() +  ' ' * floor(half_width)  + '|'}
{'|' + ' '*(width-2) + '|'}
{'|' * width}"""
    # если режет глаз отсутствие отступов, то можно ещё так определить эту строку
    # неявная конкатенация в явном выражении в скобках
    # m = (f"\n{'#' * width}"
    #      + f"\n{'#' + ' ' * (width - 2) + '#'}"
    #      + f"\n{'#' + ' ' * ceil(half_width) + text.upper() + ' ' * floor(half_width) + '#'}"
    #      + f"\n{'#' + ' ' * (width - 2) + '#'}"
    #      + f"\n{'#' * width}")
    print(m, end='\n\n')
