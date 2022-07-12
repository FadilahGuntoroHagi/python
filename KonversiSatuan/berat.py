from termcolor import colored
from misc import misc

'''
	Konversi berat (massa)
	- Kilogram
	- Gram
	- Miligram
'''
class berat:
	satuan = {
		"gram": 'g',
		"miligram": 'mg',
		"kilogram": 'kg',
	}

	# konversi dari kilogram
	def kilogram(berat):
		return {
			"gram": berat * (10 ** 3),
			"miligram": berat * (10 ** 6)
		}

	# konversi dari gram
	def gram(berat):
		return {
			"kilogram": berat / (10 ** 3),
			"miligram": berat * (10 ** 3)
		}

	# konversi dari miligram
	def miligram(berat):
		return {
			"kilogram": berat / (10 ** 6),
			"gram": berat / (10 ** 3)
		}

	# menu utama
	def menu():
		# tampilkan menu pilihan
		print("\nPilih satuan berat awal:")
		print("["+misc.col(1)+"] Kilogram (kg)")
		print("["+misc.col(2)+"] Gram (g)")
		print("["+misc.col(3)+"] Miligram (mg)")

		# mengambil nilai input
		data = misc.input("berat")

		if data["option"] == 1:
			output = berat.kilogram(data["value"])
		elif data["option"] == 2:
			output = berat.gram(data["value"])
		elif data["option"] == 3:
			output = berat.miligram(data["value"])
		else:
			print(colored("Pilihan tidak ditemukan!", 'red'))
			return

		# menampilkan hasil
		print(colored("\nOutput :", 'green'))
		# looping nilai dari dictionary output
		for nama, nilai in output.items():
			print("Satuan", nama, ":", nilai, berat.satuan[nama])
