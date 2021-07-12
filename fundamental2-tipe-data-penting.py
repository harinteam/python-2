# Tipe data skalar => tipe data sederhana
anak1 = 'Muhammad Umar Alfatih'
anak2 = 'Nyimas Hanin Asyifa Almahira'
anak3 = 'Muhammad Uwais Alqarni'
anak4 = 'Nyimas Husna Aghnia'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('---' * 7)

# Tipe data List/daftar/array
anak = ['Muhammad Umar Alfatih', 'Nyimas Hanin Asyifa Almahira', 'Muhammad Uwais Alqarni', 'Nyimas Husna Aghnia']
print(anak)
anak.append('Belum tau')
print(anak)

print('---' * 7)

# Sapa anak ke-2
print(f'Hai {anak[1]}!')

print('---' * 7)

# Sapa semua anak cara gampang
for a in anak:
    print(f'Hai {a}')
