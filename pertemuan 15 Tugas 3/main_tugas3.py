# Main Program Perkalian Matrix
# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E

import module_perkalian_matrix as mkm

def main():
    print("--- SYARAT: Kolom Matriks A harus = Baris Matriks B ---")
    m = int(input("Input jumlah Baris Matriks A (m): "))
    n = int(input("Input jumlah Kolom Matriks A / Baris Matriks B (n): "))
    p = int(input("Input jumlah Kolom Matriks B (p): "))
    
    # Inisialisasi Matriks
    A = [[0 for col in range(n)] for row in range(m)] # Ukuran m x n
    B = [[0 for col in range(p)] for row in range(n)] # Ukuran n x p
    C = [[0 for col in range(p)] for row in range(m)] # Matriks Hasil ukuran m x p
    
    print("\n--- Isi Matriks A ---")
    mkm.bacaMatrix(A, m, n, "A")
    
    print("\n--- Isi Matriks B ---")
    mkm.bacaMatrix(B, n, p, "B")
    
    # Proses Perkalian
    mkm.PerkalianMatriks(A, B, C, m, n, p)
    
    print("\nHasil Perkalian Matriks A * B (Matriks C):")
    mkm.cetakMatrix(C, m, p)

if __name__ == "__main__":
    main()