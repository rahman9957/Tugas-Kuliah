# input
print('TARGET PENGIRIMAN')
pengiriman = int(input('masukkan total barang pengiriman : '))

# proses 
if pengiriman  > 200 :
    kriteria = 'PRIORITAS'
elif pengiriman  > 150 :
    kriteria = 'CEPAT'
elif pengiriman > 110 :
    kriteria = 'STANDAR'
elif pengiriman > 80 :
    kriteria = 'TERTINGGAL'
else :
    kriteria = 'GAGAL'  
    

# output 
print ('kriteria :',kriteria)
print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    