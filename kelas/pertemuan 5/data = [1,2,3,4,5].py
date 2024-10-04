#data = [1,2,3,4,True,[2,3],"adi"]
#data_2 = list((1,2,3,4,5))
#data =["apel","durian","jeruk"]
#data[0:2] = "anggur","mangga"
#del data[1]
#data.pop(1)
#data.remove("jeruk")
#print(data*3)
#print()
#data.extend(["rambutan","semangka"])

# data.append("semangka")
#data.append(True)
#print(data)
#data.insert(0,"rambutan")
#print(len(data))

#print(data[5][0])
#print(type(data_2))

#data_mahasiswa  = [
#    ["060","ifnu",["APD","ARSIKOM"]],
#   ["065","adi"]
#]
#print(data_mahasiswa[1][0])

buah =["apel","durian","jeruk"]
index = 1
#for data in buah:
#    print(f"data ke {index}")
#    print(data)
#    print("="*10)
#    index = index + 1

for index, item enumerate (buah,2):
    print(f"data ke {index + 1}")
    print (item[0])
    print (item[1])