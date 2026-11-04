# Program python untuk menghitung upah karyawan 
# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E
# Menentukan upah mingguan seorang karyawan. Masukan yang dibaca dari papan kunci adalah nama karyawan, golongan, dan jumlah jam kerja.
# Keluaran program adalah nama karyawan dan upahnya.

# DEKLARASI
JamNormal = 48          # jumlah jam kerja normal per minggu
UpahPerJam = 2000      # upah per jam, Rp 2000
UpahLembur = 3000      # upah per jam lembur, Rp 3000

# tipe data:
# nama : string (nama karyawan)
# JJK : integer (Jumlah Jam Kerja)
# lembur : real (jumlah jam lembur)
# upah : real (upah karyawan)
# jawab : char (jawaban untuk ulang)

# ALGORITMA
while True:
    # Read input
    nama = input("Masukkan nama karyawan: ")
    JJK = int(input("Masukkan jumlah jam kerja: "))

    # Proses perhitungan upah
    if JJK <= JamNormal:
        upah = JJK * UpahPerJam
    else:
        lembur = JJK - JamNormal
        upah = JamNormal * UpahPerJam + lembur * UpahLembur

    # Output hasil
    print(f"Nama: {nama}")
    print(f"Upah: Rp {upah}")

    # tanyakan apakah ulangi
    jawab = input("Ulangi untuk karyawan yang lain? (y/t): ").lower()
   
   # (jawab = 't')
    if jawab == 't':
        break # Keluar dari perulangan jika jawaban adalah 't'

print("Program Selesai.")