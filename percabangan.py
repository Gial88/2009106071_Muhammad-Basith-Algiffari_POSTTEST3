print("Menu Takoyaki")
print("="*50)
print("Varian 1 = Rp.2000/pcs")
print("Varian 2 = Rp.2500/pcs")
stop = False
while (not stop):
	print("="*50)
	pil = int(input("Pilih Varian Takoyaki (1/2) : "))
	if (pil==1):
		beli = int(input("Berapa Banyak yang ingin di beli : "))
		if beli <= 45:
			if beli >= 10:
				harga = 2000
				potongan = int(beli * harga * 0.1)
				bayar = beli * harga - potongan 
				print("Total bayar : Rp."+str(bayar))
			else : 
				harga = 2000
				bayar = beli * harga 
				print("Total bayar : Rp."+str(bayar))
		else : 
			print("Takoyakinya Tidak Cukup")
	else :
		beli = int(input("Berapa Banyak yang ingin di beli : "))
		if beli <= 40:
			if beli >= 8:
				harga = 2500
				potongan = int(beli * harga * 0.08)
				bayar = beli * harga - potongan  
				print("Total bayar : Rp."+str(bayar))
			else : 
				harga = 2500
				bayar = beli * harga 
				print("Total bayar : Rp."+str(bayar))
		else : 
			print("Takoyakinya Tidak Cukup")
	coba = input("Mau Coba Lagi ? (ya/tidak) ")
	if coba == "tidak":
		stop = True
print("=========Terima Kasih==========")