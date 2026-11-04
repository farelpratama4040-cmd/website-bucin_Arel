# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E

def PencarianBeruntunVersi2(x, N, NilYangDicari, ketemu):
    i = 0
    ketemu = False
    while (i<(N-1)) and (not ketemu):
        if(x[i]==NilYangDicari):
            ketemu = True
        else:
            i = i + 1

    return ketemu