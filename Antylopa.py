from Zwierze import Zwierze
import random, copy


class Antylopa(Zwierze):

    sila = 4
    inicjatywa = 4
    znak = 'A'
    nazwa = "Antylopa"

    def __init__(self, s):
        super().__init__(s)
        self.kolor = self.swiat.plansza.ANTYLOPA

    def akcja(self):
        moved = False
        tmp = copy.copy(self.polozenie)
        self.czysc()

        while not moved:
            liczba = random.randint(0, 3)
            if liczba == 0:
                if tmp[0] + 2 < self.swiat.plansza.N:
                    self.polozenie = (tmp[0] + 2, tmp[1])
                    moved = True
            elif liczba == 1:
                if tmp[0] - 2 >= 0:
                    self.polozenie = (tmp[0] - 2, tmp[1])
                    moved = True
            elif liczba == 2:
                if tmp[1] - 2 >= 0:
                    self.polozenie = (tmp[0], tmp[1] - 2)
                    moved = True
            elif liczba == 3:
                if tmp[1] + 2 < self.swiat.plansza.N:
                    self.polozenie = (tmp[0], tmp[1] + 2)
                    moved = True

        self.poprzednie_polozenie = tmp
        self.rysowanie()
        self.wiek = self.wiek + 1
        super().kolizja()

    def rozmnazanie(self):
        tmp = copy.copy(self.polozenie)
        dziecko = Antylopa(self.swiat)
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
