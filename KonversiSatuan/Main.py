

'''
	Program pengkonversi
	Suhu, berat & jarak
'''

print("+-----------------------------+")
print("|   PROGRAM PENGKONVERSI    |")
print("+-----------------------------+")

ulangi = True

# ulangi program selama diperlukan
while ulangi:
	print("")
	print("Pilih menu:")
	print("["+misc.col(1)+"] Konversi suhu")
	print("["+misc.col(2)+"] Konversi berat")
	print("["+misc.col(3)+"] Konversi meter")
	print("["+misc.col(0)+"] Keluar")
	print("")

	check = True
	# ulangi selama inputan tidak sesuai
	while check:
		try:
			pilihan = int(input(colored(">> ", 'cyan')))
			# cek pilihan menu
			if pilihan == 1:
				suhu.menu()
				check = False
			elif pilihan == 2:
				berat.menu()
				check = False
			elif pilihan == 3:
				meter.menu()
				check = False
			elif pilihan == 0:
				print(colored("Sampai jumpa..", 'magenta'))
				exit()
			else:
				print(misc.col("Pilihan menu tidak ditemukan!"))
		except Exception as e:
			# jika bukan angka tampilkan pesan
			if 'invalid literal for int()' in str(e):
				print(misc.col('Masukkan angka!'))
			else:
				# tampilkan pesan error lain
				print(e)

	# konfirmasi jika ingin mengulangi program
	answer = str(input("\nUlangi program? (y/t): "))

	if answer[0] == "y":
		ulangi = True
	else:
		ulangi = False
		print(colored("Sampai jumpa..", 'magenta'))


