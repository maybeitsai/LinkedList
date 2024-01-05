from tabulate import tabulate
from module import *
import sys

clear()
value = []
nextPointer = []
LinkedList = []
index=[]
summary = int(input("Masukkan jumlah simpul: "))

for index in range(1,summary+1):
    nilai = input(f"Masukkan nilai simpul ke-{index}: ")
    link = int(input(f"Masukkan next pointer untuk simpul ke-{index}: "))
    # Tambahkan data ke list
    value.append(nilai)
    nextPointer.append(link)
    LinkedList.append([index, nilai, link])

clear()
# Menampilkan Tabel
print(tabulate(LinkedList, ["Index","Value", "Next Pointer"], tablefmt="pretty"))

start = int(input("start: "))
avail = int(input("avail: "))
valueNonAvail,nextPointerNonAvail = split_list(start,nextPointer,value)
valueAvail,nextPointerAvail = split_list(avail,nextPointer,value)

# Menambahkan nilai start pada indeks pertama
nextPointerAvail.insert(0,avail)

# Menampilkan list non avail
display_list_nonavail(start,valueNonAvail,nextPointerNonAvail)

# Menampilkan list avail
display_list_avail(nextPointerAvail)

# Algoritma Delete
print("========================================================")
while True:
    askForDelete = input("Apakah anda ingin menghapus simpul (Y/N): ")
    if askForDelete.upper() == "N":
        print("Bye!")
        sys.exit()
    elif askForDelete.upper() == "Y":
        break
    print("Silahkan masukkan ulang")

while True :
    loc = int(input("Delete indeks: "))
    if loc != 0 and loc != start :
        valueNonAvail.remove(value[loc-1])
        nextPointerNonAvail.remove(loc)
        break

    elif loc == start:
        start = nextPointerNonAvail[0]
        nextPointerNonAvail.pop(0)
        valueNonAvail.pop(0)
        break

    print('Underflow!') 
print("========================================================")

# Memasukkan kedalam avail
nextPointerAvail.insert(0,loc)

# Menampilkan list non avail
display_list_nonavail(start,valueNonAvail,nextPointerNonAvail)

# Menampilkan list avail
display_list_avail(nextPointerAvail)