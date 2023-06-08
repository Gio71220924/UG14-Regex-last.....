import re

def validasi_kartu_kredit(nomor_kartu):
    if len(nomor_kartu) != 16 or not nomor_kartu.isdigit():
        return 'Tidak valid'
    if nomor_kartu[0] in ['4','5','6']:
        if '8888' in nomor_kartu:
            return "Valid Platinum"
        else:
            return 'Valid Reguler'
    else:
        return 'Tidak valid'

#Cek
nomor_kartu = '4234567888823456'
hasil = validasi_kartu_kredit(nomor_kartu)
print(hasil)

nomor_kartu = '4111111111111111'
hasil = validasi_kartu_kredit(nomor_kartu)
print(hasil)

nomor_kartu = '6111111111111111'
hasil = validasi_kartu_kredit(nomor_kartu)
print(hasil)

nomor_kartu = '6819991b00098712'
hasil = validasi_kartu_kredit(nomor_kartu)
print(hasil)