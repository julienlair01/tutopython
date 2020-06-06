# -*- coding: utf8 -*-
import random
import json

def read_values_from_json(file,key):
	values = []
	with open(file) as f:
		data = json.load(f)
		for entry in data:
			values.append(entry[key])
	return values

def get_random_character():
	all_values = read_values_from_json("characters.json","character")
	return get_random_item(all_values)


def get_random_quote():
	all_values = read_values_from_json("quotes.json","quote")
	return get_random_item(all_values).strip()


def get_random_item(my_list):
	rand_numb = random.randint(0,len(my_list) - 1)
	item = my_list[rand_numb]
	return item


def message(character,quote):	
	n_character = character.capitalize()
	n_quote = quote.capitalize()
	return "{} a dit : {}".format(n_character,n_quote)


# Programm
user_answer = input(' ---------------------------------------------------------------------------- \n'
    				'Tapez entrée pour connaître une autre citation ou B pour quitter le programme.\n')

while user_answer != "B":
    print(message(get_random_character(), get_random_quote()))
    user_answer = input(' ---------------------------------------------------------------------------- \n'
    					'Tapez entrée pour connaître une autre citation ou B pour quitter le programme.\n')