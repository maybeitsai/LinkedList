from tabulate import tabulate
from module import *
import sys

clear()

# Membuat list kosong untuk menyimpan nilai dan next pointer
value = []
nextPointer = []
LinkedList = []

# Mengambil input jumlah simpul dari pengguna
summary = int(input("Masukkan jumlah simpul: "))

# Mengisi nilai dan next pointer untuk setiap simpul
for index in range(1, summary+1):
    nilai = input(f"Masukkan nilai simpul ke-{index}: ")
    link = int(input(f"Masukkan next pointer untuk simpul ke-{index}: "))
    
    # Tambahkan data ke list
    value.append(nilai)
    nextPointer.append(link)
    LinkedList.append([index, nilai, link])

clear()

# Menampilkan tabel dengan menggunakan library tabulate
print(tabulate(LinkedList, ["Index","Value", "Next Pointer"], tablefmt="pretty"))

# Mengambil input nilai start dan avail
start = int(input("start: "))
avail = int(input("avail: "))

# Memisahkan linked list menjadi list non avail dan list avail
valueNonAvail, nextPointerNonAvail = split_linked_list(start, nextPointer, value)
valueAvail, nextPointerAvail = split_linked_list(avail, nextPointer, value)

# Menambahkan nilai start pada indeks pertama pada list avail
nextPointerAvail.insert(0, avail)

# Menampilkan list non avail dan list avail
display_linked_list(start, valueNonAvail, nextPointerNonAvail)
display_avail_list(nextPointerAvail)

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
while True:
    while True:
        loc = int(input("Delete indeks : "))

        if loc != 0 and loc != start:
            for index in range(0,len(nextPointer)):
                if nextPointer[index] == loc:
                    locp = index+1
            valueNonAvail.remove(value[loc-1])
            nextPointerNonAvail.remove(loc)
            nextPointer[locp-1]=nextPointer[loc-1]
            nextPointer[loc-1]=avail
            LinkedList[loc-1][1] = ""
            break

        elif loc == start:
            locp=0
            start = nextPointerNonAvail[0]
            nextPointerNonAvail.pop(0)
            valueNonAvail.pop(0)
            nextPointer[loc-1]=avail
            LinkedList[loc-1][1] = ""
            break

    print("========================================================")

    # Memasukkan indeks yang dihapus kedalam avail
    nextPointerAvail.insert(0, loc)

    # Menampilkan list non avail dan list avail
    display_linked_list(start, valueNonAvail, nextPointerNonAvail)
    display_avail_list(nextPointerAvail)

    # menampilkan algoritma
    print_algoritma(start, loc, locp, nextPointer, nextPointerAvail)

    print("========================================================")
    
    while True:
        askForDeleteAgain = input("Apakah anda ingin menghapus simpul lagi (Y/N): ")
        if askForDeleteAgain.upper() == "N":
            print("Bye!")
            sys.exit()
        elif askForDeleteAgain.upper() == "Y":
            break

    if start == 0:
        print("Linked list sudah kosong")
        print("Underflow!")
        print("Bye!")
        sys.exit()
    
