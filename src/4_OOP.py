class Auto:
    def __init__(self, kolor, kondycja, wiek=0):
        self.kolor = kolor
        self.ilosc_paliwa = 10
        self.kondycja = kondycja
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.rocznik = 2024 - wiek

    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        return round(zasieg)

    def ustaw_tryb(self, tryb):
        if tryb == 'eco':
            self.tryb_ekonomiczny = True
            self.spalanie_na_100 = 10
        elif tryb == 'normal':
            self.tryb_ekonomiczny = False
            self.spalanie_na_100 = 14
        else:
            print('bez zmian')

    def __str__(self):
        napis = f'Auto ma kolor {self.kolor} i jest rocznik {self.rocznik + 3}'
        return napis

auto1 = Auto('white', 5, 12)
print(auto1.kolor)
print(auto1.ilosc_paliwa)
auto1.ilosc_paliwa -= 30
auto1.ustaw_tryb('eco')
print(auto1.ilosc_paliwa)
print(auto1)