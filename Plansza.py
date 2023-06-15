import pygame
from Swiat import Swiat


class Plansza:
    TRAWA = (18, 196, 33)
    BARSZCZ = (211, 245, 213)
    GUARANA = (207, 98, 62)
    MLECZ = (240, 204, 62)
    JAGODY = (102, 5, 45)
    ANTYLOPA = (158, 99, 44)
    CYBER = (162, 235, 235)
    OWCA = (255, 255, 255)
    LIS = (247, 110, 5)
    WILK = (117, 117, 117)
    ZOLW = (1, 84, 26)
    CZLOWIEK = (235, 56, 187)

    win = pygame.display.set_mode((500, 500))

    def __init__(self, n):
        self.N = n
        pygame.init()
        self.rozmiar = 500 / self.N


    def wyswietl(self):
        # wyświetlanie okna gry
        pygame.display.set_caption("Symulacja Świata, Hanna Banasiak 193078")
        run = True
        # pętla główna
        while run:
            pygame.time.delay(50)

            # obsługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()
            ruch = False
            self.swiat.czlowiek.czysc()

            if keys[pygame.K_LEFT] and self.swiat.czlowiek.polozenie[0] - 1 >= 0:
                self.swiat.czlowiek.polozenie = (self.swiat.czlowiek.polozenie[0] - 1, self.swiat.czlowiek.polozenie[1])
                ruch = True
            if keys[pygame.K_RIGHT] and self.swiat.czlowiek.polozenie[0] + 1 < self.N:
                self.swiat.czlowiek.polozenie = (self.swiat.czlowiek.polozenie[0] + 1, self.swiat.czlowiek.polozenie[1])
                ruch = True
            if keys[pygame.K_UP] and self.swiat.czlowiek.polozenie[0] - 1 >= 0:
                self.swiat.czlowiek.polozenie = (self.swiat.czlowiek.polozenie[0], self.swiat.czlowiek.polozenie[1] - 1)
                ruch = True
            if keys[pygame.K_DOWN] and self.swiat.czlowiek.polozenie[0] + 1 < self.N:
                self.swiat.czlowiek.polozenie = (self.swiat.czlowiek.polozenie[0], self.swiat.czlowiek.polozenie[1] + 1)
                ruch = True
            if keys[pygame.K_SPACE]:
                self.swiat.czlowiek.kolizja()

            self.swiat.czlowiek.rysowanie()
            if ruch:
                self.swiat.wyjonajTure()