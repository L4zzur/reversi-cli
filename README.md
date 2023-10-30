# Реверси/Отелло

Реализация данной настольной игры на Python для командной строки.

Всё об игре и её правилах: [Реверси](https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D0%B2%D0%B5%D1%80%D1%81%D0%B8 "Википедия")

Реализация с веб-интерфейсом и мультиплеером: [Reversi Web](https://gitlab.com/SolinnenHub/flask/reversi-web)

# Установка:

###### Склонировать репозиторий:
```bash
$ git clone https://github.com/L4zzur/reversi_cli.git
```

###### Перейти в папку reversi-cli:
```bash
$ cd reversi-cli
```

###### Запустить основной файл игры с набором аргументов:
```bash
$ python main.py --color --random --sleep 1
```

Один из трёх аргументов (```human, random, test```) является обязательным.

Аргумент  | Значение
--------- | -------------------
--color   | Запуск в цветном режиме
--sleep   | Устанавливает таймаут ожидания после ходов, может быть вещественным (по умолчанию 0)
--human   | Игра против другого человека
--random  | Игра против бота-рандома
--test    | Игра двух ботов-рандомов
