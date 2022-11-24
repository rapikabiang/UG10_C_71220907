a=int(input("Masukkan Bulan (1-12): "))
if a==2:
    print("Jumlah Hari: 28")
if a<8:
    if a%2 == 1:
        print("Jumlah Hari: 31")
    else:
        print("Jumlah Hari: 30")
elif a>8:
    if a%2 == 1:
        print("Jumlah Hari: 30")
    else:
        print("Jumlah Hari: 31")
    
