# function 1


def banner(tinggi,lebar):
    area = tinggi * lebar 
    return area 
# function 2

def harga(area,meter):
    cetak = area * meter 
    print('harga cetak :',cetak)
    print('-------------------')

# call function 

area = banner(4,7)
harga(area,114000)

