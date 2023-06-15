from abc import ABC, abstractmethod
import pygame
import random


class Organizm (ABC):
    sila = 0
    inicjatywa = 0
    poprzednie_polozenie = (0, 0)
    wiek = 0
    nazwa = "organizm"
    znak = '*'

    def __init__(self, s):
        self.swiat = s
        liczba1 = random.randint(0, self.swiat.plansza.N-1)
        liczba2 = random.randint(0, self.swiat.plansza.N-1)
        self.polozenie = (liczba1, liczba2)
        self.powstanie()
        self.win = self.swiat.plansza.win
        self.rozmiar = self.swiat.plansza.rozmiar

    def akcja(self):
        pass  # Implement the desired behavior for akcja()

    def kolizja(self):
        pass  # Implement the desired behavior for kolizja()

    def rysowanie(self):
        # self.kolor = self.swiat.plansza.ANTYLOPA
        pygame.draw.rect(self.win, self.kolor, (self.polozenie[0] * self.rozmiar,
                                                self.polozenie[1] * self.rozmiar, self.rozmiar, self.rozmiar))
        pygame.display.update()

    def czysc(self):
        pygame.draw.rect(self.win, (000, 000, 000), (self.polozenie[0] * self.rozmiar,
                                               self.polozenie[1] * self.rozmiar, self.rozmiar,self.rozmiar))
        pygame.display.update()

    def rozmnazanie(self):
        pass

    def powstanie(self):
        pow = '\nPowstał nowy organizm: ' + self.nazwa
        self.swiat.powiadomienia.append(pow)

    def __del__(self):
        pass  # Implement the desired behavior for __del__()
