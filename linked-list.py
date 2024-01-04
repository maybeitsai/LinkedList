from tabulate import tabulate
import os

class Node:
    def __init__(self, value, next_pointer):
        self.value = value
        self.next_pointer = next_pointer

def clear():
    os.system('cls')

def delete_node(linked_list, index):
    deleted_node = linked_list.pop(index - 1)
    return deleted_node

def main():
    linked_list = []
    n = int(input("Masukkan jumlah simpul: "))

    for i in range(n):
        value = input(f"Masukkan nilai simpul ke-{i+1}: ")
        next_pointer = input(f"Masukkan next pointer untuk simpul ke-{i+1}: ")

        node = Node(value, next_pointer)
        linked_list.append(node)

    clear()

    header = ["Value", "Next Pointer"]
    table_data = [[node.value, node.next_pointer] for node in linked_list]
    table = tabulate(table_data, header, tablefmt="pretty")

    print(table + '\n')

    start = int(input("start: "))
    avail = int(input("avail: "))
    print("\n-----------------------------\n")

    index_start = start
    index_avail = avail

    info_link = []

    for _ in range(n):
        info = linked_list[index_start - 1].value
        link = linked_list[index_start - 1].next_pointer
        info_link.append([info, link])

        if not link or link == "0":
            break

        index_start = int(link)

    avail_list = []

    for _ in range(n):
        avail_list.append(index_avail)

        if not linked_list[index_avail - 1].next_pointer or linked_list[index_avail - 1].next_pointer == "0":
            break

        index_avail = int(linked_list[index_avail - 1].next_pointer)

    print("Linked list:")
    print(f"start |{start}|", end="")
    
    for info, link in info_link:
        print(f"---|{info}|{link}|", end="")
    print("")

    print("\nList avail:")
    for avail in avail_list:
        print(f"|{avail}|---|  ", end="")
    print("|0|")

    print("\n-----------------------------\n")
   # Delete a node
    delete_index = int(input("Masukkan indeks simpul yang akan dihapus: "))
    deleted_node = delete_node(linked_list, delete_index)

    # Move the deleted node's information into avail list
    avail_list.reverse()
    avail_list.append(delete_index)
    avail_list.reverse()
    avail_index = avail_list[-1]

    # Set the avail pointer in the deleted node
    deleted_node.next_pointer = str(avail_index)

    # Insert the deleted node into the avail list
    linked_list.insert(avail_index - 1, deleted_node)

    print("Linked list:")
    print(f"start |{start}|", end="")
    
    for info, link in info_link:
        print(f"---|{info}|{link}|", end="")
    print("")

    print("\nList avail:")
    for avail in avail_list:
        print(f"|{avail}|---|  ", end="")
    print("|0|")

main()