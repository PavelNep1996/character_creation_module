from random import randint
from graphic_arts.start_game_banner import run_screensaver


# Значение стандартной атаки
DEFAULT_ATTACK = 5
# Значение стандартной защиты
DEFAULT_DEFENCE = 10
# Значение стандартной выновсливости
DEFAULT_STAMINA = 80


class Character:
    # Базовый титутл.
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    # Диапазон очков урона.
    RANGE_VALUE_ATTACK = (1, 3)
    # Диапазон очков защиты
    RANGE_VALUE_DEFENCE = (1, 5)
    # Значение очков урона.
    SPECIAL_BUFF = 15
    # Удача.
    SPECIAL_SKILL = 'Удача'

    # Объявляем конструктор класса.
    def __init__(self, name):
        self.name = name

    # Объявляем метод атаки.
    def attack(self) -> str:
        # Описываем метод атаки.
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    # Объявляем метод защиты.
    def defence(self):
        # Описываем метод защиты.
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона')

    # Объявляем метод специального умения.
    def special(self):
        # Описываем метод специального умения.
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    # Описание классов
    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    # Добавили словарь, в котором соотносится ввод пользователя и класс
    # персонажа.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    approve_choice: str = None

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    # Замените конструкцию условных операторов на словарь.
    print(character)
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')

    cmd = None
    commands = {
        'attack': character.attack,
        'defence': character.defence,
        'special': character.special
    }

    while cmd != 'skip':
        cmd = input('Введи команду: ')
        # Вместо блока условных операторов добавьте условие
        # принадлежности введённой команды словарю.
        # В функции print() будет вызываться метод класса,
        # который соответствует введённой команде.
        if cmd in commands.keys():
            print(commands[cmd]())
    return 'Тренировка окончена.'


if __name__ == '__main__':
    """Главная функция.
    Она запускает игру, и из неё вызываются
    все вспомогательные функции.
    """
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class(char_name)
    print(start_training(char_class))


# def attack(char_name: str, char_class: str) -> str:
#     """Генерирует количество очков атаки.
#     В зависимости от выбранного типа персонажа и
#     возвращает строковое сообщение о проведённой атаке.
#     """
#     if char_class == 'warrior':
#         return (f'{char_name} нанёс урон '
#                 f'противнику равный {5 + randint(3, 5)}')
#     if char_class == 'mage':
#         return (f'{char_name} нанёс урон '
#                 f'противнику равный {5 + randint(5, 10)}')
#     if char_class == 'healer':
#         return (f'{char_name} нанёс урон '
#                 f'противнику равный {5 + randint(-3, -1)}')
#     return (f'{char_name} не нанёс урон')


# def defence(char_name: str, char_class: str) -> str:
#     """Генерирует количество очков защиты.
#     В зависимости от выбранного типа персонажа и возвращает строковое
#     сообщение о выполненном блокировании атаки.
#     """
#     if char_class == 'warrior':
#         return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
#     if char_class == 'mage':
#         return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
#     if char_class == 'healer':
#         return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
#     return (f'{char_name} не блокировал урон')


# def special(char_name: str, char_class: str) -> str:
#     """Генерирует количество очков специального умения.
#     В зависимости от выбранного типа персонажа и возвращает строковое
#     сообщение о выполненном применении специального умения.
#     """
#     if char_class == 'warrior':
#         return (f'{char_name} применил специальное '
#                 f'умение «Выносливость {80 + 25}»')
#     if char_class == 'mage':
#         return (f'{char_name} применил специальное умение «Атака {5 + 40}»')
#     if char_class == 'healer':
#         return (f'{char_name} применил '
#                 f'специальное умение «Защита {10 + 30}»')
#     return (f'{char_name} не применил специальное умение')


# def start_training(char_name: str, char_class: str) -> str:
#     """Запускает цикл тренировки навыков персонажа.
#     В качестве параметров она получает введённое игроком имя персонажа
#     и выбранный тип персонажа.
#     """
#     if char_class == 'warrior':
#         print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
#     if char_class == 'mage':
#         print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
#     if char_class == 'healer':
#         print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
#     print('Потренируйся управлять своими навыками.')
#     print('Введи одну из команд: attack — чтобы атаковать противника, '
#           'defence — чтобы блокировать атаку противника или '
#           'special — чтобы использовать свою суперсилу.')
#     print('Если не хочешь тренироваться, введи команду skip.')
#     cmd: str = None
#     while cmd != 'skip':
#         cmd = input('Введи команду: ')
#         if cmd == 'attack':
#             print(attack(char_name, char_class))
#         if cmd == 'defence':
#             print(defence(char_name, char_class))
#         if cmd == 'special':
#             print(special(char_name, char_class))
#     return 'Тренировка окончена.'


# def choice_char_class() -> str:
#     """Функция выбора класса персонажа."""
#     approve_choice: str = None
#     char_class: str = None
#     while approve_choice != 'y':
#         char_class = input('Введи название персонажа, '
#                            'за которого хочешь играть: Воитель — warrior, '
#                            'Маг — mage, Лекарь — healer: ')
#         if char_class == 'warrior':
#             print('Воитель — дерзкий воин ближнего боя. '
#                   'Сильный, выносливый и отважный.')
#         if char_class == 'mage':
#             print('Маг — находчивый воин дальнего боя. '
#                   'Обладает высоким интеллектом.')
#         if char_class == 'healer':
#             print('Лекарь — могущественный заклинатель. '
#                   'Черпает силы из природы, веры и духов.')
#         approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
#                                'или любую другую кнопку, чтобы выбрать '
#                                'другого персонажа ').lower()
#     return char_class


# if __name__ == '__main__':
#     """Главная функция.
#     Она запускает игру, и из неё вызываются
#     все вспомогательные функции.
#     """
#     run_screensaver()
#     print('Приветствую тебя, искатель приключений!')
#     print('Прежде чем начать игру...')
#     char_name: str = input('...назови себя: ')
#     print(f'Здравствуй, {char_name}! '
#           'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
#     print('Ты можешь выбрать один из трёх путей силы:')
#     print('Воитель, Маг, Лекарь')
#     char_class: str = choice_char_class()
#     print(start_training(char_name, char_class))
# char_class = {
    #     'warrior': ', ты Воитель — великий мастер ближнего боя.',
    #     'mage': ', ты Маг — превосходный укротитель стихий.',
    #     'healer': ', ты Лекарь — чародей, способный исцелять раны.'}
