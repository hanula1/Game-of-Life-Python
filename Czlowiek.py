from Zwierze import Zwierze
import copy


class Czlowiek(Zwierze):
    sila = 5
    inicjatywa = 4
    znak = '&'
    nazwa = "Czlowiek"
    umiejetnosc = 0

    def __init__(self, s):
        super().__init__(s)
        self.kolor = self.swiat.plansza.CZLOWIEK

    def akcja(self):
        if self.umiejetnosc == 5:
            self.umiejetnosc = -5
        elif self.umiejetnosc != 0 and self.umiejetnosc < 5:
            self.umiejetnosc += 1
            if self.umiejetnosc > 0:
                self.um()

    def kolizja(self):
        if self.umiejetnosc == 0:
            self.um()
            self.umiejetnosc += 1
            print("umiejetnosc")
        elif self.umiejetnosc > 0:
            print("umiejetnosc trwa")
        elif self.umiejetnosc < 0:
            print("umiejetnosc niedostepna")

    def um(self):
        for i in self.swiat.organizmy:
            for j in range(-1, 1):
                for k in range(-1, 1):
                    tempo = (self.polozenie[0] + j, self.polozenie[1] + k)
                    if (k == 0 and j == 0) or tempo[0] >= self.swiat.plansza.N or tempo[0] < 0 or \
                            tempo[1] >= self.swiat.plansza.N or tempo[1] < 0:
                        continue
                    if i.polozenie == tempo:
                        i.akcja()

