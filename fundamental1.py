# KONSTRUKSI DASAR PTYHON
# SEQUENTIAL: Eksekusi berurutan
print('Hello World!')
print('by Harin')
print('Tanggal 03 Juli 2021')
print('---' * 7)

# PERCABANGAN
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus aja ya dan lari!')
else:
    print('Jalan lain dan jalan santai!')

# PERCABANGAN PILIHAN LEBIH DARI 2
ingin_balik = True

# new line
print('---' * 7)

# PERULANGAN
jumlah_anak = 4

# Tanpa Perulangan contoh dibawah ini harus menulis berulang kali
print('Halo anak #1')
print('Halo anak #2')
print('Halo anak #3')
print('Halo anak #4')
print('---' * 7)

# Pake perulangan contoh kode seperti dibawah ini: (code dibawah indexnya masih berulang #!)
for index_anak in range(1, jumlah_anak+1):
    print('Halo anak #1')

print('---' * 7)

# Pake perulangan contoh kode seperti dibawah ini: (code dibawah indexnya sudah berurutan #!)
for index_anak in range(1, jumlah_anak+1):
    print(f'Halo anak #{index_anak}')
