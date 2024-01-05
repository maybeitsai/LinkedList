import os

def clear():
    os.system('cls')

def print_algoritma(loc, locp, LinkedList, availList):
    print("\n\nAlgoritma: Del(Info, Link, Start, Avail, Loc, Locp)")
    if locp == 0:
        print(f"1. Jika {locp} = 0 --> T. ",
              f"\n\tStart := {LinkedList[loc - 1][1]}",
              "\n2. Exit")
    else:
        print(f"\n1. Jika {locp} = 0 --> F. ",
              f"\n\tLink[{locp}] := Link[{loc}]. *Menghapus simpul N",
              f"\n\tLink[{locp}] := {LinkedList[locp-1][1]}",
              "\n2. [Mengembalikan simpul terhapus kepada list AVAIl]",
              f"\n\tLink[{loc}] := {availList[1]}",
              f"\n\tAvail := {loc}",
               "\n3. Exit")

def split_list(start,nextPointer,value):
    valueAvail=[]
    nextPointerAvail=[]
    while start != 0 :
        valueAvail.append(value[start-1])
        nextPointerAvail.append(nextPointer[start-1])
        start = nextPointer[start-1]
    
    return valueAvail,nextPointerAvail

def display_list_nonavail(start,valueNonAvail,nextPointerNonAvail):
    print("\nLinked list : ")
    print(f"start |{start}|",end="")
    for index, value in enumerate(nextPointerNonAvail):
        print(f"---|{valueNonAvail[index]}|{value}|", end="")
    print()

def display_list_avail(nextPointerAvail):
    print("\nList avail:")
    for index, value in enumerate(nextPointerAvail):
        if value != 0 :
            print(f"|{value}|---|  ", end="")
    print("|0|\n")