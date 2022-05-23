#Основной файл программы, исполняемый модуль, модуль верхнего уровня
#Здесь не используем объявление функций




from players import *
from help import show_help, show_message

#Приветствие
show_message('КРЕСТИКИ-НОЛИКИ')

# чтение .ini файла
    # '-i' - запустить в интерактивном меню в edit configurations
#if read_ini():
#    show_help()


# запуск суперцикла
while True:
    command = input('_>')

    if command in ('quit', 'выход'):
        # обработка завершения работы приложения
        break
    elif command in ('new', 'yes', 'новая', 'да'):
        #есть ли текущий игрок
        if not PLAYER:
            #запрос имени игрока
            player_name()




    # ввод имени игрока
