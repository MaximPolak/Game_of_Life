import time
import Hra_zivota
import PySimpleGUI as sg

vyska = 20
sirka = 30
hra = Hra_zivota.HraZivota(sirka, vyska)

hraci_plocha = [[sg.Button(
    "", key=(radek, sloupec), size=(2, 1), pad=(0, 0), button_color=("blue", "#4964A9")) 
        for sloupec in range(sirka)] for radek in range(vyska)]
zbytek_plochy = [[sg.Button("Další kolo", size=(8, 2))]]
rozmisteni = hraci_plocha + zbytek_plochy

okno = sg.Window("Hra života", rozmisteni)

barvy = {True: ("red", "#E98478"), False: ("blue", "#4964A9")}

while True:
    udalost, hodnoty = okno.read()
    if udalost == sg.WINDOW_CLOSED:
        break
    elif udalost != "Další kolo":
        barva = hra.zmen_pole(udalost)
        okno[udalost].update(button_color=(barvy[barva]))
        
    elif udalost == "Další kolo":
        for stav, indexy in hra.policka_na_update():
            okno[indexy].update(button_color=barvy[stav])
        hra.update()
        
okno.close()                                                                          