current_users = ['adel', 'sanya' , 'kostya', 'anna', 'nail']

new_users = ['adel', 'VLAD', 'Timur', 'ANNA']

for new_user in new_users:
	if new_user.lower() in current_users:
		print(f'{new_user} net idi nahui, ti uje est tut\n')
	if new_user.lower() not in current_users:
		current_users.append(new_user.lower())
		print(f'{new_user}, ti prinyat\n')

print('a ti kto takoi? \n')

new_user = str(input())

if new_user.lower() in current_users:
	print(f'{new_user} net idi nahui, ti uje est tut\n')
if new_user.lower() not in current_users:
		current_users.append(new_user.lower())
		print(f'{new_user}, ti prinyat\n')

print(current_users)