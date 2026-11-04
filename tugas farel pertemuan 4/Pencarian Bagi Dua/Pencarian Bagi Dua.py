# Fungsi Pencarian Bagi Dua (Binary Search)
# Nama: Farel Ilyasa Habi Pratama
# Kelas: 2583E
# NIM: 25041450138


def binarySearch(L, n, X):
   
    # ALGORITMA
    i = 0              # ujung kiri larik
    j = n - 1          # ujung kanan larik
    ketemu = False     # asumsi X belum ditemukan

    while (not ketemu) and (i <= j):
        k = (i + j) // 2   # bagi dua larik

        if L[k] == X:
            ketemu = True
        else:
            if L[k] < X:
                # cari di bagian kanan
                i = k + 1
            else:
                # cari di bagian kiri
                j = k - 1

    # Setelah keluar dari while
    if ketemu:
        return k
    else:
        return -1


# ============================================
# Program Utama
# ============================================

L = [3, 7, 11, 18, 25, 39, 42, 56, 63, 75]
n = len(L)

X = int(input("Masukkan nilai yang dicari: "))

hasil = binarySearch(L, n, X)

if hasil != -1:
    print("X ditemukan pada indeks ke-", hasil)
else:
    print("X tidak ditemukan dalam larik")