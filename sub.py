# Kelas Dasar Pahlawanku
class Pahlawanku:
    def __init__(self, name, jenis, deskripsi):
        self.name = name
        self.jenis = jenis
        self.deskripsi = deskripsi

    def showInfo(self):
        print(f"Nama: {self.name}")
        print(f"Jenis: {self.jenis}")
        print(f"Deskripsi: {self.deskripsi}")
        print("=" * 70)

# Sub Class Revolusi
class Revolusi(Pahlawanku):
    def __init__(self, name=""):
        print("=" * 35, "Pahlawaku", "=" * 35)
        # Menggunakan SuperClass untuk pahlawanku dan Constructor
        super().__init__(name, "Revolusi", "Gugur Karena kebiadaban PKI.")
        super().showInfo()

# Sub Class Nasional
class Nasional(Pahlawanku):
    def __init__(self, name=""):
        super().__init__(name, "Nasional", "Panglima Perang Kemerdekaan.")
        super().showInfo()

# Sub Class Guru
class Guru(Pahlawanku):
    def __init__(self, name=""):
        super().__init__(name, "Pahlawan Tanpa Tanda Jasa", "Jasa Jasamu Sangat Berharga.")
        super().showInfo()

# Menciptakan New Objek Rev, Nas dan NN
Rev = Revolusi("Soekarno")
Nas = Nasional("Jenderal Sudirman")
NN = Guru("Ki Hajar Dewantara")

print("Hore Saya Berhasil Boss")
print("=" * 32, "S E L E S A I", "=" * 34)
