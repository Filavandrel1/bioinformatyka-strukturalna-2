Program uruchamia się komendą: 

python3 zadanie_2.py --fasta {nazwa_pliku.fasta}


Plik {nazwa_pliku.fasta} powinien mieć następującą strukturę:
>nazwa sekwencji
DKLMNPQRSFFWYHEACGTV
>nazwa drugiej sekwencji
VIDRNPHQMSLFENAKL


Program zapisuje wyniki do pliku wynik.txt

Plik wynik.txt składa się ze wszystkich możliwych rozwiązań na podstawie wyniku, jakie osiągnęły dane rozwiązania, rozwiązania oddzielone są linią.

Domyślny zestaw oceniania jest następujący:
Przerwa = -2
Poprawne dopasowanie = 1
Błędne dopasowanie = -1

Każde z rozwiązań można podzielić na części:
Pierwsze dwie linie mówią gdzie zaczynają się znalezione dopasowania w oryginalnych sekwencjach. Kolejne 3 pokazują znalezione rozwiązanie ze znakiem "|" tam, gdzie występuje połączenie i " " tam, gdzie go nie ma. 

Przykładowy wygląd rozwiązania:
sekwencja1: pozycje 9-38
sekwencja2: pozycje 9-38
MKTAYIAKQRQISFVKSHFSRQLEERLGLI
||||||| |||||||| |||||||| ||||
MKTAYIAEQRQISFVKTHFSRQLEEKLGLI


Przykład uruchomienia:
python3 zadanie_2.py --fasta test.fasta

plik test.fasta wygląda następująco:
>sekwencja 1 
DDKLMNPQRSFFWYHEACGTVIDEE
>sekwencja 2
GGWYHEAGTVIDRNPHQMSLFENAKLMNPQRSCC

wynik.txt wygląda następująco:
sekwencja 1: pozycje 3-10
sekwencja 2: pozycje 25-32
KLMNPQRS
||||||||
KLMNPQRS
--------------------------
sekwencja 1: pozycje 13-23
sekwencja 2: pozycje 3-12
WYHEACGTVID
||||| |||||
WYHEA-GTVID


Oba rozwiązania dostały po 8 punktów. W pierwszym jest to 8 poprawnych połączeń z rzędu, natomiast w drugim mamy 10 poprawnych i jedną przerwę, więc 10*1 - 2 = 8.