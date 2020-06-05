# -*- coding: utf8 -*-
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]


# get a random quote from the specified list and return it

def get_random_quote(my_list):
	item = my_list[0]
	return item

user_answer = ""

while user_answer != "B":
	print(get_random_quote(quotes))
	user_answer = input("Appuyez sur Entrée pour voir une autre citation ou sur B pour quitter.")