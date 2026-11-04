# Main Program Penjumlahan Matrix
# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E

import module_penjumlahan_matrix as mpm

def main():
    NBar = int(input("inputkan nilai N Baris= "))
    NKol = int(input("inputkan nilai N Kolom= "))
    
    # Inisialisasi Matriks A, B, dan C dengan nilai 0
    A = [[0 for col in range(NKol)] for row in range(NBar)]
    B = [[0 for col in range(NKol)] for row in range(NBar)]
    C = [[0 for col in range(NKol)] for row in range(NBar)]
    
    mpm.bacaMatrixA(A, NBar,54 NKol)
    print("---")
    mpm.bacaMatrixB(B, NBar, NKol)
    print("---")
    
    mpm.PenjumlahanMatrix(A, B, C, NBar, NKol)
    
    print("Hasil Penjumlahan adalah matrix C: ")
    mpm.cetakMatrixC(C, NBar, NKol)

if __name__ == "__main__":
    main()