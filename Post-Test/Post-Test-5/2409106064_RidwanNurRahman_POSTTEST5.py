akun = {"admin": "admin#123"}  
simpan_data = []  

while True:
    print("="*32)
    print("  MANAJEMEN RENCANA PERJALANAN")
    print("="*32)
    print("1. Login")
    print("2. Daftar")
    print("3. Keluar Program")
    pilih = input("Silahkan pilih opsi: ")

    if pilih == "1":  # Login
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        # Memeriksa login
        if username in akun and akun[username] == password:
            print(f"Selamat datang, {username}")

            while True:
                print("="*32)
                print("          Menu Admin")
                print("="*32)
                print("1. Lihat Rencana Perjalanan")
                print("2. Tambah Rencana Perjalanan")
                print("3. Update Rencana Perjalanan")
                print("4. Hapus Rencana Perjalanan")
                print("5. Logout")
                pilihan = input("Silahkan pilih opsi: ")

                if pilihan == "1":  # Lihat Rencana Perjalanan
                    if len(simpan_data) == 0:
                        print("Tidak ada rencana perjalanan.")
                    else:
                        for i, simpan in enumerate(simpan_data):
                            print(f"Rencana Perjalanan {i + 1}:")
                            print(f"Destinasi        : {simpan[0]}")
                            print(f"Keberangkatan    : {simpan[1]}")
                            print(f"Kembali          : {simpan[2]}")
                            print(f"Detail Aktivitas : {simpan[3]}")

                elif pilihan == "2":  # Tambah Rencana Perjalanan
                    tujuan = input("Masukkan destinasi                : ")
                    berangkat = input("Masukkan tanggal keberangkatan : ")
                    kembali = input("Masukkan tanggal kembali         : ")
                    aktivitas = input("Masukkan detail aktivitas      : ")

                    simpan_data.append([tujuan, berangkat, kembali, aktivitas])
                    print("Rencana perjalanan berhasil ditambahkan.")

                elif pilihan == "3":  # Update Rencana Perjalanan
                    if len(simpan_data) == 0:
                        print("Tidak ada rencana perjalanan.")
                    else:
                        for i, simpan in enumerate(simpan_data):
                            print(f"Rencana Perjalanan {i + 1}:")
                            print(f"Destinasi        : {simpan[0]}")
                            print(f"Keberangkatan    : {simpan[1]}")
                            print(f"Kembali          : {simpan[2]}")
                            print(f"Detail Aktivitas : {simpan[3]}")

                        update = input("Masukkan nomor rencana perjalanan yang ingin diupdate: ")
                        if update.isdigit():
                            update = int(update) - 1
                            if 0 <= update < len(simpan_data):
                                tujuan = input("Masukkan destinasi baru                : ")
                                berangkat = input("Masukkan tanggal keberangkatan baru : ")
                                kembali = input("Masukkan tanggal kembali baru         : ")
                                aktivitas = input("Masukkan detail aktivitas baru      : ")

                                simpan_data[update] = [tujuan, berangkat, kembali, aktivitas]
                                print("Rencana perjalanan berhasil diupdate!")
                            else:
                                print("Nomor rencana perjalanan tidak valid.")
                        else:
                            print("Input harus berupa angka.")

                elif pilihan == "4":  # Hapus Rencana Perjalanan
                    if len(simpan_data) == 0:
                        print("Tidak ada rencana perjalanan.")
                    else:
                        for i, simpan in enumerate(simpan_data):
                            print(f"Rencana Perjalanan {i + 1}:")
                            print(f"Destinasi        : {simpan[0]}")
                            print(f"Keberangkatan    : {simpan[1]}")
                            print(f"Kembali          : {simpan[2]}")
                            print(f"Detail Aktivitas : {simpan[3]}")

                        hapus = input("Masukkan nomor rencana perjalanan yang ingin dihapus: ")
                        if hapus.isdigit():
                            hapus = int(hapus) - 1
                            if 0 <= hapus < len(simpan_data):
                                simpan_data.pop(hapus)
                                print("Rencana perjalanan berhasil dihapus.")
                            else:
                                print("Nomor rencana perjalanan tidak valid.")
                        else:
                            print("Input harus berupa angka.")

                elif pilihan == "5":  # Logout
                    print("Berhasil logout.")
                    break

                else:
                    print("Opsi tidak valid.")

        else:
            print("Username atau password salah.")

    elif pilih == "2":  # Daftar
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in akun:
            print("Username sudah terdaftar.")
        else:
            akun[username] = password  # Menambahkan username dan password
            print(f"User {username} berhasil terdaftar!")

    elif pilih == "3":  # Keluar Program
        print("Program selesai.")
        break

    else:
        print("Opsi tidak valid.")

