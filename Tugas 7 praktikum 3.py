1.
print("Tampilkan n bilangan acak yang lebih kecil dari 0.5")

jumblah = int(input("Masukan jumblah n: "))
import random
for i in range(jumblah):
    print("Data ke",i+1 ,"-",(random.uniform(0.1,0.5)))