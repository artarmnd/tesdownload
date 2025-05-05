class Mamalia(object):
    def __init__(self, Nama_Hewan):
        self.Nama_Hewan = Nama_Hewan
        
        print(Nama_Hewan, 'Adalah hewan berdarah panas.')
        
    def show(self):
        print('Nama Hewan:', self.Nama_Hewan)

class Harimau(Mamalia):
    def __init__(self):
        print('Harimau adalah hewan berkaki 4.')
        super().__init__('Harimau')
        # super().showinfo()
m1 = Harimau()

class Sea():
    def __init__(self, Laut):
        print(Laut, 'Adalah hewan berdarah dingin.')

class Lumba2(Sea):
    def __init__(self):
        print('Lumba-lumba adalah hewan yang hidup dilaut.')
        super().__init__('Lumba-lumba')
m2 = Lumba2()