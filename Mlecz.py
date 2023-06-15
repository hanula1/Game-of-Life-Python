from Roslina import Roslina
import random
import copy


class Mlecz(Roslina):
    znak = 'm'
    nazwa = "Mlecz"

    def __init__(self, s):
        super().__init__(s)
        self.kolor = self.swiat.plansza.MLECZ

    def akcja(self):
        self.wiek = self.wiek + 1
        self.kolizja()
        for i in range(3):
            rozsianie = random.randint(0, 10)
            if rozsianie == 1:
                self.rozmnazanie()

    def rozmnazanie(self):
        tmp = copy.copy(self.polozenie)
        dziecko = Mlecz(self.swiat)
        success = False

        if self.swiat.pustePole(tmp[0] + 1, tmp[1]):
            dziecko.polozenie = (tmp[0] + 1, tmp[1])
            success = True
        elif self.swiat.pustePole(tmp[0] - 1, tmp[1]):
            dziecko.polozenie = (tmp[0] - 1, tmp[1])
            success = True
        elif self.swiat.pustePole(tmp[0], tmp[1] + 1):
            dziecko.polozenie = (tmp[0], tmp[1] + 1)
            success = True
        elif self.swiat.pustePole(tmp[0], tmp[1] - 1):
            dziecko.polozenie = (tmp[0], tmp[1] - 1)
            success = True

        if success:
            dziecko.rysowanie()
            self.swiat.organizmy.append(dziecko)