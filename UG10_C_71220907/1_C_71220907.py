print("========== Pilih Menu ==========")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
e = int(input("Masukkan angka pertama: "))
f = int(input("Masukkan angka kedua: "))
l = int(input("Pilihan anda: "))
if l == 1:
    n=(e+f)
elif l == 2:
    n=(e-f)
elif l == 3:
    n=(e*f)
elif l == 4:
    n=(e%f)
print("Hasil:",n)

