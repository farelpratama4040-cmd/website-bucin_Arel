# Program untuk menentukan apakah sebuah tahun adalah tahun kabisat atau bukan 
# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E

# Input
tahun = int(input("Masukkan tahun masehi: "))

# Proses dan Output
if tahun % 4 == 0:
    print(tahun, "adalah tahun kabisat")
else:
    print(tahun, "bukan tahun kabisat")