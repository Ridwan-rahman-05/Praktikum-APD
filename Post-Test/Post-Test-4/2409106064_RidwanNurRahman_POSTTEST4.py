kesempatan = 3

while kesempatan > 0:
    print("Login untuk mengakses program:")
    username = input("masukkan Username = ")
    password = input("masukkan Password = ")

    if username == "ridwan" and password == "064":
        print("Login berhasil!")
        break
    else:
        print("Username atau Password salah!")
        kesempatan -= 1
        print(f"Login gagal! Percobaan tersisa {kesempatan} kali")
        

if kesempatan == 0:
    print("Keluar program.")
else:
    
    while True:
        print("=========================================================")
        print("  Menu Program Menghitung Luas/Volume Bangun Ruang       ") 
        print("=========================================================")
        print("Menu bangun ruang :")
        print("1. Kubus")
        print("2. Balok")
        print("3. Tabung")
        print("0. Keluar program")
        print("=========================================================")
        
        bangun_ruang = int(input("Pilih bangun ruang = "))

        if bangun_ruang == 1:
            print("Pilih rumus:")
            print("1. Luas")
            print("2. Volume")
            rumus = int(input("Luas atau Volume? = "))
            if rumus == 1:
                rusuk = float(input("Panjang rusuk = "))
                luas_kubus = 6 * rusuk * rusuk
                print(f"Luas kubus = {luas_kubus}\n")
            elif rumus == 2:
                rusuk = float(input("Panjang rusuk = "))
                volume_kubus = rusuk * rusuk * rusuk
                print(f"Volume kubus = {volume_kubus}\n")

        elif bangun_ruang == 2:
            print("Pilih rumus:")
            print("1. Luas")
            print("2. Volume")
            rumus = int(input("Luas atau Volume? = "))
            if rumus == 1:
                panjang = float(input("Panjang = "))
                lebar = float(input("Lebar = "))
                tinggi = float(input("Tinggi = "))
                luas_balok = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
                print(f"Luas balok = {luas_balok}")
            elif rumus == 2:
                panjang = float(input("Panjang = "))
                lebar = float(input("Lebar = "))
                tinggi = float(input("Tinggi = "))
                volume_balok = panjang * lebar * tinggi
                print(f"Volume balok = {volume_balok}\n")

        elif bangun_ruang == 3:
            print("\nPilih rumus:")
            print("1. Luas Selimut")
            print("2. Luas Permukaan")
            print("3. Volume")
            rumus = int(input("Luas Permukaan, Selimut, atau Volume? = "))
            if rumus == 1:
                radius = float(input("Jari-jari = "))
                tinggi = float(input("Tinggi = "))
                if radius % 7 == 0:
                    phi = 22 / 7
                else:
                    phi= 3.14
                luas_selimut_tabung = 2 * phi * radius * tinggi
                print(f"Luas selimut tabung = {luas_selimut_tabung}\n")
            elif rumus == 2:
                radius = float(input("Jari-jari = "))
                tinggi = float(input("Tinggi = "))
                if radius % 7 == 0:
                    phi = 22 / 7
                else:
                    phi = 3.14
                luas_permukaan_tabung = 2 * phi * radius * (radius + tinggi)
                print(f"Luas permukaan tabung = {luas_permukaan_tabung}\n")
            elif rumus == 3:
                radius = float(input("Jari-jari = "))
                tinggi = float(input("Tinggi = "))
                phi = 22 / 7 if radius % 7 == 0 else 3.14
                volume_tabung = phi * radius * radius * tinggi
                print(f"Volume tabung = {volume_tabung}\n")

        elif bangun_ruang == 0:
            print("Program selesai.")
            break

        else:
            print("Tolong masukkan pilihan yang tersedia!")
