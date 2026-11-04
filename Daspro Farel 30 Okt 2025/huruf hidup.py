# Program untuk membaca sebuah karakter, lalu menuliskan pesan "huruf hidup" jika karakter tersebut huruf vokal
# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E

kar = input("Masukkan sebuah huruf: ").lower()

if kar in ['a', 'i', 'u', 'e', 'o']:
    print("huruf hidup")
else:
    print("bukan huruf hidup")