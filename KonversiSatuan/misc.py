from termcolor import colored

class misc:
	def input(text):
		check = True

		while check:
			try:
				option = int(input(colored("\n>> ", 'cyan')))
				value = float(input("Masukkan "+text+": "))
				check = False
			except Exception as e:
				# jika bukan angka tampilkan pesan
				if 'invalid literal for int()' in str(e):
					print('Masukkan angka!')
				else:
					# tampilkan pesan error lain
					print(e)
		
		return {
			"option": option,
			"value": value
		}
	
	def col(a):
		return colored(str(a), "yellow")