# Program: Menghitung jumlah kemunculan bilangan genap
# NAMA : Farel Ilyasa Habi Pratama
# KELAS : E
# NIM : 25041450138

def hitung_bilangan_genap():
    print("=== Program Menghitung Jumlah Bilangan Genap ===")
    print("Masukkan bilangan bulat satu per satu.")
    print("Ketik 9999 untuk mengakhiri input.\n")

    jumlah_genap = 0

    while True:
        try:
            x = int(input("Masukkan bilangan: "))
        except ValueError:
            print("Input tidak valid! Harap masukkan bilangan bulat.")
            continue

        if x == 9999:
            break  # keluar dari loop

        if x % 2 == 0:
            jumlah_genap += 1

    print("\nJumlah bilangan genap yang dimasukkan adalah:", jumlah_genap)


# Program utama
if __name__ == "__main__":
    hitung_bilangan_genap()
