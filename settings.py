WIDTH, HEIGHT = 8, 8            # длины сторон
NORTH = -WIDTH                  # север
NORTHEAST = -WIDTH + 1          # северо-запад
EAST = 1                        # запад
SOUTHEAST = WIDTH + 1           # юго-запад
SOUTH = WIDTH                   # юг
SOUTHWEST = WIDTH - 1           # юго-восток
WEST = - 1                      # восток
NORTHWEST = -WIDTH - 1          # северо-восток

DIRECTIONS = (
    NORTH, NORTHEAST,
    EAST, SOUTHEAST,
    SOUTH, SOUTHWEST,
    WEST, NORTHWEST
    )

COLORS = {
    'B': 'Черные',
    'W': 'Белые'
}


class PieceType():              # типы полей
    '''Класс всех возможных состояний полей на доске'''
    BOARD = '·'                     # пустое
    BLACK = 'B'                     # черная фишка
    WHITE = 'W'                     # белая фишка
    MOVE = '×'                      # вариант хода


class NoMoves(Exception):
    pass


class WrongMove(Exception):
    pass


def chunks(lst, n):                     # разбиение массива по чанкам
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def out_of_bounds(piece, direction):    # проверка на возможный выход за пределы поля
    '''Проверка, касается ли текущее поле границы в заданном направлении'''
    piece_top = 0 <= piece <= 7             # верхняя граница (индексы от 0 до 7)
    piece_bot = 56 <= piece <= 63           # нижняя граница (индексы от 56 до 63)
    piece_right = piece % WIDTH == 7        # правая граница (индексы, дающие 7 по модулю WIDTH)
    piece_left = piece % WIDTH == 0         # левая граница (индексы, дающие 0 по модулю WIDTH)
    return (direction in (NORTH, NORTHEAST, NORTHWEST) and piece_top) or \
           (direction in (SOUTH, SOUTHWEST, SOUTHEAST) and piece_bot) or \
           (direction in (EAST, NORTHEAST, SOUTHEAST) and piece_right) or \
           (direction in (WEST, NORTHWEST, SOUTHWEST) and piece_left)


def get_color(fg=None, bg=None):
    color = ''
    if fg:
        color += f'\x1b[38;2;{fg}m'
    if bg:
        color += f'\x1b[48;2;{bg}m'
    return color


def reset_color():
    return '\x1b[0m'


def color_string(str, fg=None, bg=None):
    return get_color(fg, bg) + str + reset_color()
