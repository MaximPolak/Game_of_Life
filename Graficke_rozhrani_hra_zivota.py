import time
import Hra_zivota
import PySimpleGUI as sg

vyska = 20
sirka = 30
hra = Hra_zivota.HraZivota(sirka, vyska)

hraci_plocha = [[sg.Button("", key=(radek, sloupec), size=(2, 1), pad=(0, 0), button_color=("blue", "#0000FF")) for sloupec in range(sirka)] for radek in range(vyska)]
zbytek_plochy = [[sg.Button("Start", size=(6, 2))]]
rozmisteni = hraci_plocha + zbytek_plochy

okno = sg.Window("Hra života", rozmisteni)

while True:
    udalost, hodnoty = okno.read()
    if udalost == sg.WINDOW_CLOSED:
        break
    elif udalost and udalost != "Start":
        okno[udalost].update(button_color=("red", "#FF0000"))
        hra.zmen_pole(udalost)
    elif udalost == "Start":
        while True:
            for stav, indexy in hra.policka_na_update():
                if stav == True:
                    okno[indexy].update(button_color=("red", "#FF0000"))
                else:
                    okno[indexy].update(button_color=("blue", "#0000FF"))
            hra.update()
            time.sleep(1)
        
okno.close()   