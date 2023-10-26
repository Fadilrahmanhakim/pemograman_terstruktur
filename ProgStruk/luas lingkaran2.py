# Program menghitung luas lingkaran

import konstanta # Memanggil file tempat kosntanta diletakkan

print("Program menghitung Luas Lingkaran \n")

# Memasukan nilai Variabel jari-jari
# Dengan meminta kepada user unutk memasukan
jari = int(input("Masukan Nilai Jari-Jari : "))

Luas = (konstanta.PHI) * jari * jari # Menghitung luas lingkaran

# menampilkan hasil perhitungan luas lingkaran
print("Luas Lingkaran Adalah = {} dari nilai phi {} ".format(Luas, konstanta.PHI), end= "")
print("jari-jari ", jari)