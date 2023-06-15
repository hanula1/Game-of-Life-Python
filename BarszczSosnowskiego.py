from Roslina import Roslina
from Zwierze import Zwierze
import random, copy


class BarszczSosnowskiego (Roslina):
    sila = 10
    znak = 'b'
    nazwa = "Barszcz Sosnowskiego"

    def __init__(self, s):
        super().__init__(s)
        self.kolor = self.swiat.plansza.BARSZCZ

    def akcja(self):
        self.wiek = self.wiek + 1
        super().kolizja()

        tmp = copy.copy(self.polozenie)

        for i in self.swiat.organizmy:
            for j in range(-1, 1):
                for k in range(-1, 1):
                    tempo = (tmp[0] + j, tmp[1] + k)
                    if (k == 0 and j == 0) or tempo[0] >= self.swiat.plansza.N or tempo[0] < 0 or \
                            tempo[1] >= self.swiat.plansza.N or tempo[1] < 0:
                        continue
                    if i.polozenie == tempo:
                        self.swiat.organizmy.pop(self.swiat.organizmy.index(i))

        for i in range(-1, 1):
            for j in range(-1, 1):
                tempo = (self.polozenie[0] + i, self.polozenie[1] + j)
                if (i == 0 and j == 0) or tempo[0] >= self.swiat.plansza.N or tempo[0] < 0 or \
                        tempo[1] >= self.swiat.plansza.N or tempo[1] < 0:
                    continue
                for k in self.swiat.organizmy:
                    if k.polozenie == tempo and isinstance(k, Zwierze):
                        pow = '\n' + "Zwierze " + k.nazwa + " zostala zabita przez " + self.nazwa
                        self.swiat.powiadomienia.append(pow)
                        self.swiat.organizmy.pop(self.swiat.organizmy.index(k))

        rozsianie = random.randint(0, 10)
        if rozsianie == 1:
            self.rozmnazanie()

    def rozmnazanie(self):
        tmp = copy.copy(self.polozenie)
        dziecko = BarszczSosnowskiego(self.swiat)
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