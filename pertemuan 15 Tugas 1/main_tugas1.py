# Main Program
# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E

import module_baca_matrix as mbm

def main():
    NBar = int(input("inputkan nilai N Baris= "))
    NKol = int(input("inputkan nilai N Kolom= "))
    
    # Inisialisasi matriks dengan angka 0
    matrix = [[0 for col in range(NKol)] for row in range(NBar)]
    
    mbm.bacaMatrix(matrix, NBar, NKol)
    
    print("\nBerikut adalah bentuk matriksnya:")
    mbm.cetakMatrix(matrix, NBar, NKol)

if __name__ == "__main__":
    main()