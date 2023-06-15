import random
from Antylopa import Antylopa
from CyberOwca import CyberOwca
from Lis import Lis
from Owca import Owca
from Zolw import Zolw
from Wilk import Wilk
from BarszczSosnowskiego import BarszczSosnowskiego
from Guarana import Guarana
from Mlecz import Mlecz
from Trawa import Trawa
from WilczeJagody import WilczeJagody
from Czlowiek import Czlowiek


class Swiat:
    def __init__(self, plansza):
        self.organizmy = []
        self.powiadomienia = []
        self.plansza = plansza
        plansza.swiat = self
        self.czlowiek = Czlowiek(self)
        self.losujDrop()
        self.plansza.wyswietl()


    def wyjonajTure(self):
        self.czyscPowiadomienia()

        # Sortowanie po ini i wieku

        for organizm in self.organizmy:
            if organizm.wiek == 0:
                organizm.wiek = 1
            else:
                organizm.akcja()

        self.rysujPowiadomienia()

    def rysujSwiat(self):
        pass
        # Implementation of rysujSwiat in Python

    def pustePole(self, x, y):
        if x >= self.plansza.N or x < 0 or y >= self.plansza.N or y < 0:
            return False

        for i in range(len(self.organizmy)):
            if self.organizmy[i].polozenie[0] == x and self.organizmy[i].polozenie[1] == y:
                return False

        return True

    def rysujPowiadomienia(self):
        for i in self.powiadomienia:
            print(i)
        print('\n')

    def czyscPowiadomienia(self):
        self.powiadomienia = []

    def losujDrop(self):
        for i in range(self.plansza.N):
            liczba = random.randint(0, 10)
            if liczba == 0:
                self.organizmy.append(Antylopa(self))
            elif liczba == 1:
                self.organizmy.append(Lis(self))
            elif liczba == 2:
                self.organizmy.append(Owca(self))
            elif liczba == 3:
                self.organizmy.append(Wilk(self))
            elif liczba == 4:
                self.organizmy.append(Zolw(self))
            elif liczba == 5:
                self.organizmy.append(BarszczSosnowskiego(self))
            elif liczba == 6:
                self.organizmy.append(Guarana(self))
            elif liczba == 7:
                self.organizmy.append(Mlecz(self))
            elif liczba == 8:
                self.organizmy.append(Trawa(self))
            elif liczba == 9:
                self.organizmy.append(WilczeJagody(self))
            elif liczba == 10:
                self.organizmy.append(CyberOwca(self))

        self.organizmy.append(self.czlowiek)

        for i in self.organizmy:
            i.rysowanie()
