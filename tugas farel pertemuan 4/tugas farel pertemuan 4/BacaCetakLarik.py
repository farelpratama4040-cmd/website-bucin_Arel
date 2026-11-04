# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E

import ModuleBacaCetakLarik as bcl

def main():
    x = []
    N=int(input("inputkan nilai N = "))

    bcl.bacaLarik(x,N)

    NilYangDicari = int(input("inputkan nilai yang dicari = "))

    ketemu = False
    print("Ketemu = ",bcl.PencarianBeruntunVersi1(x,N,NilYangDicari, ketemu))

if __name__ == "__main__":
    main()