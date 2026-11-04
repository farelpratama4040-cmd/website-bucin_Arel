import csv
import os

# Variabel Global (State Management)
data_absensi = []
status_data_terurut = False # Sentinella pelindung Binary Search

def baca_csv(filepath):
    """Membaca file CSV dan mengubahnya menjadi List of Dictionaries."""
    data = []
    try:
        # Menggunakan DictReader untuk mengikat baris pertama sebagai kunci
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(dict(row))
        print(f"Berhasil memuat {len(data)} data dari {filepath}.")
        return data
    except FileNotFoundError:
        print(f"Error: File {filepath} tidak ditemukan. Pastikan file ada di folder yang sama.")
        return []

def tampilkan_data(data):
    """Menampilkan data dalam format tabel sederhana."""
    if len(data) == 0:
        print("Data masih kosong.")
        return
    
    print("-" * 45)
    print(f"{'NIM':<10} | {'NAMA':<20} | {'KODE MK':<10}")
    print("-" * 45)
    for record in data:
        print(f"{record['nim']:<10} | {record['nama']:<20} | {record['kode_mk']:<10}")
    print("-" * 45)

def bubble_sort(data):
    """Mengurutkan data berdasarkan NIM dengan Bubble Sort (Ascending)."""
    n = len(data)
    # Optimasi: Gunakan boolean swapped untuk berhenti jika sudah terurut
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if data[j]['nim'] > data[j + 1]['nim']:
                # Pertukaran referensi alamat memori Python
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        
        # Jika tidak ada yang ditukar dalam 1 pass, iterasi dihentikan
        if not swapped:
            break
    print("\nData berhasil diurutkan menggunakan Bubble Sort.")

def selection_sort(data):
    """Mengurutkan data berdasarkan NIM dengan Selection Sort (Ascending)."""
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if data[j]['nim'] < data[min_index]['nim']:
                min_index = j
        
        # Penukaran nilai elemen ekstrem
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
            
    print("\nData berhasil diurutkan menggunakan Selection Sort.")

def sequential_search(data, target_nim):
    """Pencarian Linear yang menangani hasil ganda."""
    matched_records = []
    for index, record in enumerate(data):
        if record['nim'] == target_nim:
            matched_records.append(record)
    return matched_records

def binary_search(data, target_nim):
    """Pencarian Membelah Dua yang menangani hasil ganda via ekspansi linier."""
    matched_records = []
    bottom = 0
    top = len(data) - 1
    
    while bottom <= top:
        middle = (bottom + top) // 2
        current_val = data[middle]['nim']
        
        if current_val == target_nim:
            # Ditemukan! Mulai ekspansi untuk mencari duplikat di sekitar index 'middle'
            matched_records.append(data[middle])
            
            # Ekspansi ke kiri (mundur)
            for i in range(middle - 1, -1, -1):
                if data[i]['nim'] == target_nim:
                    matched_records.append(data[i])
                else:
                    break
                    
            # Ekspansi ke kanan (maju)
            for i in range(middle + 1, len(data)):
                if data[i]['nim'] == target_nim:
                    matched_records.append(data[i])
                else:
                    break
                    
            break # Hentikan Binary Search utama karena ekspansi sudah selesai
            
        elif target_nim < current_val:
            top = middle - 1
        else:
            bottom = middle + 1
            
    return matched_records

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    global data_absensi, status_data_terurut
    
    while True:
        print("\n=== PROGRAM MANAJEMEN ABSENSI MAHASISWA ===")
        print("1. Muat Data dari CSV")
        print("2. Tampilkan Data Saat Ini")
        print("3. Urutkan Data (Bubble Sort)")
        print("4. Urutkan Data (Selection Sort)")
        print("5. Cari Mahasiswa (Sequential Search)")
        print("6. Cari Mahasiswa (Binary Search)")
        print("7. Keluar")
        print("===========================================")
        
        pilihan = input("Pilih menu (1-7): ")
        
        if pilihan == '1':
            data_absensi = baca_csv('data_absen.csv')
            status_data_terurut = False # Reset status jika data baru dimuat
            
        elif pilihan == '2':
            tampilkan_data(data_absensi)
            
        elif pilihan == '3':
            if not data_absensi:
                print("Error: Muat data terlebih dahulu (Menu 1).")
            else:
                bubble_sort(data_absensi)
                status_data_terurut = True
                
        elif pilihan == '4':
            if not data_absensi:
                print("Error: Muat data terlebih dahulu (Menu 1).")
            else:
                selection_sort(data_absensi)
                status_data_terurut = True
                
        elif pilihan == '5':
            if not data_absensi:
                print("Error: Muat data terlebih dahulu (Menu 1).")
            else:
                target = input("Masukkan NIM yang dicari: ")
                hasil = sequential_search(data_absensi, target)
                if hasil:
                    print(f"\nDitemukan {len(hasil)} rekaman untuk NIM {target}:")
                    tampilkan_data(hasil)
                else:
                    print(f"\nNIM {target} tidak ditemukan.")
                    
        elif pilihan == '6':
            if not data_absensi:
                print("Error: Muat data terlebih dahulu (Menu 1).")
            elif not status_data_terurut:
                # Proteksi pencegahan gagal komputasi dari unsorted data
                print("Peringatan: Data belum diurutkan! Binary Search mensyaratkan data terurut.")
                print("Silakan gunakan Menu 3 atau 4 terlebih dahulu.")
            else:
                target = input("Masukkan NIM yang dicari: ")
                hasil = binary_search(data_absensi, target)
                if hasil:
                    print(f"\nDitemukan {len(hasil)} rekaman untuk NIM {target}:")
                    tampilkan_data(hasil)
                else:
                    print(f"\nNIM {target} tidak ditemukan.")
                    
        elif pilihan == '7':
            print("Keluar dari program. Terima kasih!")
            break
            
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()