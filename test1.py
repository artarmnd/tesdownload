class data:
    def __init__(self, nama, kelamin, pekerjaan):

# data members (instance variabels)
        self.nama = nama
        self.kelamin = kelamin
        self.pekerjaan = pekerjaan

# behavior (instance methods)
    def show(self):
        print('nama :', self.nama, 'kelamin :', self.kelamin, 'pekerjaan :', self.pekerjaan)

# behavior (instance methods)
    def work(self):
        print(self.nama, 'is working as a', self.pekerjaan)

# create object of a class
nama = input("masukkan nama : ")
kelamin = input("masukkan kelamin : ")
pekerjaan = input("masukkan pekerjaan : ")

jessa = data(nama, kelamin, pekerjaan)

# call methods
print("=" * 50)
jessa.show()
print("=" * 50)
jessa.show()