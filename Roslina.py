from Zwierze import Zwierze
import random, copy
from Organizm import Organizm


class Roslina(Organizm):
    def __init__(self,s):
        super().__init__(s)

    def akcja(self):
        self.wiek = self.wiek + 1
        self.kolizja()
        rozsianie = random.randint(0, 10)
        if rozsianie == 1:
            self.rozmnazanie()

    def kolizja(self):
        t = 0
        tmp = copy.copy(self.polozenie)

        for i in range(len(self.swiat.organizmy)):
            if self.swiat.organizmy[i] == self:
                t = i

        for i in range(len(self.swiat.organizmy)):
            if self.swiat.organizmy[i] == self:
                continue

            if self.swiat.organizmy[i].polozenie == tmp:
                if isinstance(self.swiat.organizmy[i], Zwierze):
                    pow = "\nRoslina " + self.nazwa + " zostala zjedzona przez zwierze " + self.swiat.organizmy[i].nazwa
                    self.swiat.powiadomienia.append(pow)
                    #wyswietlanie
                    self.swiat.organizmy.pop(t)
                    break
