# import re
# def cek_kodepos(kodepos):
#     #Baca kode posnya
#     pattern = r"[0-9]{5}(?:-[0-9]{4})?$"

#     #cek tidak ada digit berulang
#     pattern2 = r"^(\d)(?!\1{7})\d{7}$"
#     hasil = re.findall (pattern2,kodepos )
#     print("Valid")

#     #cek 3 digit berurutan
#     pattern3 = r"(\d)\1{3,}"
#     if re.search(pattern3, kodepos):
#         return "Tidak valid"
#     else:
#         return "Valid"

# cek_kodepos('12145')
# cek_kodepos('32432')
# cek_kodepos('55252')
# cek_kodepos('55511')
# cek_kodepos('55155')


# import re
# def cek_kodepos(kodepos):
#     #Validasi kode pos.
#     pattern = r""
#     hasil = re.match(pattern, kodepos)

# cek_kodepos('12145')
# cek_kodepos('32432')
# cek_kodepos('55252')
# cek_kodepos('55511')
# cek_kodepos('55155')

# Versi sargi
def cek_kodepos(kodePos):
    if len(kodePos) == 5:
        total = 0
        for i in range(len(kodePos) -2 ):
            if kodePos[i] == kodePos[i+2]:
                total +=1
        if total >1:
            return "Tidak valid"
        else:
            return "Valid"
        
print(cek_kodepos('12145'))
print(cek_kodepos('32432'))
print(cek_kodepos('55252'))
print(cek_kodepos('55511'))
print(cek_kodepos('55155'))


# #Versi 3 kata
# import re
# def cek_kodepos(kodePos):
#     pola = r"^(?!.*(.).*\1(?!.*(\d\2{3})[1-9]\d{4}$))"
#     if re.match(pola, kodePos):
#         return "Valid"
#     else:
#         return 'Tidak valid'
# print(cek_kodepos('12145'))
# print(cek_kodepos('32432'))
# print(cek_kodepos('55252'))
# print(cek_kodepos('55511'))
# print(cek_kodepos('55155'))