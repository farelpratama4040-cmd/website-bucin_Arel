# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : 2583E
# Tugas Algoritma Pertemuan 7

# 1. PENGURUTAN SISIP (INSERTION SORT) 
def InsertionSort1(x, N):
    for i in range(1, N):
        y = x[i]
        j = i - 1
        ketemu = False
        while (j >= 0) and (not ketemu):
            if (y < x[j]):
                x[j+1] = x[j]
                j = j - 1
            else:
                ketemu = True
        x[j+1] = y


# 2. PENGURUTAN SHELL (SHELL SORT) 
def InsSort(x, N, Start, Step):
    i = Start + Step
    n = N - 1
    while (i <= n):
        y = x[i]
        j = i - Step
        ketemu = False
        while (j >= 0) and (not ketemu):
            if (y < x[j]):
                x[j+Step] = x[j]
                j = j - Step
            else:
                ketemu = True
        x[j+Step] = y
        i = i + Step

def ShellSort(x, N):
    n = N - 1
    Step = n
    while (Step > 1):
        Step = int((Step/3)) + 1
        # Menggunakan range(0, Step) agar sesuai dengan logika pembagian blok data
        for Start in range(0, Step): 
            InsSort(x, N, Start, Step)


# CONTOH CARA TESTING DI VS CODE 

# 1. Siapkan data acak yang mau diurutkan
data_angka = [89, 34, 25, 12, 22, 11, 90]
jumlah_elemen = len(data_angka)

print("Data awal (berantakan):", data_angka)

# 2. Pilih salah satu fungsi untuk mengurutkan (hilangkan tanda # untuk memilih)
# InsertionSort1(data_angka, jumlah_elemen)
ShellSort(data_angka, jumlah_elemen)

# 3. Cetak hasil
print("Data akhir (sudah urut):", data_angka)