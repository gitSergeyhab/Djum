from random import sample
from .data import skillist


def titles(request):
    return {
        'title': 'Джуманджи',
        'skillist': sample(skillist, 5),
    }
