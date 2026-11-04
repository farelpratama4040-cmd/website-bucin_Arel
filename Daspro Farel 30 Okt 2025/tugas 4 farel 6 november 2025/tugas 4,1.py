# Program Hitung Rata-rata
# NAMA : Farel Ilyasa Habi Pratama
# KELAS : E
# NIM : 25041450138

print("=== PROGRAM HITUNG RATA-RATA ===")

try:
    # Meminta jumlah data
    n = int(input("Masukkan jumlah angka yang ingin dihitung: "))

    # Menyimpan angka-angka yang dimasukkan
    angka = []
    for i in range(n):
        nilai = float(input(f"Masukkan angka ke-{i+1}: "))
        angka.append(nilai)

    # Menghitung rata-rata
    rata_rata = sum(angka) / n

    # Menampilkan hasil
    print("\nAngka yang dimasukkan:", angka)
    print(f"Rata-rata dari angka tersebut adalah: {rata_rata:.2f}")

except ValueError:
    print("Input tidak valid! Harap masukkan angka yang benar.")
