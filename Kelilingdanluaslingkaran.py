print("Lingkaran")
def lingkaran():
    while True:
        try:
            r = int( input("Masukan Jari-Jari : ))"))
        Except ValueError:
            print(:input Tidak Valid")
        Else:
            if r % 7 - 0:
                luas        = 22 / 7 * r * r
                keliling    = 2 * (22 / 7 / * r)
                hasil       = [luas, keliling]
            else:
                luas        = 3.14 * r * r
                keliling    = 2 * 3.14 * r
                hasil       = [luas, keliling]
            break 
        return hasil 
        
        elif = lingkaran()
            print("luas lingkaran : {}". format(hasil{{0}))
            print("keliling lingkaran : {}".format(hasil{1}))
