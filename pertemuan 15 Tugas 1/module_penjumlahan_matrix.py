# Module Penjumlahan Matrix
# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E

def bacaMatrixA(A, NBar, NKol):
    for i in range(0, NBar):
        for j in range(0, NKol):
            print(f"inputkan Matrix A ke {i},{j} : ", end="")
            A[i][j] = int(input())

def bacaMatrixB(B, NBar, NKol):
    for i in range(0, NBar):
        for j in range(0, NKol):
            print(f"inputkan Matrix B ke {i},{j} : ", end="")
            B[i][j] = int(input())

def PenjumlahanMatrix(A, B, C, NBar, NKol):
    for i in range(0, NBar):
        for j in range(0, NKol):
            C[i][j] = A[i][j] + B[i][j]

def cetakMatrixC(C, NBar, NKol):
    for i in range(0, NBar):
        for j in range(0, NKol):
            print(C[i][j], end=' ')
        print()