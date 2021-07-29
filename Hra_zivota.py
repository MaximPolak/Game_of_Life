import time

class Hra_zivota:
    def __init__(self, sirka, vyska):
        self.sirka = sirka
        self.vyska = vyska
        self.hraci_plocha = [[" " for _ in range(self.sirka)] for _ in range(self.vyska)]
        self.policka_okolo_bunky = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    def indexy(self):
        for radek in range(self.vyska):
            for sloupec in range(self.sirka):
                yield (radek, sloupec)
                
    def policka_na_update(self):
        policka_na_update = []
        for radek, sloupec in self.indexy():
            zive_bunky_okolo = 0

            for pole in self.policka_okolo_bunky:

                try:
                    if self.hraci_plocha[radek + pole[0]][sloupec + pole[1]] != " ":
                        zive_bunky_okolo += 1
                except IndexError:
                    pass

            aktualni_bunka = self.hraci_plocha[radek][sloupec]
            if aktualni_bunka == " " and zive_bunky_okolo == 3:
                policka_na_update.append(("o", (radek, sloupec)))
            elif aktualni_bunka == "o" and zive_bunky_okolo not in (2, 3):
                policka_na_update.append((" ", (radek, sloupec)))

        return policka_na_update

    def update(self):
        for znak, (radek, sloupec) in self.policka_na_update():
            self.hraci_plocha[radek][sloupec] = znak

"""
hra = Hra_zivota(10, 10)

hra.hraci_plocha[1][4] = "o"
hra.hraci_plocha[1][6] = "o"
hra.hraci_plocha[2][2] = "o"
hra.hraci_plocha[2][4] = "o"
hra.hraci_plocha[2][7] = "o"
hra.hraci_plocha[3][4] = "o"
hra.hraci_plocha[3][6] = "o"
hra.hraci_plocha[3][7] = "o"
hra.hraci_plocha[4][2] = "o"
hra.hraci_plocha[4][4] = "o"
hra.hraci_plocha[5][5] = "o"


while True:
    for radek in hra.hraci_plocha:
        print(radek)
    print("\n")
    print(10 * "-")

    hra.update()

    time.sleep(1)
"""