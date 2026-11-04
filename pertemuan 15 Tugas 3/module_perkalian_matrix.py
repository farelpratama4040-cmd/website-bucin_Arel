# Module Perkalian Matrix
# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E

def bacaMatrix(Matriks, NBar, NKol, nama):
    for i in range(NBar):
        for j in range(NKol):
            print(f"Inputkan Matrix {nama} ke {i},{j} : ", end="")
            Matriks[i][j] = int(input())

def cetakMatrix(Matriks, NBar, NKol):
    for i in range(NBar):
        for j in range(NKol):
            print(Matriks[i][j], end=' ')
        print()

def PerkalianMatriks(A, B, C, m, n, p):
    # m = baris matriks A
    # n = kolom matriks A / baris matriks B
    # p = kolom matriks B
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] = C[i][j] + (A[i][k] * B[k][j])