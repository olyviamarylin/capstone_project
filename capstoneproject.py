# MEMBUAT APLIKASI DENGAN BASIS FITUR CRUD
# DATA KARYAWAN DALAM SEBUAH PERUSAHAAN


# All Data Karyawan
dataKaryawan = [{'NAMA LENGKAP':'YUSUF PRAYOGA', 'STATUS KARYAWAN' : 'TETAP', 'ALAMAT' : 'JAKARTA','JENIS KELAMIN':'L', 'NO. KTP':'3172968745678432'}, 
{'NAMA LENGKAP':'HAYDIR AKBAR', 'STATUS KARYAWAN' : 'KONTRAK', 'ALAMAT' : 'KARAWANG','JENIS KELAMIN':'L', 'NO. KTP':'3185462409895647'}]

# 1. Daftar Karyawan

def tampilanData():
    tampilan = ''
    while tampilan != '3':
        print('''\n===============DATA KARYAWAN PT. XYZ================\n
Pilihan Menu:
1. Daftar Karyawan
2. Pencarian Data Karyawan
3. Kembali Ke Menu Utama
====================================================''')
        tampilan = input("Silahkan Pilih Nomor [1-3]: ")
        if tampilan == '1':
                if len(dataKaryawan) != 0 :
                    print('''====================================================
DAFTAR KARYAWAN PT. XYZ:
NO\t| NAMA LENGKAP\t\t|  STATUS KARYAWAN\t|  ALAMAT\t| JENIS KELAMIN\t| NO. KTP''')
                    for j,i in enumerate(dataKaryawan) :
                        print(f"{j+1}\t| {i['NAMA LENGKAP']}\t\t|  {i['STATUS KARYAWAN']}\t\t|  {i['ALAMAT']}\t| {i['JENIS KELAMIN']}\t\t| {i['NO. KTP']}")
        elif tampilan =='2':
                if len(dataKaryawan) !=0 :
                    print("====================================================")
                    karyawan = input('Masukkan NO. KTP Karyawan: ')
                    print(f"\nData Karyawan dengan NO.KTP Karyawan : {karyawan}")
                    for j, i in enumerate(dataKaryawan):
                        if i ['NO. KTP'] == karyawan :
                            print(f"{j+1}. | NAMA LENGKAP : {i['NAMA LENGKAP']} | STATUS KARYAWAN : {i['STATUS KARYAWAN']} | ALAMAT : {i['ALAMAT']} | JENIS KELAMIN : {i['JENIS KELAMIN']} | NO. KTP : {i['NO. KTP']}")
                            break
                        else:
                            print('\nNomor KTP Belum Terdaftar!') 
        elif tampilan == '3':
            break
        else:
            print('\nERROR!, Silahkan Pilih Nomor [1-3]')
    return tampilan

# 2. Menambahkan Data Karyawan    
def regist_karyawan():  #function untuk mendefinisikan 
    add = ''
    while add != '2':    #while loop untuk mengetahui suatu kondisi tertentu
        print('''\n================REGISTRASI KARYAWAN=================\n
Pilihan Menu:
1. Registrasi Karyawan
2. Kembali Ke Menu Utama
====================================================''')
        add = input("Silahkan Pilih Nomor [1-2]: ")  #untuk menentukan kemungkinan dari inputan user
        if add == '1':
            add_nik = str(input('\nMasukan NO. KTP: '))
            add_data = [dataKaryawan[i]["NO. KTP"] for i in range(len(dataKaryawan))]   # pengecekan data inputan user
            if add_nik in add_data:
                print('Nomor KTP Sudah Ada!')
            else:
                addNamaLengkap = input('Masukan Nama Lengkap: ')
                addStatus = input('Masukan Status Karyawan (Tetap/Kontrak): ')
                addAlamat = input('Masukan Alamat: ')
                addGender = input('Masukan Jenis Kelamin (L/P): ')
                while True: 
                    addConfirm = input('Apakah data akan disimpan (Y/N)? ')   #konfirmasi sebelum data di tambahkan
                    if addConfirm.upper() == 'Y':
                        dataKaryawan.append({
                                                'NAMA LENGKAP': addNamaLengkap.upper(),
                                                'STATUS KARYAWAN': addStatus.upper(),
                                                'ALAMAT': addAlamat.upper(),
                                                'JENIS KELAMIN': addGender.upper(),
                                                'NO. KTP': add_nik
                                                })
                        print('\nRegistrasi Berhasil!')
                        break
                    elif addConfirm.upper() == 'N':
                        print('\nData Karyawan Tidak Tersimpan')
                        break
        elif add == '2':
            break
        else:
            print('\nERROR!, Silahkan Pilih Nomor [1-2]') 
    return add

