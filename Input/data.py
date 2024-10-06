# meminta input jumlah mahasiswa
jml = int(input("Masukan jumlah mahasiswa :"))

# membuat list kosong untuk menampung data mahasiswa
data_mahasiswa = []

# looping untuk setiap mahasiswa
for i in range(jml):

    # menampilkan pesan data "mahasiswa ke"
    print("data mahasiswa ->",i+1)

    # mengambil input dari user
    nama = input("Masukan nama :")
    umur = int(input("Masukan umur :"))
    jk   = input("Masukan jenis kelamin :")

    # menambahkan data mahasiswa ke dalam list data_mahasiswa  
    data_mahasiswa.append({"nama":nama, "umur":umur, "jk": jk})

# menampilkan tabel
print("-"*70)
print(f"{'NAMA':<35} {'UMUR':<20} {'JENIS KELAMIN':<15}")
print("-"*70)

# menampilkan data mahasiswa
for i in data_mahasiswa:
    print(f"{i['nama']:<35} {i['umur']:<20} {i['jk']:<15}")

# menampilkan garis bawah
print("-"*70)