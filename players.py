# модуль работы с данными игроков

from configparser import ConfigParser

# глобальные переменные
PLAYERS = {}
# PLAYERS = {'Ivan':[1,1,0]}
PLAYER = tuple()

SAVES = {}
# SAVES = {('ivan','ai1'):[[]],
#          ('ivan','oleg'):[[]]}

# опишите функцию: что она делает?
def read_ini():
    global PLAYERS, SAVES
    config = ConfigParser()

    if config.read('data.ini', encoding='utf-8'):

        PLAYERS = {name.title: [int(n) for n in score.split(',')]
                   for name, score in config['Scores'].items()}

        SAVES = {tuple(name.split(';')):
                     [[' ' if c == '-' else c for c in field[i:i+3]]
                       for i in range(0,9,3)]
                 for name , field in config['Saves'].items()}

        return True if config['General']['first'] == 'yes' else False

    else:
        raise FileExistsError

# опишите функцию: что она делает?
def save_ini():
    config = ConfigParser()

    config['Scores'] = {name: '.'.join((str(n) for n in score))
                        for name, score in PLAYERS.items()}

    config['Saves'] = {';'.join(name): ''.join(['-' if c == ' ' else c for r in field for c in r])
                       for name, field in SAVES.items()}

    config['General']['first'] = 'no'

    with open('data.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)

# опишите функцию: что она делает?
def player_name(bot_mode=''):
    global PLAYER
    # если имя игрока еще не вводилось
    if len(PLAYER) == 0:
        PLAYER = (input().lower(), )
    #
    elif len(PLAYER) == 1:
        if bot_mode:
            # добавить имя бота с уровнем сложности
            PLAYER = (PLAYER[0], bot_mode)
        else:
            PLAYER = (PLAYER[0], input().lower())
    else:
        # для выбора символа поменять местами элементы кортежа
        pass

# здесь должны быть функции по обработке ввода режима игры, уровня сложности, символа...

# здесь должна(-ы) быть функция(-и) работы со статистикой игроков
