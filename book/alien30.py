aliens = []

for alien in range(30):
	alien = {'color':'red', 'points':'10'}
	aliens.append(alien)

for a in aliens[0:3]:
	print(a)

print()

for alien in aliens[:3]:
	if alien['color'] == 'red':
		alien['color'] = 'blue'

for alien in aliens [:5]:
	print(alien)

print(len(aliens))