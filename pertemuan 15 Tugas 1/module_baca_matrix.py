# Module Baca Cetak Matrix
# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E

def bacaMatrix(matrix, NBar, NKol):
    for i in range(0, NBar):
        for j in range(0, NKol):
            # Print format disesuaikan biar rapi
            print(f"inputkan larik ke- {i},{j} : ", end="") 
            matrix[i][j] = int(input())

def cetakMatrix(matrix, NBar, NKol):
    for i in range(0, NBar):
        for j in range(0, NKol):
            print(matrix[i][j], end=' ')
        print() # Print baris baru