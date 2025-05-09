# FUNCTION
def hitung_total(jumlah_porsi,perporsi):
    total = jumlah_porsi * perporsi
    return total

print('Total harga (function) gacoan :', hitung_total(6, 12300))

# LAMBDA
# cara 1 : use variabel
total_harga = lambda porsi, harga: porsi * harga
print('Total harga (lambda_1) gacoan :', total_harga(6, 12300))

# cara 2 : directly
print('Total harga (lambda_2) gacoan :', (lambda porsi, harga: porsi * harga)(6, 12300))