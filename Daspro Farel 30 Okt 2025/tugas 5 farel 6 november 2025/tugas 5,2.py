# Program: Menghitung perpangkatan
# NAMA : Farel Ilyasa Habi Pratama
# KELAS : E
# NIM : 25041450138

if __name__ == "__main__":
    print("PROGRAM Menghitung perpangkatan a^n, a dan n bilangan bulat sembarang.")
    print("-" * 50)

    try:
        # Input dari user
        a_str = input("Masukkan nilai yang dipangkatkan (a, real): ")
        n_str = input("Masukkan nilai pangkat (n, bilangan bulat): ")

        a = float(a_str)
        n = int(n_str) 
        
        # Validasi tambahan untuk n (walaupun float() akan gagal jika input non-angka)
        if n != float(n_str):
             print("Error: Pangkat (n) harus berupa bilangan bulat.")
        
        # Panggil fungsi
        hasil = hitung_perpangkatan(a, n)

        # Output hasil
        print("-" * 50)
        print(f"Hasil dari {a}^{n} adalah: {hasil}")
        
    except ValueError:
        print("Error: Pastikan input 'a' adalah angka (real) dan input 'n' adalah bilangan bulat.")
    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")