# 3. Mengubah Data Karyawan                      
def update_data():
    update = True
    while update != '2':
        print('''\n================UPDATE DATA KARYAWAN================\n
Pilihan Menu:
1. Update Data Karyawan
2. Kembali Ke Menu Utama
====================================================''')
        update = input("Silahkan Pilih Nomor [1-2]: ")
        if update == '1':
            nomor_nik = input('\nMasukan Nomor KTP Karyawan yang ingin diubah (16 digit) : ')
            if len(nomor_nik) == 16 :       #validasi jumlah digit pada no. ktp
                print(f'\nData NO. KTP Karyawan : {nomor_nik}\n')
                for j,i in enumerate(dataKaryawan) :
                    if i['NO. KTP'] == nomor_nik:
                        print('NO\t| NAMA LENGKAP\t\t|  STATUS KARYAWAN\t|  ALAMAT\t| JENIS KELAMIN\t| NO. KTP')
                        print(f"{j+1}\t| {i['NAMA LENGKAP']}\t\t|  {i['STATUS KARYAWAN']}\t\t|  {i['ALAMAT']}\t| {i['JENIS KELAMIN']}\t\t| {i['NO. KTP']}")
                        continue
                while True:
                    ubah_data = input('Anda Yakin Data Akan Diubah? [Y/N] : ')      # konfirmasi sebelum perubahan data
                    if ubah_data.upper() == 'Y' :
                        ubahKolom = input('\nInput kolom data yang ingin diubah : ')
                        kolomBaru = input(f'Input data {ubahKolom} baru : ')
                        if ubahKolom.upper() == 'NAMA LENGKAP':
                            i['NAMA LENGKAP'] = kolomBaru.upper()
                        elif ubahKolom.upper() == 'STATUS KARYAWAN':
                            i['STATUS KARYAWAN'] = kolomBaru.upper()
                        elif ubahKolom.upper() == 'ALAMAT':
                            i['ALAMAT'] == kolomBaru.upper()
                        elif ubahKolom.upper() == 'JENIS KELAMIN':
                            i['JENIS KELAMIN'] = kolomBaru.upper()
                        elif ubahKolom.upper() == 'NO. KTP':
                            i['NO. KTP'] = kolomBaru
                        else:
                            print('\nkolom tidak tersedia!')
                            break
                        print('\nData Berhasil Diubah!')
                        print(f"{j+1}\t| {i['NAMA LENGKAP']}\t\t|  {i['STATUS KARYAWAN']}\t\t|  {i['ALAMAT']}\t| {i['JENIS KELAMIN']}\t\t| {i['NO. KTP']}")
                        break
                    elif ubah_data.upper() == 'N' :
                        print('\nData Tidak Diubah')
                        break
                    else :
                        print('\nData Karyawan Tidak Ditemukan!')
            else :
                print('\nJumlah NO. KTP Tidak sesuai!')        
        elif update == '2':
            break
        else:
            print('\nERROR!, Silahkan Pilih Nomor [1-2]')


# 4. Menghapus Data Karyawan
def hapus_data():
    remove = True
    while remove != '2':
        print('''\n================DELETE DATA KARYAWAN================\n
Pilihan Menu:
1. Delete Data Karyawan
2. Kembali Ke Menu Utama
====================================================''')
        remove = input("Silahkan Pilih Nomor [1-2]: ")
        if remove == '1':
            if len(dataKaryawan) != 0 :
                nomor_nik = input('\nMasukan Nomor KTP Karyawan yang ingin Hapus : ')
                print(f'\nData Nomor KTP Karyawan : {nomor_nik}\n')
                print('NO\t| NAMA LENGKAP\t\t|  STATUS KARYAWAN\t|  ALAMAT\t| JENIS KELAMIN\t| NO. KTP')
                for j,i in enumerate(dataKaryawan) :
                    if i['NO. KTP'] == nomor_nik:
                        print(f"{j+1}\t| {i['NAMA LENGKAP']}\t\t|  {i['STATUS KARYAWAN']}\t\t|  {i['ALAMAT']}\t| {i['JENIS KELAMIN']}\t\t| {i['NO. KTP']}")
                        break
                    else:                            
                        print('\nData Karyawan Belum Terdaftar!')
                        continue            
                while True:
                    remove1 = input('konfirmasi data akan dihapus [Y/N] : ')    # konfirmasi kembali sebelum datanya di hapus
                    if remove1.upper() == 'Y':
                        del dataKaryawan[j]
                        print('\nData Berhasil Dihapus!')
                        break
                    elif remove1.upper() == 'N':
                        print('\nData Tidak Dihapus')
                        break
                    else:
                        print('\nPilihan Tidak Sesuai')
                        continue
        elif remove == '2':
            break
        else:
            print('\nERROR!, Silahkan Pilih Nomor [1-2]')
    return 

# Menu Data
while True :
    pilihMenu = input('''
============= DAFTAR KARYAWAN PT. XYZ ==============

Menu Utama:
1. DAFTAR KARYAWAN
2. REGISTRASI KARYAWAN
3. UPDATE DATA KARYAWAN
4. DELETE DATA KARYAWAN
5. EXIT      
====================================================
Silahkan Pilih Nomor [1-5]: ''')

    if(pilihMenu == '1'):           # menu daftar karyawan
        tampilanData()
    elif(pilihMenu == '2'):         # menu registrasi karyawan
        regist_karyawan()
    elif(pilihMenu == '3'):         # menu update data karyawan
        update_data()
    elif(pilihMenu == '4'):         # menu hapus data karyawan
        hapus_data()
    elif(pilihMenu == '5'):
        print('Data Karyawan Closed!\n')    # menu exit system karyawan
        break
    else:
        print('\nERROR! Silahkan Pilih Nomor [1-5]') 

