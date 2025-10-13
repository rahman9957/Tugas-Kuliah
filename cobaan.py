# Penjelasan tentang fungsi bubbleSort:
# Fungsi bubbleSort adalah algoritma pengurutan yang bekerja dengan cara membandingkan elemen-elemen yang berdekatan
# dalam sebuah list dan menukarnya jika mereka berada dalam urutan yang salah. Proses ini diulang hingga list menjadi terurut.

def bubbleSortWithExplanation(arr):
  n = len(arr)
  for i in range(n-1):
    print(f"Iterasi ke-{i+1}:")
    for j in range(n-i-1):
        print(f"  Membandingkan {arr[j]} dan {arr[j+1]}")
        if arr[j] > arr[j + 1]:
           print(f"  Menukar {arr[j]} dengan {arr[j+1]}")
           arr[j], arr[j + 1] = arr[j + 1], arr[j]
        else:
          print(f"  Tidak ada penukaran")
    print(f"List setelah iterasi ke-{i+1}: {arr}")
    print("Proses pengurutan selesai.")
    return arr
#contoh penggunaan fungsi dengan penjelasan
arr = [64, 34, 25, 12, 22, 11, 90]
print("\nList yang belum diurutkan:", arr)
bubbleSortWithExplanation(arr)
print("\nList hasil pengurutan:", arr)