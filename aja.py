#rizkyaw
#k = 2 x pi x r
#l = pi x r x r
import math
def keliling():
    global k
    k = 2 * math.pi * r
  
def luas():
    global l
    r2 = r ** 2
    l = math.pi * r2

r = float(input("Masukkan nilai jari-jari lingkaran "))
keliling()
luas()
print("Besar keliling lingkaran dengan jari-jari", r, "adalah", k)