# Program Cari Nilai Minimum
# NAMA : Farel Ilyasa Habi Pratama
# KELAS : E
# NIM : 25041450138

print("=== PROGRAM CARI NILAI MINIMUM ===")

try:
    # Meminta jumlah data
    n = int(input("Masukkan jumlah angka: "))

    # Menyimpan angka-angka yang dimasukkan
    angka = []
    for i in range(n):
        nilai = float(input(f"Masukkan angka ke-{i+1}: "))
        angka.append(nilai)

    # Mencari nilai minimum
    nilai_minimum = min(angka)

    # Menampilkan hasil
    print("\nAngka yang dimasukkan:", angka)
    print(f"Nilai terkecil adalah: {nilai_minimum}")

except ValueError:
    print("Input tidak valid! Harap masukkan angka yang benar.")
