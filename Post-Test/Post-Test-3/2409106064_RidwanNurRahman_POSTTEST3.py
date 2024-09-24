print("=========================================================")
print("  Menu Program Menghitung Luas/volume Bangun Ruang       ") 
print("=========================================================")
print("Menu bangun ruang :")
print("1.kubus")
print("2.balok")
print("3.Tabung")

bangun_ruang = int(input("pilih bangun ruang ="))

if bangun_ruang == 1:
    print("pilih rumus :")
    print("1.luas")
    print("2.volume")
    rumus = int(input("luas/volume? ="))
    if rumus == 1:
        rusuk = int(input("panjang rusuk ="))
        luas_kubus = 6*rusuk*rusuk
        print(f"luas kubus = {luas_kubus}")

    elif rumus == 2:
        rusuk = int(input("panjang rusuk ="))
        volume_kubus = rusuk*rusuk*rusuk
        print(f"volume kubus = {volume_kubus}")

elif bangun_ruang == 2:
    print("pilih rumus :")
    print("1.luas")
    print("2.volume")
    rumus = int(input("luas/volume? ="))
    if rumus == 1:
        panjang = int(input("panjang ="))
        lebar = int(input("lebar ="))
        tinggi = int(input("lebar ="))
        luas_balok = (2*panjang*lebar)+(2*panjang*tinggi)+(2*lebar*tinggi)
        print(f"luas balok = {luas_balok}")

    elif rumus == 2:
        panjang = int(input("panjang ="))
        lebar = int(input("lebar ="))
        tinggi = int(input("lebar ="))
        volume_balok = panjang*lebar*tinggi
        print(f"volume balok = {volume_balok}")

elif bangun_ruang == 3:
    print("pilih rumus :")
    print("1.luas selimut")
    print("2.luas permukaan")
    print("3.volume")
    rumus = int(input("luas permukaan/selimut/volume? ="))
    if rumus == 1:
        radius = int(input("jari-jari ="))
        tinggi = int(input("tinggi ="))
        if radius %7==0:
            phi = int(22/7)
        else:
            phi = float(3.14)

        luas_selimut_tabung = 2*phi*radius*tinggi
        print(f"luas selimut tabung = {luas_selimut_tabung}")

    elif rumus == 2:
        radius = int(input("jari-jari ="))
        tinggi = int(input("tinggi ="))
        if radius %7==0:
            phi = int(22/7)
        else:
            phi = float(3.14)

        luas_permukaan_tabung = (2*phi*radius*tinggi) + (phi*radius*radius*tinggi)
        print(f"luas permukaan tabung = {luas_permukaan_tabung}")

    elif rumus == 3:
        radius = int(input("jari-jari ="))
        tinggi = int(input("tinggi ="))
        if radius %7==0:
            phi = int(22/7)
        else:
            phi = float(3.14)
        
        volume_tabung = phi*radius*radius*tinggi
        print(f"volume tabung = {volume_tabung}")


 








