class Rumah:
    # Instance attribute
    def __init__(self, bahan, harga, lokasi, model):
        # self adalah instance dari class
        self.bahan = bahan
        self.harga = harga
        self.lokasi = lokasi
        self.model = model

    def show(self):
        print("Bahan Bangunan: ", self.bahan, ", Harga: ", self.harga)

    def gaya(self):
        print("Rumah Idamanku: ", self.model, "Dan Lokasinya: ", self.lokasi)

# Membuat objek
rumah1 = Rumah("Kayu", 700000000, "Pedesaan", "Britania Klasik")
rumah2 = Rumah("Beton", 1500000000, "Perkotaan", "Klasik Modern")

# Menampilkan informasi rumah1
rumah1.show()
rumah1.gaya()
print("=" * 60)

# Menampilkan informasi rumah2
rumah2.show()
rumah2.gaya()