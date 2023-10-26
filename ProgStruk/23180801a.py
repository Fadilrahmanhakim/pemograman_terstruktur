# konversi tipe data secara eksplisit atau (manual)
nilai_string = "678" 
nilai_integer = 678

print("Tipe data dari variabel nilai_string sebelum Type Casting:", type(nilai_string))

# proses konversi tipe data eksplisit
nilai_string = int(nilai_string)

#menampilkan nilai dan tipe data yang dihasilakan
print("Tipe data dari variabel nilai_string sebelum Type Casting:", type(nilai_string))

nilai_jlh = nilai_integer + nilai_string

print("hasil penjumlahan: ", nilai_jlh)
print("Tipe data dari nilai_jlh", type(nilai_jlh))
