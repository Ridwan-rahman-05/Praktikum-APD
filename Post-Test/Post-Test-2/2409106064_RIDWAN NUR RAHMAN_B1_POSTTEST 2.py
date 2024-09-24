def biodata():

    nama = input("Masukkan Nama: ")  
    umur = int(input("Masukkan Umur: ")) 
    tinggi_badan = float(input("Masukkan Tinggi Badan (cm): "))  
    status = input("Apakah Anda seorang mahasiswa? (ya/tidak): ")

    if status == "ya":
        status = "mahasiswa"
    elif status == "tidak":
        status = "Bukan mahasiswa"
   

    total_data_integer_dan_float = umur + tinggi_badan

    print("====================================================")
    print(" " * 14 + "Bio Data Anda")
    print("====================================================")
    print(f"Nama         : {nama}")
    print(f"Umur         : {umur} tahun")
    print(f"Tinggi Badan : {tinggi_badan} cm")
    print(f"Status       : {status}")
    print("====================================================")

    print(f"Total data intiger dan float: {total_data_integer_dan_float}")

biodata()
