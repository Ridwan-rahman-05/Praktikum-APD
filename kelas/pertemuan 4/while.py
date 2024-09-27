lagi="yes"
ulang=0
while lagi=="yes":
    ulang +=1
    print("mabar")
    lagi=input("mabar lagi gak?")
print("selesai mabar!")
print(f"perulangan terjadi sebanyak {ulang} kali")

while true:
    ulang = input("mabar lagi :")
    if ulang=="gk":
        break
    print("mabar lagi")