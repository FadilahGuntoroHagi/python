
'''
	Konversi suhu dalam satuan internasional
	- Celcius
	- Reamur
	- Fahrenheit
	- Kelvin
'''
class suhu:
	satuan = {
		"celcius": "C",
		"fahrenheit": "F",
		"reamur": "R",
		"kelvin": "K"
	}

	# konversi dari celcius
	def celcius(tempratur):
		reamur = (4/5) * tempratur
		fahrenheit = (9/5) * tempratur + 32
		kelvin = tempratur + 273

		return {
			"reamur": reamur,
			"fahrenheit": fahrenheit,
			"kelvin": kelvin
		}

	# konversi dari reamur
	def reamur(tempratur):
		celcius = (5/4) * tempratur
		fahrenheit = (9/4) * tempratur + 32
		kelvin = celcius + 273

		return {
			"celcius": celcius,
			"fahrenheit": fahrenheit,
			"kelvin": kelvin
		}

	# konversi dari kelvin
	def kelvin(tempratur):
		celcius = tempratur - 273
		reamur = (4/5) * celcius
		fahrenheit = (9/5) * celcius + 32

		return {
			"celcius": celcius,
			"reamur": reamur,
			"fahrenheit": fahrenheit
		}

	# konversi dari fahrenheit
	def fahrenheit(tempratur):
		reamur = (4/9) * (tempratur - 32)
		celcius = (5/9) * (tempratur - 32)
		kelvin = (5/9) * (tempratur - 32) + 273

		return {
			"reamur": reamur,
			"celcius": celcius,
			"kelvin": kelvin
		}

	# menu utama
	def menu():
		# tampilkan menu pilihan
		print("\nPilih satuan suhu awal:")
		print("["+misc.col(1)+"] Celcius (C)")
		print("["+misc.col(2)+"] Reamur (R)")
		print("["+misc.col(3)+"] Fahrenheit (F)")
		print("["+misc.col(4)+"] Kelvin (K)")

		# input satuan suhu dan tempratur
		data = misc.input("tempratur")

		# cek satuan yang dipilih
		if data["option"] == 1:
			output = suhu.celcius(data["value"])
		elif data["option"] == 2:
			output = suhu.reamur(data["value"])
		elif data["option"] == 3:
			output = suhu.fahrenheit(data["value"])
		elif data["option"] == 4:
			output = suhu.kelvin(data["value"])
		else:
			print(colored("Pilihan tidak ditemukan!", 'red'))
			return

		# tampilkan semua hasil
		print(colored("\nOutput :", 'green'))
		# looping nilai dari dictionary output
		for nama, nilai in output.items():
			print("Satuan", nama, ":",  nilai, u"\N{DEGREE SIGN}", '\b'+suhu.satuan[nama])
