#data_mhs = {
 #   "nama" : "ucup",
  #  "nim" : 1,
   # "matkul" :["APD", "Kalkukus", "jarkom"],
    #"dosen" : {
     #   "nama" : "pak awang",
      #  "matkul" : "APD"
    #}
    
#}

data_mhs = [
    {
        "nama" : "ucup",
        "role" : "admin"
    },

    {
        "nama" : "michael",
        "role" : "user"
    }
]

data_mhs2 =[
    ["ucup", "admin"],
    ["michael", "user"]
]

print(data_mhs[0]['nama'])
print(data_mhs[1]['nama'])
print(data_mhs2[0][1])

#data_mhs['alamat'] ='samarinda'
#data_mhs['alamat'] = 'tenggarong'


#data_mhs.update({'alamat' : 'samarinda'})
#del data_mhs["nim"]

#cache = data_mhs.pop("nim")
#data_mhs["id"] = cache
#rint(cache, "cache")

#print(data_mhs,)

##for data in data_mhs:
  #  print(data)
#for key_data, value_data in data_mhs.items():
 #   print(f"key: {key_data}\nvalue: {value_data}\n")    
#print(data_mhs['nama'])
#print(data_mhs['nim'])

#key = "apel", "jeruk", "mangga"
#value = 1
#buah = dict.fromkeys(key, value)
#print(buah)

#Nilai = {
#    "Matematika" : 80,
#    "B. Indonesia" : 90,
 #   "B. Inggris" : 81
  #  }
#sebelum Setdefault
#print(Nilai)
#print("")
#menggunakan setdefault
#print("Nilai : ", Nilai.setdefault("Kimia", 70))
#print("")
#setelah menggunakan setdefault
#print(Nilai)