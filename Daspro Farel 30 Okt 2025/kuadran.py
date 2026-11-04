# Program untuk menentukan kuadran dari sebuah titik (x, y)
# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E


# Input
x = float(input("Masukkan nilai x: "))
y = float(input("Masukkan nilai y: "))

# Proses dan Output
if x > 0 and y > 0:
    print(f"Titik ({x}, {y}) terletak di Kuadran I")
elif x < 0 and y > 0:
    print(f"Titik ({x}, {y}) terletak di Kuadran II")
elif x < 0 and y < 0:
    print(f"Titik ({x}, {y}) terletak di Kuadran III")
elif x > 0 and y < 0:
    print(f"Titik ({x}, {y}) terletak di Kuadran IV")
elif x == 0 and y == 0:
    print(f"Titik ({x}, {y}) terletak di titik pusat (0,0)")
else:
    print(f"Titik ({x}, {y}) tidak terletak di kuadran manapun (berada pada sumbu X atau Y)")