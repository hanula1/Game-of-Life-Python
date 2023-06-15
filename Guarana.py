from Roslina import Roslina
from Zwierze import Zwierze
import copy


class Guarana(Roslina):
    znak = 'g'
    nazwa = "Guarana"

    def __init__(self, s):
        super().__init__(s)
        self.kolor = self.swiat.plansza.GUARANA

    def rozmnazanie(self):
        tmp = copy.copy(self.polozenie)
        dziecko = Guarana(self.swiat)
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

    def kolizja(self):
        t = 0
        tmp = self.polozenie

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
                    self.swiat.organizmy[i].sila += 1
                    # wyswietlanie
                    self.swiat.organizmy.pop(t)
                    break
