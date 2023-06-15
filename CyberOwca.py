from Owca import Owca
from BarszczSosnowskiego import BarszczSosnowskiego
import copy


class CyberOwca(Owca):
    sila = 11
    inicjatywa = 4
    znak = 'C'
    nazwa = "CyberOwca"

    def __init__(self, s):
        super().__init__(s)
        self.kolor = self.swiat.plansza.CYBER

    def akcja(self):
        barszcz = False

        for i in self.swiat.organizmy:
            if isinstance(i, BarszczSosnowskiego):
                barszcz = True
                break

        if barszcz:
            self.szukaj_barszczu()
            tmp_a = copy.copy(self.polozenie[0])
            tmp_b = copy.copy(self.polozenie[1])
            if self.trasa[0] > self.trasa[1]:
                if self.kierunek[0]:
                    tmp_a -= 1
                else:
                    tmp_a += 1
            else:
                if self.kierunek[1]:
                    tmp_b -= 1
                else:
                    tmp_b += 1
            self.czysc()
            self.polozenie = (tmp_a, tmp_b)
            self.rysowanie()
            self.kolizja()
        else:
            super().akcja()

    def szukaj_barszczu(self):
        trasa = (self.swiat.plansza.N, self.swiat.plansza.N)
        for i in self.swiat.organizmy:
            if isinstance(i, BarszczSosnowskiego):
                if(i.polozenie[0]>self.polozenie[0]):
                    a = i.polozenie[0]-self.polozenie[0]
                    k1 = False
                else:
                    a = self.polozenie[0] - i.polozenie[0]
                    k1 = True

                if (i.polozenie[1] > self.polozenie[1]):
                    b = i.polozenie[1] - self.polozenie[1]
                    k2 = False
                else:
                    b = self.polozenie[1] - i.polozenie[1]
                    k2 = True
                c = a + b
                d = trasa[0] + trasa[1]
                if c < d:
                    self.trasa = (a,b)
                    self.kierunek = (k1, k2)



    def kolizja(self):
        pass

    # def rozmnazanie(self):
    #     tmp = copy.copy(self.polozenie)
    #     dziecko = CyberOwca(self.swiat)
    #     success = False
    #
    #     if self.swiat.pustePole(tmp[0] + 1, tmp[1]):
    #         dziecko.polozenie = (tmp[0] + 1, tmp[1])
    #         success = True
    #     elif self.swiat.pustePole(tmp[0] - 1, tmp[1]):
    #         dziecko.polozenie = (tmp[0] - 1, tmp[1])
    #         success = True
    #     elif self.swiat.pustePole(tmp[0], tmp[1] + 1):
    #         dziecko.polozenie = (tmp[0], tmp[1] + 1)
    #         success = True
    #     elif self.swiat.pustePole(tmp[0], tmp[1] - 1):
    #         dziecko.polozenie = (tmp[0], tmp[1] - 1)
    #         success = True
    #
    #     if success:
    #         dziecko.rysowanie()
    #         self.swiat.organizmy.append(dziecko)
