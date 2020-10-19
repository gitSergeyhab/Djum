from random import choice, shuffle
from .data import skillist


def skill_maker(x):
    shuffle(skillist)
    number_skills = list(range(x - 1, x + 1))
    return ' • '.join(skillist[:choice(number_skills)])


def user_maker(x):
    return f'username{x}', f'email{x}@mail.fake', f'{x}word'

