import random, copy
from django import template
register = template.Library()

icons = [
    'Airplane',
    'AirplayAudio',
    'App',
    'Battery',
    'Bluetooth',
    'Brightness',
    'DND',
    'Date',
    'Emoji',
    'File',
    'Flashlight',
    'GET',
    'GIF',
    'Image',
    'Input',
    'Language',
    'Location',
    'Make-PDF',
    'Note',
    'Notification',
    'Record',
    'Quicklook',
    'RSS',
    'Settings',
    'Skip-Forward',
    'Variable',
    'Web',
    'Play-Pause',
    'WiFi',
    'Math',
    'Mobile',
]

@register.filter(is_safe=True)
def shuffle_icons(iterations:int):
    icons = []
    for i in range(0,iterations):
        icons += shuffler()
    return icons

def shuffler():
    shuffled = copy.deepcopy(icons)
    shuffled = [f'assets/cat/{i}.svg' for i in icons]
    random.shuffle(shuffled)
    return shuffled