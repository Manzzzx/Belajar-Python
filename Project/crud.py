import os

def list_mahasiswa(list_mhs):
    for i, mhs in enumerate(list_mhs, start=1):
        print(f"Mahasiswa ke-{i} = {mhs}")
def delete_mahasiswa(list_mhs, index):
    list_mhs.pop(index)

def edit_mahasiswa(list_mhs, index):
    mahasiswa = str(input("Mahasiswa : "))
    list_mhs[index] = mahasiswa

def create_mahasiswa(list_mhs):
    mahasiswa = str(input("Mahasiswa Baru : "))
    list_mhs.append(mahasiswa)

def print_menu():
    print("\n\n\n")
    print("Pilih Command :")
    print("c (Create Mahasiswa)")
    print("d (Delete Mahasiswa)")
    print("e (Edit Mahasiswa)")
    print("q (Quit Program)")


mahasiswa = []
while True:
    print_menu()
    command = str(input("Masukan Command : "))
    if command == "q":
        break
    elif command == "c":
        create_mahasiswa(mahasiswa)
        os.system("clear")
        list_mahasiswa(mahasiswa)
    elif command == "d":
        index = int(input("Masukan Index : "))
        delete_mahasiswa(mahasiswa, index)
        os.system("clear")
        list_mahasiswa(mahasiswa)
    elif command == "e":
        index = int(input("Masukan nomor : "))
        edit_mahasiswa(mahasiswa, index)
        os.system("clear")
        list_mahasiswa(mahasiswa)
    else:
        print("Command Tidak Valid")