from Organizm import Organizm
import random
import copy
# from Zolw import Zolw


class Zwierze (Organizm):
    def __init__(self, s):
        super().__init__(s)

    def akcja(self):
        moved = False
        tmp = copy.copy(self.polozenie)
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

    def kolizja(self):
        tmp = copy.copy(self.polozenie)

        t = 0
        for i in range(len(self.swiat.organizmy)):
            if self.swiat.organizmy[i] == self:
                t = i

        for i in range(len(self.swiat.organizmy)):
            if self.swiat.organizmy[i] == self:
                continue
            if self.swiat.organizmy[i].polozenie == tmp:
                if self.znak == self.swiat.organizmy[i].znak:
                    self.rozmnazanie()
                    break
                # elif isinstance(self.swiat.organizmy[i], Zolw):
                #     if self.sila < 5:
                #         tmp_point = self.polozenie
                #         self.polozenie = self.poprzednie_polozenie
                #         self.poprzednie_polozenie = tmp_point
                #         #zmiana na planszy
                #         break
                #     else:
                #         pow = '\nZginelo zwierze: Zolw'
                #         self.swiat.powiadomienia.append(pow)
                #         # wyswietl
                #         self.swiat.organizmy.pop(i)
                #         break
                elif isinstance(self.swiat.organizmy[i], Zwierze):
                    if self.swiat.organizmy[i].sila > self.sila:
                        pow = '\nZwierze ' + self.nazwa + ' zostalo zabite przez ' + self.swiat.organizmy[i].nazwa
                        self.swiat.powiadomienia.append(pow)
                        self.swiat.organizmy[i].rysowanie()
                        self.swiat.organizmy.pop(t)  # this
                        break
                    else:
                        pow = '\nZwierze ' + self.swiat.organizmy[i].nazwa + ' zostalo zabite przez ' + self.nazwa
                        self.swiat.powiadomienia.append(pow)
                        self.rysowanie()
                        self.swiat.organizmy.pop(i)  # przeciwnik
                        break

