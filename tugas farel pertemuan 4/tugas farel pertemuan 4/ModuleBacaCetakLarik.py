# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E

def PencarianBeruntunVersi1(x,N,NilYangDicari, ketemu):
    i = 0;
    while (i<(N-1)) and (x[i] != NilYangDicari):
        i = i + 1

    if (x[i] == NilYangDicari):
        ketemu = True
    else:
        ketemu = False

    return ketemu


def HitungRata(rata,x,N):
    jumlah = 0
    for i in range(0,N) :
        jumlah = jumlah + x[i]
    rata = jumlah / N
    return rata


def bacaLarik(x,N):
    for i in range(0,N):
        baca = int(input("inputkan nilai larik ke -  "))
        x.append(baca)

def cetakLarik(x,N):
    for i in range(0,N) :
        print(x[i])