import time

class HraZivota:
    def __init__(self, sirka, vyska, hraci_plocha="nezadano"):
        self.sirka = sirka
        self.vyska = vyska
        if hraci_plocha == "nezadano":
            self.hraci_plocha = [[False for _ in range(self.sirka)] for _ in range(self.vyska)]
        else:
            self.hraci_plocha = hraci_plocha
        self.policka_okolo_bunky = tuple((i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0))
        # self.policka_okolo_bunky = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    def indexy(self):
        for radek in range(self.vyska):
            for sloupec in range(self.sirka):
                yield (radek, sloupec)
                
    def policka_na_update(self):
        policka_na_update = []
        for radek, sloupec in self.indexy():
            zive_bunky_okolo = 0

            for x, y in self.policka_okolo_bunky:

                try:
                    if self.hraci_plocha[radek + x][sloupec + y] != False:
                        zive_bunky_okolo += 1
                except IndexError:
                    pass

            aktualni_bunka = self.hraci_plocha[radek][sloupec]
            if aktualni_bunka == False and zive_bunky_okolo == 3:
                policka_na_update.append((True, (radek, sloupec)))
            elif aktualni_bunka == True and zive_bunky_okolo not in (2, 3):
                policka_na_update.append((False, (radek, sloupec)))

        return policka_na_update

    def update(self):
        for znak, (radek, sloupec) in self.policka_na_update():
            self.hraci_plocha[radek][sloupec] = znak

    def zmen_pole(self, index):
        x, y = index
        if self.hraci_plocha[x][y] == False:
            self.hraci_plocha[x][y] = True
        else:
            self.hraci_plocha[x][y] = False



"""
hra = HraZivota(10, 10)

hra.hraci_plocha[1][4] = True
hra.hraci_plocha[1][6] = True
hra.hraci_plocha[2][2] = True
hra.hraci_plocha[2][4] = True
hra.hraci_plocha[2][7] = True
hra.hraci_plocha[3][4] = True
hra.hraci_plocha[3][6] = True
hra.hraci_plocha[3][7] = True
hra.hraci_plocha[4][2] = True
hra.hraci_plocha[4][4] = True
hra.hraci_plocha[5][5] = True


while True:
    for radek in hra.hraci_plocha:
        print(radek)
    print("\n")
    print(10 * "-")

    hra.update()

    time.sleep(1)
"""
