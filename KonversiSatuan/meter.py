from termcolor import colored
from misc import misc



'''
	Konversi satuan meter (distance)
	- Meter
	- Kilometer
	- Centimeter
	- Milimeter
'''
class meter:
	satuan = {
		"milimeter": "mm",
		"centimeter": "cm",
		"meter": "m",
		"kilometer": "km",
	}

	# konversi dari meter
	def meter(value):
		return {
			"kilometer": value / (10 ** 3),
			"centimeter": value * (10 ** 2),
			"milimeter": value * (10 ** 3)
		}

	# konversi dari kilometer
	def kilometer(value):
		return {
			"meter": value * (10 ** 3),
			"centimeter": value * (10 ** 5),
			"milimeter": value * (10 ** 6)
		}

	# konversi dari centimeter
	def centimeter(value):
		return {
			"kilometer": value / (10 ** 5),
			"meter": value / (10 ** 2),
			"milimeter": value * 10
		}

	# konversi dari milimeter
	def milimeter(value):
		return {
			"kilometer": value / (10 ** 6),
			"meter": value / (10 ** 3),
			"centimeter": value / 10
		}

	# menu utama
	def menu():
		# tampilkan menu pilihan
		print("\nPilih satuan meter awal:")
		print("["+misc.col(1)+"] Meter (m)")
		print("["+misc.col(2)+"] Kilometer (km)")
		print("["+misc.col(3)+"] Centimeter (cm)")
		print("["+misc.col(4)+"] Milimeter (mm)")

		# mengambil nilai inputan
		data = misc.input("meter")

		if data["option"] == 1:
			output = meter.meter(data["value"])
		elif data["option"] == 2:
			output = meter.kilometer(data["value"])
		elif data["option"] == 3:
			output = meter.centimeter(data["value"])
		elif data["option"] == 4:
			output = meter.milimeter(data["value"])
		else:
			print(colored("Pilihan tidak ditemukan!", 'red'))
			return

		# tampilkan hasil output
		print(colored("\nOutput :", 'green'))
		# looping nilai dari dictionary output
		for nama, nilai in output.items():
			print("Satuan", nama, ":", nilai, meter.satuan[nama])