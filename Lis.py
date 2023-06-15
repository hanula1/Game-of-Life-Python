from Zwierze import Zwierze
import random


class Lis(Zwierze):
    sila = 3
    inicjatywa = 7
    znak = 'L'
    nazwa = "Lis"

    def __init__(self, s):
        super().__init__(s)
        self.kolor = self.swiat.plansza.LIS

    def akcja(self):  # silniejszy wróg !!!
        moved = False
        tmp = self.polozenie
        self.czysc()

        while not moved:
            liczba = random.randint(0, 3)
            if liczba == 0:
                if tmp[0] + 1 < self.swiat.plansza.N:
                    self.polozenie=(tmp[0] + 1, tmp[1])
                    moved = True
            elif liczba == 1:
                if tmp[0] - 1 >= 0:
                    self.polozenie=(tmp[0] - 1, tmp[1])
                    moved = True
            elif liczba == 2:
                if tmp[1] - 1 >= 0:
                    self.polozenie=(tmp[0], tmp[1] - 1)
                    moved = True
            elif liczba == 3:
                if tmp[1] + 1 < self.swiat.plansza.N:
                    self.polozenie=(tmp[0], tmp[1] + 1)
                    moved = True

        self.poprzednie_polozenie = tmp

        self.rysowanie()

        self.wiek = self.wiek+1

        self.kolizja()

    def rozmnazanie(self):
        tmp = self.polozenie
        dziecko = Lis(self.swiat)
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