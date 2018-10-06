country = input('What is your nationality? ')

if country == 'Taiwan':
	age = input('What is your age? ')
	if int(age) >= 18:
		print('You could have licence test.')
	else:
		print('You could NOT have licence test.')
elif country == 'US':
	age = input('What is your age? ')
	if int(age) >= 16:
		print('You could have licence test.')
	else:
		print('You could NOT have licence test.')
else:
	print('You should only fill in your nationality as Taiwan or US.')
