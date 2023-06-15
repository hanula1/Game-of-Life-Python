from Zwierze import Zwierze
import random, copy


class Zolw(Zwierze):
    sila = 2
    inicjatywa = 1
    znak = 'Z'
    nazwa = "Zolw"

    def __init__(self, s):
        super().__init__(s)
        self.kolor = self.swiat.plansza.ZOLW

    def akcja(self):
        liczba = random.randint(0, 3)
        if liczba == 0:
            super().akcja()

    def rozmnazanie(self):
        tmp = copy.copy(self.polozenie)
        dziecko = Zolw(self.swiat)
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