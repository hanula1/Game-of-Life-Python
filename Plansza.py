import pygame
import pickle
from Swiat import Swiat
from Antylopa import Antylopa
from CyberOwca import CyberOwca
from Lis import Lis
from Owca import Owca
from Zolw import Zolw
from Wilk import Wilk
from BarszczSosnowskiego import BarszczSosnowskiego
from Guarana import Guarana
from Mlecz import Mlecz
from Trawa import Trawa
from WilczeJagody import WilczeJagody
from Czlowiek import Czlowiek

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
            mouse_presses = pygame.mouse.get_pressed()

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
            if keys[pygame.K_s]:
                self.zapis()
            if keys[pygame.K_l]:
                self.odczyt()
            if mouse_presses[0]:
                pos = pygame.mouse.get_pos()
                pos = (int(pos[0]/self.rozmiar), int(pos[1]/self.rozmiar))
                self.wybor(pos)
                run = True


            self.swiat.czlowiek.rysowanie()
            if ruch:
                self.swiat.wyjonajTure()

    def wybor(self, pozycja):
        font_size = 25
        font = pygame.font.Font(None, font_size)
        choice = pygame.display.set_mode((200, 350))
        tworzenie = ["Antylopa", "Barszcz Sosnowskiego", "Cyber Owca", "Guarana", "Lis", "Mlecz", "Owca", "Trawa",
                     "Wilcze Jagody", "Wilk", "Zolw"]
        run = True
        while run:
            for i in tworzenie:
                text_surface = font.render(i, True, (255, 255, 255))  # Kolor biały
                text_x = (200 - text_surface.get_width()) // 2
                text_y = 30*tworzenie.index(i)
                choice.blit(text_surface, (text_x, text_y))
                pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                pos = pygame.mouse.get_pos()
                a = int(pos[1]/30)
                print(a)
                if tworzenie[a] == "Antylopa":
                    self.swiat.organizmy.append(Antylopa(self.swiat))
                elif tworzenie[a] == "Owca":
                    self.swiat.organizmy.append(Owca(self.swiat))
                elif tworzenie[a] == "Barszcz Sosnowkiego":
                    self.swiat.organizmy.append(BarszczSosnowskiego(self.swiat))
                elif tworzenie[a] == "Cyber Owca":
                    self.swiat.organizmy.append(CyberOwca(self.swiat))
                elif tworzenie[a] == "Guarana":
                    self.swiat.organizmy.append(Guarana(self.swiat))
                elif tworzenie[a] == "Lis":
                    self.swiat.organizmy.append(Lis(self.swiat))
                elif tworzenie[a] == "Mlecz":
                    self.swiat.organizmy.append(Mlecz(self.swiat))
                elif tworzenie[a] == "Trawa":
                    self.swiat.organizmy.append(Trawa(self.swiat))
                elif tworzenie[a] == "Wilcze Jagody":
                    self.swiat.organizmy.append(WilczeJagody(self.swiat))
                elif tworzenie[a] == "Wilk":
                    self.swiat.organizmy.append(Wilk(self.swiat))
                elif tworzenie[a] == "Zolw":
                    self.swiat.organizmy.append(Zolw(self.swiat))
                wielkosc = len(self.swiat.organizmy)
                self.swiat.organizmy[wielkosc - 1].polozenie = pozycja
                run = False

        self.win = pygame.display.set_mode((500, 500))
        for i in self.swiat.organizmy:
            i.rysowanie()
        pygame.display.update()

    def zapis(self):
        with open("zapis.txt", "w") as file:
            file.write(str(self.N)+'\n')
            for i in self.swiat.organizmy:
                if isinstance(i, Czlowiek):
                    continue
                file.write(str(i.nazwa)+'\n')
                file.write(str(i.polozenie[0])+'\n')
                file.write(str(i.polozenie[1]) + '\n')
                file.write(str(i.poprzednie_polozenie[0])+'\n')
                file.write(str(i.poprzednie_polozenie[1]) + '\n')
                file.write(str(i.sila)+'\n')
                file.write(str(i.wiek)+'\n')

            file.write(str(self.swiat.czlowiek.nazwa) + '\n')
            file.write(str(self.swiat.czlowiek.polozenie[0]) + '\n')
            file.write(str(self.swiat.czlowiek.polozenie[1]) + '\n')
            file.write(str(self.swiat.czlowiek.poprzednie_polozenie[0]) + '\n')
            file.write(str(self.swiat.czlowiek.poprzednie_polozenie[1]) + '\n')
            file.write(str(self.swiat.czlowiek.sila) + '\n')
            file.write(str(self.swiat.czlowiek.wiek) + '\n')
            file.write(str(self.swiat.czlowiek.umiejetnosc)+'\n')

    def odczyt(self):
        self.win.fill((0, 0, 0))
        self.swiat.organizmy = []
        with open("zapis.txt", "r") as file:
            self.N = file.readline()
            text = file.readline()
            i=0
            while text is not "Czlowiek":
                if text == "Antylopa":
                    self.swiat.organizmy.append(Antylopa(self.swiat))
                elif text == "Owca":
                    self.swiat.organizmy.append(Owca(self.swiat))
                elif text == "Barszcz Sosnowkiego":
                    self.swiat.organizmy.append(BarszczSosnowskiego(self.swiat))
                elif text == "Cyber Owca":
                    self.swiat.organizmy.append(CyberOwca(self.swiat))
                elif text == "Guarana":
                    self.swiat.organizmy.append(Guarana(self.swiat))
                elif text == "Lis":
                    self.swiat.organizmy.append(Lis(self.swiat))
                elif text == "Mlecz":
                    self.swiat.organizmy.append(Mlecz(self.swiat))
                elif text == "Trawa":
                    self.swiat.organizmy.append(Trawa(self.swiat))
                elif text == "Wilcze Jagody":
                    self.swiat.organizmy.append(WilczeJagody(self.swiat))
                elif text == "Wilk":
                    self.swiat.organizmy.append(Wilk(self.swiat))
                elif text == "Zolw":
                    self.swiat.organizmy.append(Zolw(self.swiat))
                a = file.readline()
                b = file.readline()
                self.swiat.organizmy[i].polozenie = (int(a), int(b))
                a = file.readline()
                b = file.readline()
                self.swiat.organizmy[i].poprzednie_polozenie = (int(a), int(b))
                self.swiat.organizmy[i].sila = int(file.readline())
                self.swiat.organizmy[i].wiek = int(file.readline())
                i += 1
                text = file.read()

            self.swiat.czlowiek = Czlowiek(self.swiat)
            self.swiat.organizmy.append(self.swiat.czlowiek)
            a = file.readline()
            b = file.readline()
            self.swiat.organizmy[i].polozenie = (int(a), int(b))
            a = file.readline()
            b = file.readline()
            self.swiat.organizmy[i].poprzednie_polozenie = (int(a), int(b))
            self.swiat.organizmy[i].sila = int(file.readline())
            self.swiat.organizmy[i].wiek = int(file.readline())
            self.swiat.organizmy[i].umiejetnosc = int(file.readline())

        for i in self.swiat.organizmy:
            i.rysowanie()

        # Convert the string back to an integer
        #number = int(number_str)
