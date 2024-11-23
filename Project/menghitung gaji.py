'''
fungsi untuk menghitung gaji karyawan

Diketahui
gaji pokok : 300000
golongan: jabatan karyawan (1: 5% , 2: 10% , 3: 15%)
pendidikan: tingkat pendidikan karyawan (SMA : 2.5%, D1: 5%, D3: 20%, S1 : 30%)

Logika nya : 
    - jika seorang karyawan tsb dengan golongan 3, maka mendapatkan tunjangan 15% * 300000
    - jika seorang karyawan tsb dengan pendidikan S1, maka mendapatkan tunjangan 30% * 300000

Honor Lembur : 
    Jumlah jam kerja normal sebanyak 8 jam, 
    honor lembur diberikan jika jumlah jam kerja lebih dari 8 jam,
    maka kelebihan jam kerja tsb di kalikan dengan Rp. 3500 untuk setiap kelebihan jam kerja karyawan tsb.
'''
def hitung_gaji(nama, golongan, pendidikan, jam_kerja):

# Gaji pokok karyawan
    gaji_pokok = 300000

# Tunjangan jabatan berdasarkan golongan
    tunjangan_jabatan = {1: 0.05, 2: 0.1, 3: 0.15}

# Tunjangan pendidikan berdasarkan tingkat pendidikan
    tunjangan_pendidikan = {'SMA': 0.025, 'D1': 0.05, 'D3': 0.2, 'S1': 0.3}

# Proses menghitung tunjangan berdasarkan jabatan dan pendidikan
    tunjangan_jabatan_rupiah = gaji_pokok * tunjangan_jabatan[golongan]
    tunjangan_pendidikan_rupiah = gaji_pokok * tunjangan_pendidikan[pendidikan]

# Menghitung honor lembur
    jam_lembur = max(jam_kerja -8,0)
    honor_lembur = jam_lembur * 3500

#Menghitung total gaji
    total_gaji = gaji_pokok + tunjangan_jabatan_rupiah + tunjangan_pendidikan_rupiah + honor_lembur

# hasil
    return {
        'nama': nama,
        'tunjangan_jabatan': tunjangan_jabatan_rupiah,
        'tunjangan_pendidikan': tunjangan_pendidikan_rupiah,
        'honor_lembur': honor_lembur,
        'total_gaji': total_gaji
    }

# Input data karyawan 
print("|==============================================================|")
print("|             Program Menghitung Gaji Karyawan                 |")
print("|==============================================================|")
nama = input("Masukan Nama Karyawan : ")
golongan = int(input("Golongan Jabatan:"))
pendidikan = input("Tingkat Pendidikan : ")
jam_kerja = int(input("Jumlah Jam Kerja : "))

# Menghitung dan menampilkan hasil
hasil = hitung_gaji(nama, golongan, pendidikan, jam_kerja)
print()
print("|==============================================================|")
print("|             Program Menghitung Gaji Karyawan                 |")
print("|==============================================================|")
print()
print("  Nama Karyawan        : ", hasil['nama'])
print()
print("|==============================================================|")
print("|                    Honor Yang Diterima                       |")
print("|==============================================================|")
print()
print("  Tunjangan Jabatan    : Rp.", hasil['tunjangan_jabatan'])
print("  Tunjangan Pendidikan : Rp.", hasil['tunjangan_pendidikan'])
print("  Honor Lembur         : Rp.", hasil['honor_lembur'])
print("  Total Gaji           : Rp.", hasil['total_gaji'])
