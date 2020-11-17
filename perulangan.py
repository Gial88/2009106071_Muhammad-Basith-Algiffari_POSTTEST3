print("Perulangan Menggunakan While")
stop = False
while (not stop):
	print("="*50)
	n = int(input("Masukkan nilai N : "))
	i = 0
	while (i <= n):
	    if 10 ** i <= n:
	    	a = i
	    else:
	    	break
	    i += 1
	print("Nilai terkecil dari 10^x > n adalah 10^"+str(i) , "atau", 10 ** i)
	pil = input("Coba Lagi ? (ya/tidak) ")
	if pil =="tidak":
		stop = True
print("==========Terima Kasih===========")