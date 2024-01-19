import os

def clear():
    # Fungsi ini menghapus layar konsol
    os.system('cls')

def print_algoritma(start, loc, locp, nextPointer, availList):
    # Fungsi ini mencetak algoritma dengan parameter yang diberikan
    print("\nAlgoritma: Del(Info, Link, Start, Avail, Loc, Locp)")
    if locp == 0:
        # Jika locp adalah 0, maka lakukan langkah berikut
        print(f"1. Jika {locp} = 0 --> T. ",
              f"\n\tStart := {start}",
              f"\n\tAvail := {loc}",
              "\n2. Keluar\n")
    else:
        # Jika locp bukan 0, maka lakukan langkah berikut
        print(f"\n1. Jika {locp} = 0 --> F. ",
              f"\n\tLink[{locp}] := Link[{loc}]. *Menghapus simpul N",
              f"\n\tLink[{locp}] := {nextPointer[locp - 1]}",
              "\n2. [Mengembalikan simpul terhapus kepada list avail]",
              f"\n\tLink[{loc}] := {availList[1]}",
              f"\n\tAvail := {loc}",
              "\n3. Keluar\n")

def split_linked_list(start,nextPointer,value):
    # Fungsi ini memisahkan linked list dan mengembalikan nilai-nilai list dan next pointer
    listValue=[]
    nextPointerAvail=[]
    while start != 0 :
        listValue.append(value[start-1])
        nextPointerAvail.append(nextPointer[start-1])
        start = nextPointer[start-1]
    
    return listValue,nextPointerAvail

def display_linked_list(start,valueNonAvail,nextPointerNonAvail):
    # Fungsi ini menampilkan linked list
    print("\nLinked list : ")
    print(f"start |{start}|",end="")
    for index, value in enumerate(nextPointerNonAvail):
        print(f"---|{valueNonAvail[index]}|{value}|", end="")
    print()

def display_avail_list(nextPointerAvail):
    # Fungsi ini menampilkan daftar yang tersedia
    print("\nList avail:")
    for index, value in enumerate(nextPointerAvail):
        if value != 0 :
            print(f"|{value}|---|  ", end="")
    print("|0|\n")