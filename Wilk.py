from Zwierze import Zwierze
import copy

class Wilk (Zwierze):
    sila = 9
    inicjatywa = 5
    znak = 'W'
    nazwa = "Wilk"

    def __init__(self, s):
        super().__init__(s)
        self.kolor = self.swiat.plansza.WILK

    def rozmnazanie(self):
        tmp = copy.copy(self.polozenie)
        dziecko = Wilk(self.swiat)
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