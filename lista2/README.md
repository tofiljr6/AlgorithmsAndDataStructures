# Lista 2

## Lista czego brakuje (rzeczy wymagane):



### zadanie 1

- [X] brak niebraków

### zadanie 2

- [ ] dobry generator liczb
- [X] uśrednienie wyników

### zadanie 3

- [ ] ekseprymentalnie wyznacz stałą stojącą przy czynniku `nlogn` dla liczby porównań między kluczami

### zadanie 4

- [ ] sortowanie dowolnego typu

---

## Zadanie 1

Program przyjmuje dwa parametry wejściowe `--type insert|merge|quick` - określający wykorzystywanych algorytm sortowania oraz `--comp '>='|'<='` - określający porządek sortowania.

Wejściem dla programu są kolejno:

* liczba n - długość sortowania tablicy
* tablica elementów do posortowania

Program sortuje tablice wybranym algorytmem i wypisuje na standartowym wyjściu błędów wykonywanie operacje (porównania, przedstawienia). Po zakończeniu sortowania, na standardowym wyjściu błędów powinna zostać wypisana łączna liczba porównań, łączna liczba przestawień oraz czas działania algorytmu sortującego. Finalnie, program sprawdza, czy wynikowy ciąg jest posortowany zgodnie z wybranym porządkiem, a naste ̨pnie wypisuje na standardowe wyjście liczbę posortowanych elementów oraz posortowaną tablicę.

Przetestuj każdy z algorytmów dla następujących przypadków danych wejściowych tablica posortowana według określonego porządku, tablica „odwrotnie posortowana” według określonego porządku, tablica nieposortowana (np. losowa kolejność elementów). Wykonaj testy dla różnych długości tablicy n (np. n ∈ {10, 50, 100}).

```
./main --type quick --comp '>='
5
9 1 -7 1000 4
```
## Notes - zad 1

### ToDo
Dzisiaj must have
- [X] standardowe wyjście błędu **prawie zrobione, ale teraz nie na to pora**
- [X] obsługa z konsoli
- [X] porównania i przedstawienie NOW
  - [X] MERGESORT
  - [X] QUICKSORT
  - [X] INSERTIONSORT
- [X] czas działania algorytmu
- [X] final fun sprawdzajaca czy tablica jest faktycznie posortowana z podanym porządkiem
- [ ] naprawić insertion sort - zwraca tablice z porównaniami i podstawieniami, trzeba wybierać [0], nieładne to zrobiłem **!**
- [ ] obsługa błedu obsługi z konsoli **!**
- [X] po kolei instrukcje wypisuje **!!!**
  - [X] MERGESORT
  - [X] QUICKSORT
  - [X] INSERTIONSORT

### Porównania

- porównania to każdy if else itp
- przedstawienia to elemntów np. `A[j] = A[j+1]`

### Strerr

`python3 zad1.py 2> err.txt` wypisuje to co na standardowym wyjściu było!

---

## Zadanie 2

Plik główny to rysowania wykresów to **dataProcessing.py**
Jest bardzo słabo napisany, do poprawy w wolnym czasie!

Uzupełnij program z **zadania 1.** o możliwość wywoływania go z dodatkowym parametrem uruchomienia `--stat nazwa_pliku k`. W takim przypadku program ma pomijać wczytywanie danych i dla każdego `n` należącego do {100, 200, 300, ..., 100000} wykonywać po k niezależnych powtórzeń

Moje dane są w pliku `result2.txt`

## Notes - zad2
- [X] genertowanie losowej tablic *n* elementowej
  - [ ] zadbaj o dobry generator pseudolosowy **??**
- [X] sortowanie kopii wygenerowanych tablicy każdym algorytmem
- [X] dla każdego z sortowań, zapisania do pliku `nazwa_pliku` statystyk odnoście rozmiary danych n, liczby wykonanych porównań między kluczami, liczby przestawień kluczy oraz czas działania algorytmu sortującego

Po zakończeniu programu korzystając z zebranych danych, przedstaw na wykresach za pomocą `numpy`:

- [X] średnią liczbę wykonywanych porównań (c) w zależności od n
- [X] średnią liczbę przedstawień kluczy (s) w zależności od n
- [X] średni czas działania algorytmu w zależności od n
- [X] iloraz c/n w zależności od n
- [X] iloraz s/n w zależności od n

Zadbaj o to by dane dotyczące różnych algorytmów sortujących można było nakładać na te same osie i porównywać. Sprawdź, jak wykresy zmieniają się dla różnych wartości k (np. k = 1, k = 10, k = 1000)

### WYKRESY

#### Wykres przedstawiający liczbę wykonanych porównań w zależności od n

![wykres liczby wykonanych porównań w zależności od n](/lista2/charts/avgCompALL.png)

#### Wykres przedstawiający liczbę wykonanych przestawień w zależności od n

![wykres liczby wykonanych przestawień w zależności od n](/lista2/charts/avgSubsALL.png)

#### Wykres przedstawiający liczbę sekund w zależności od n

![wykres liczby sekund w zależności od n](/lista2/charts/timeALL.png)

#### Wykres przedstawiający iloraz c/n w zależności od n

![Wykres przedstawiający iloraz c/n w zależności od n](/lista2/charts/cn.png)

#### Wykres przedstawiający iloraz s/n w zależności od n

![Wykres przedstawiający iloraz s/n w zależności od n](/lista2/charts/sn.png)

---

## Zadanie 3

Sam algorytm **DAUL-PIVOT QUICKSORT** jest w pliku `zad3.py`. Natomiast w programie `zad1.py` dopisze i przeprowadzę na nim statystyki.

## Notes - zad 3

- [X] Stworzyć algorytm na kartce
- [X] Przemyśleć count
- [X] Stworzyć na boku działający program
- [X] Uzupełnić plik `zad1.py` o ten algorytm
- [X] Przeprowadzić dla niego statystyki
  - [X]  Porównania i przestawienia
- [ ] eksperymentalnie wyznaczyć stałą przed nlogn


### Wykres liczby sekund w zależności od n - porównanie quicksortów

![Wykres quicksrotów](/lista2/charts/quickSort.png)


## Zadanie 4

Zrobiłem w osobnym pliku.

### Wykres liczby sekund w zaelżności od n - porównanie quicksortów i hybrydy

![Hybryda sort](/lista2/charts/hybridcomparequicks.png)

### Uśredniony wynik hybrydowego dla 10 niezależnych powtórzeń

W sumie można się tego było spodziewać..., nie ma sensu powtarzać tego dla quicksortów
(może później to zrobię)

![Hybryda sort2](/lista2/charts/avghybrid.png)
