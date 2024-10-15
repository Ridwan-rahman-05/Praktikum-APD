akun = {"admin": "admin#123"}  
simpan_data = {}  

while True:
    print("="*32)
    print("  MANAJEMEN RENCANA PERJALANAN")
    print("="*32)
    print("1. Login")
    print("2. Daftar")
    print("3. Keluar Program")
    pilih = input("Silahkan pilih opsi: ")

    if pilih == "1":  
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        
        if username in akun and akun[username] == password:
            print(f"Selamat datang, {username}")

            while True:
                if username == "admin": 
                    print("="*32)
                    print("          Menu Admin")
                    print("="*32)
                    print("1. Lihat Semua Rencana Perjalanan")
                    print("2. Tambah Rencana Perjalanan")
                    print("3. Update Rencana Perjalanan")
                    print("4. Hapus Rencana Perjalanan")
                    print("5. Logout")
                    pilihan = input("Silahkan pilih opsi: ")

                    if pilihan == "1":  
                        if len(simpan_data) == 0:
                            print("Tidak ada rencana perjalanan.")
                        else:
                            for user, data in simpan_data.items():
                                print(f"Rencana Perjalanan {user}:")
                                for i, rencana in enumerate(data):
                                    print(f"Rencana {i + 1}:")
                                    print(f"Destinasi        : {rencana['tujuan']}")
                                    print(f"Keberangkatan    : {rencana['berangkat']}")
                                    print(f"Kembali          : {rencana['kembali']}")
                                    print(f"Detail Aktivitas : {rencana['aktivitas']}")
                        input("[ENTER]...")

                    elif pilihan == "2":  
                        user_rencana = input("Masukkan username pemilil rencana untuk menambah rencana : ")
                        tujuan    = input("Masukkan destinasi             : ")
                        berangkat = input("Masukkan tanggal keberangkatan : ")
                        kembali   = input("Masukkan tanggal kembali       : ")
                        aktivitas = input("Masukkan detail aktivitas      : ")

                        if user_rencana in simpan_data:
                            simpan_data[user_rencana].append({
                                "tujuan"    : tujuan, 
                                "berangkat" : berangkat, 
                                "kembali"   : kembali, 
                                "aktivitas" : aktivitas
                            })
                        else:
                            simpan_data[user_rencana] = [{
                                "tujuan"   : tujuan, 
                                "berangkat": berangkat, 
                                "kembali"  : kembali, 
                                "aktivitas": aktivitas
                            }]
                        print("Rencana perjalanan berhasil ditambahkan.")
                        input("[ENTER]...")

                    elif pilihan == "3":  
                        user_rencana = input("Masukkan username pemilik rencana yang ingin diupdate : ")
                        if user_rencana in simpan_data:
                            for i, rencana in enumerate(simpan_data[user_rencana]):
                                print(f"Rencana {i + 1}:")
                                print(f"Destinasi        : {rencana['tujuan']}")
                                print(f"Keberangkatan    : {rencana['berangkat']}")
                                print(f"Kembali          : {rencana['kembali']}")
                                print(f"Detail Aktivitas : {rencana['aktivitas']}")

                            update = input("Masukkan nomor rencana perjalanan yang ingin diupdate : ")
                            if update.isdigit():
                                update = int(update) - 1
                                if 0 <= update < len(simpan_data[user_rencana]):
                                    tujuan    = input("Masukkan destinasi baru                : ")
                                    berangkat = input("Masukkan tanggal keberangkatan baru : ")
                                    kembali   = input("Masukkan tanggal kembali baru         : ")
                                    aktivitas = input("Masukkan detail aktivitas baru      : ")

                                    simpan_data[user_rencana][update] = {
                                        "tujuan": tujuan, 
                                        "berangkat": berangkat, 
                                        "kembali": kembali, 
                                        "aktivitas": aktivitas
                                    }
                                    print("Rencana perjalanan berhasil diupdate!")
                                    input("[ENTER]...")
                                else:
                                    print("Nomor rencana perjalanan tidak valid.")
                            else:
                                print("Input harus berupa angka.")
                        else:
                            print(f"Tidak ada rencana perjalanan untuk {user_rencana}")

                    elif pilihan == "4":  
                        user_rencana = input("Masukkan username pemilik rencana yang ingin dihapus: ")
                        if user_rencana in simpan_data:
                            for i, rencana in enumerate(simpan_data[user_rencana]):
                                print(f"Rencana {i + 1}:")
                                print(f"  Destinasi        : {rencana['tujuan']}")
                                print(f"  Keberangkatan    : {rencana['berangkat']}")
                                print(f"  Kembali          : {rencana['kembali']}")
                                print(f"  Detail Aktivitas : {rencana['aktivitas']}")

                            hapus = input("Masukkan nomor rencana perjalanan yang ingin dihapus: ")
                            if hapus.isdigit():
                                hapus = int(hapus) - 1
                                if 0 <= hapus < len(simpan_data[user_rencana]):
                                    simpan_data[user_rencana].pop(hapus)
                                    print("Rencana perjalanan berhasil dihapus.")
                                    input("[ENTER]...")
                                else:
                                    print("Nomor rencana perjalanan tidak valid.")
                            else:
                                print("Input harus berupa angka.")
                        else:
                            print(f"Tidak ada rencana perjalanan untuk {user_rencana}")

                    elif pilihan == "5":  
                        print("Berhasil logout.")
                        input("[ENTER]...")
                        break

                    else:
                        print("Opsi tidak valid.")

                else:  
                    print("="*32)
                    print("          Menu User")
                    print("="*32)
                    print("1. Lihat Rencana Perjalanan")
                    print("2. Tambah Rencana Perjalanan")
                    print("3. Logout")
                    pilihan = input("Silahkan pilih opsi: ")

                    if pilihan == "1":  
                        if username in simpan_data and len(simpan_data[username]) > 0:
                            for i, rencana in enumerate(simpan_data[username]):
                                print(f"Rencana Perjalanan {i + 1}:")
                                print(f"  Destinasi        : {rencana['tujuan']}")
                                print(f"  Keberangkatan    : {rencana['berangkat']}")
                                print(f"  Kembali          : {rencana['kembali']}")
                                print(f"  Detail Aktivitas : {rencana['aktivitas']}")
                        else:
                            print("Tidak ada rencana perjalanan.")
                        input("[ENTER]...")

                    elif pilihan == "2":  
                        tujuan    = input("Masukkan destinasi                : ")
                        berangkat = input("Masukkan tanggal keberangkatan : ")
                        kembali   = input("Masukkan tanggal kembali         : ")
                        aktivitas = input("Masukkan detail aktivitas      : ")

                        if username in simpan_data:
                            simpan_data[username].append({
                                "tujuan": tujuan, 
                                "berangkat": berangkat, 
                                "kembali": kembali, 
                                "aktivitas": aktivitas
                            })
                        else:
                            simpan_data[username] = [{
                                "tujuan": tujuan, 
                                "berangkat": berangkat, 
                                "kembali": kembali, 
                                "aktivitas": aktivitas
                            }]
                        print("Rencana perjalanan berhasil ditambahkan.")
                        input("[ENTER]...")

                    elif pilihan == "3":  # Logout
                        print("Berhasil logout.")
                        input("[ENTER]...")
                        break

                    else:
                        print("Opsi tidak valid.")
        else:
            print("Username atau password salah.")

    elif pilih == "2":  
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in akun:
            print("Username sudah terdaftar.")
        else:
            akun[username] = password  
            print(f"User {username} berhasil terdaftar!")
            input("[ENTER]...")

    elif pilih == "3":  
        print("Program selesai.")
        break

    else:
        print("Opsi tidak valid.")






