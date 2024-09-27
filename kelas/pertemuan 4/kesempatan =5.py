kesempatan = 5
while kesempatan>0:
    username=input("masukkan username :")
    password=input("masukkan password :")
    if username=="admin" and password=="admin#123":
        print("berhasil login")
        break
    else:
        print("gagal login")
