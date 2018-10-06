country = input('What is your nationality? ')
age = input('What is your age? ')
age = int(age)

if country == 'Taiwan':
	if age >= 18:
		print('You could have licence test.')
	else:
		print('You could NOT have licence test.')
		