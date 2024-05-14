import pygame
from os.path import join 
from os import walk

WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720 

COLORS = {
    'black': '#000000',
    'red': '#ee1a0f',
    'gray': 'gray',
    'white': '#ffffff',
}

MONSTER_DATA = {
	'Plumette':    {'element': 'plant', 'health': 90},
	'Ivieron':     {'element': 'plant', 'health': 140},
	'Pluma':       {'element': 'plant', 'health': 160},
	'Sparchu':     {'element': 'fire',  'health': 70},
	'Cindrill':    {'element': 'fire',  'health': 100},
	'Charmadillo': {'element': 'fire',  'health': 120},
	'Finsta':      {'element': 'water', 'health': 50},
	'Gulfin':      {'element': 'water', 'health': 80},
	'Finiette':    {'element': 'water', 'health': 100},
	'Atrox':       {'element': 'fire',  'health': 50},
	'Pouch':       {'element': 'plant', 'health': 80},
	'Draem':       {'element': 'plant', 'health': 110},
	'Larvea':      {'element': 'plant', 'health': 40},
	'Cleaf':       {'element': 'plant', 'health': 90},
	'Jacana':      {'element': 'fire',  'health': 60},
	'Friolera':    {'element': 'water', 'health': 70},
}

ABILITIES_DATA = {
	'scratch': {'damage': 20,  'element': 'normal', 'animation': 'scratch'},
	'spark':   {'damage': 35,  'element': 'fire',   'animation': 'fire'},
	'nuke':    {'damage': 50,  'element': 'fire',   'animation': 'explosion'},
	'splash':  {'damage': 30,  'element': 'water',  'animation': 'splash'},
	'shards':  {'damage': 50,  'element': 'water',  'animation': 'ice'},
    'spiral':  {'damage': 40,  'element': 'plant',  'animation': 'green'}
}

ELEMENT_DATA = {
    'fire':   {'water': 0.5, 'plant': 2,   'fire': 1,   'normal': 1},
    'water':  {'water': 1,   'plant': 0.5, 'fire': 2,   'normal': 1},
    'plant':  {'water': 2,   'plant': 1,   'fire': 0.5, 'normal': 1},
    'normal': {'water': 1,   'plant': 1,   'fire': 1,   'normal': 1},
}