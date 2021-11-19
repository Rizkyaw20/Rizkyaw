phi  = 3.14
r = 7
L = phi * (r * r)
 
print(L)

print('Menghitung luas lingakaran')
print('==============================')
r = int(input('masukan jari-jari lingkaran: '))
phi = 3.14
L = phi * (r * r)
print('Luas lingakaran dengan jari-jari {} adalah {}'.format(r, L))

def luas_lingkaran(r):
    return 3.14 * (r * r)
 
r = input('masukan jari-jari lingkaran: ')
luas = luas_lingkaran(int(r))
 
print('Luasnya: {}'.format(luas))
