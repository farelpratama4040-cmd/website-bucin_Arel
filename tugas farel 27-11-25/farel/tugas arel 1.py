# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : 2583E

def checkIfPrime(numberToCheck):
    # Bilangan kurang dari 2 bukan bilangan prima
    if numberToCheck < 2:
        return False
    
    # Cek pembagi dari 2 sampai numberToCheck-1
    for x in range(2, numberToCheck):
        if numberToCheck % x == 0:
            return False  # Jika habis dibagi, berarti bukan prima
    
    return True  # Jika tidak ada pembagi, maka prima


# Program utama
num = int(input("Masukkan angka: "))

if checkIfPrime(num):
    print(num, "adalah bilangan prima.")
else:
    print(num, "bukan bilangan prima.")
