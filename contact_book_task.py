
import shelve
db = shelve.open('contact_book')
while True:
	choice = int(input('1. Add new contact \n 2. Search contact \n 3. Display the contact book \n 4. Edit contact \n 5. Delete contact \n Chose the command number '))
	if choice == 1:
		new_name = input('Write full name ')
		info = [{'phone number': input('Write phone number '), 'address': input('Write address ')}]
		db[new_name] = info
	elif choice == 2:
		search_name = input('Write the contact full name ')
		if search_name in db:
			print(db[search_name])
		else:
		    print('Contact is not found')
	elif choice == 3:
		if not db:
			print('Empty book')
		print(list(db))
	elif choice == 4:
		edit_name = input('Write the contact full name ')
		info = [{'phone number': input('Write phone number '), 'address': input('Write address ')}]
		db[edit_name] = info
	else:
		del_name = input('Write the contact full name ')
		del db[del_name]


