angka = int(input("Masukkan angka: "))

if angka > 1:
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            print("Bukan angka prima")
            break
    else:
        print("Angka prima")
else:
    print("Bukan angka prima")
