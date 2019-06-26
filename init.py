class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
raman = Enemy(29)

jason.get_energy()
raman.get_energy()