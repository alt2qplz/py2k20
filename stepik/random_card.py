import random

def random_card():
	cards = {'ACE':'11', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', 
			'8':'8', '9':'9', 'TEN':'10', 'JACK':'10', 'QUEEN':'10', 'KING':'10'}
	
	x = random.choice(list(cards.keys()))

	print(x)

	return(cards.get(x))

x = random_card()
y = random_card()
z = int(x) + int(y)

if z == 21:
	print(str(z) + '\n' + 'Поздравляю, это блек джек')
else:
	print('\n' + f'{z}' + '\n' + 'Может ещё одну карту? да/нет'+ '\n')

	while str(input()) == 'да':
		r = random_card()
		z = z + int(r)

		if z < 21:
			print('\n' + str(z) + '\n' + 'Может ещё одну карту? да/нет')
		elif z == 21:
			print(str(z) + '\n' + 'Поздравляю, это блек джек')
			break
		else:
			print(str(z) + '\n' + 'Бро, это перебор')
			break
	else:
		print('Твой счет равен ' + (str(z)))


