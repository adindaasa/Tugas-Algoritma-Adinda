# BANTUAN PIP
nama = str(input('Masukkan Nama : '))
umur = int(input('Masukkan Umur : '))
pekerjaan_orangtua = str(input('Pekerjaan Orang Tua : '))
penghasilan_orangtua = int(input('Masukkan Penghasilan OrangTua : '))
persyaratan1 = pekerjaan_orangtua not in ['ASN,Direktur Perusahaan,Pegawai Kantor'] and umur <21 and penghasilan_orangtua <1500000
persyaratan2 = (input("Yatim/Piatu? (yes/no) : "))

if persyaratan1 and persyaratan2:
    print('Mendapatkan Bantuan PIP')

else:
    print('Tidak Mendapatkan Bantuan PIP')

print(nama, umur, pekerjaan_orangtua,penghasilan_orangtua, persyaratan1, persyaratan2)

