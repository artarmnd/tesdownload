class siswa:
    # class variables
    sekolah = 'SMP Negeri 5 kota jambi'
    sekolah2 = 'SD Negeri 41 kota jambi'

    # constructor
    def __init__(self, nama, usia, alamat):
        # instance variables
        self.nama = nama
        self.usia = usia
        self.alamat = alamat


# input from user
nama_input = input("Masukkan nama siswa: ")
usia_input = int(input("Masukkan usia siswa: "))
alamat_input = input("Masukkan alamat siswa: ")

s1 = siswa(nama_input, usia_input, alamat_input)

print("=" * 20, "Data Sekolah", "=" * 20)
# access instance variables
print('Nama Siswa :', s1.nama, "Umur Anak :", s1.usia, "dan Alamat : ", s1.alamat)
# access class variable
print('Nama Sekolah :', siswa.sekolah2)
print("=" * 25, "Data Sekolah ", "=" * 25)

# Modify instance variables
s1.nama = 'nazriel irham'
s1.usia = 43
s1.alamat = "Talang Banjar - Jambi"
print('Nama siswa :', s1.nama, " dan umur anak : ", s1.usia)
# access class variable
print('Nama sekolah :', siswa.sekolah)
