import csv
import random

# Kumpulan nama acak buat dikombinasikan
nama_depan = ['Andi', 'Budi', 'Citra', 'Dewi', 'Eka', 'Farel', 'Gita', 'Hadi', 'Iwan', 'Joko', 'Rina', 'Siti', 'Tono', 'Yudi', 'Zaki', 'Ayu', 'Rizky', 'Putra', 'Nadia', 'Maya']
nama_belakang = ['Pratama', 'Saputra', 'Wijaya', 'Lestari', 'Nugroho', 'Setiawan', 'Hidayat', 'Siregar', 'Kusuma', 'Pangestu', 'Sari', 'Indah', 'Maulana', 'Rahman', 'Fauzi']

# Generate 3000 mahasiswa baru tahun ajaran 2026
with open('data_mahasiswa.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['NIM', 'Nama', 'Kode MK', 'IPK', 'Tahun Angkatan'])
    for _ in range(3000):
        nim = f"2602{random.randint(10000, 99999)}"  # 26 = tahun 2026
        nama = f"{random.choice(nama_depan)} {random.choice(nama_belakang)}"
        kode_mk = f"MK{random.randint(100, 999)}"
        ipk = round(random.uniform(2.00, 4.00), 2)
        tahun_angkatan = 2026
        writer.writerow([nim, nama, kode_mk, ipk, tahun_angkatan])
print("File data_mahasiswa.csv berhasil dibuat dengan 3000 mahasiswa baru tahun ajaran 2026!")