import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--fasta", required=True)
argumenty = parser.parse_args()


def wczytaj_sekwencje(plik):
    sekwencje = []
    nowa = True
    with open(plik) as tresc:
        for linia in tresc:
            linia = linia.strip().upper()
            if linia.startswith(">"):
                nowa = True
            elif linia:
                if nowa:
                    sekwencje.append(linia)
                    nowa = False
                else:
                    sekwencje[-1] += linia
    return sekwencje


sekwencje = wczytaj_sekwencje(argumenty.fasta)
if len(sekwencje) != 2:
    parser.error("plik musi zawierać dwie sekwencje")
sekwencja1 = sekwencje[0]
sekwencja2 = sekwencje[1]

przerwa = -2
blad = -1
poprawnosc = 1
najwieksza_wartosc = [0, []]
macierz = []

for i in range(len(sekwencja1) + 1):
    wiersz = []
    for j in range(len(sekwencja2) + 1):
        wiersz.append([0, []])
    macierz.append(wiersz)

for i in range(1, len(sekwencja1) + 1):
    for j in range(1, len(sekwencja2) + 1):
        if sekwencja1[i - 1] == sekwencja2[j - 1]:
            skos = macierz[i - 1][j - 1][0] + poprawnosc
        else:
            skos = macierz[i - 1][j - 1][0] + blad
        gora = macierz[i - 1][j][0] + przerwa
        lewo = macierz[i][j - 1][0] + przerwa

        wartosc = max(0, skos, gora, lewo)
        macierz[i][j][0] = wartosc

        if wartosc > 0:
            if skos == wartosc:
                macierz[i][j][1].append(1)
            if gora == wartosc:
                macierz[i][j][1].append(2)
            if lewo == wartosc:
                macierz[i][j][1].append(3)

        if wartosc > najwieksza_wartosc[0]:
            najwieksza_wartosc = [wartosc, [[i, j]]]
        elif wartosc == najwieksza_wartosc[0] and wartosc > 0:
            najwieksza_wartosc[1].append([i, j])

wyniki = []


def odczytaj(start_i, start_j):
    stos = [[start_i, start_j, "", ""]]
    while stos:
        i, j, dopasowanie1, dopasowanie2 = stos.pop()
        kierunki = macierz[i][j][1]
        if not kierunki:
            wyniki.append([dopasowanie1, dopasowanie2, i + 1, start_i, j + 1, start_j])
            continue
        for kierunek in reversed(kierunki):
            if kierunek == 1:
                stos.append([i - 1, j - 1, sekwencja1[i - 1] + dopasowanie1, sekwencja2[j - 1] + dopasowanie2])
            elif kierunek == 2:
                stos.append([i - 1, j, sekwencja1[i - 1] + dopasowanie1, "-" + dopasowanie2])
            elif kierunek == 3:
                stos.append([i, j - 1, "-" + dopasowanie1, sekwencja2[j - 1] + dopasowanie2])


for wystapienie in najwieksza_wartosc[1]:
    odczytaj(wystapienie[0], wystapienie[1])

with open("wynik.txt", "w") as plik:
    for n in range(len(wyniki)):
        if n > 0:
            plik.write("--------------------------\n")
        plik.write("sekwencja 1: pozycje " + str(wyniki[n][2]) + "-" + str(wyniki[n][3]) + "\n")
        plik.write("sekwencja 2: pozycje " + str(wyniki[n][4]) + "-" + str(wyniki[n][5]) + "\n")
        plik.write(wyniki[n][0] + "\n")
        linia = ""
        for k in range(len(wyniki[n][0])):
            if wyniki[n][0][k] == wyniki[n][1][k]:
                linia += "|"
            else:
                linia += " "
        plik.write(linia + "\n")
        plik.write(wyniki[n][1] + "\n")
