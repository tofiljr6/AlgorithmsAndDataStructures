# Lista 2

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
# Notes - zad 1

## ToDo
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

---

# Notes - zad2
- [X] genertowanie losowej tablic *n* elementowej
  - [ ] zadbaj o dobry generator pseudolosowy **??**
- [X] sortowanie kopii wygenerowanych tablicy każdym algorytmem
- [X] dla każdego z sortowań, zapisania do pliku `nazwa_pliku` statystyk odnoście rozmiary danych n, liczby wykonanych porównań między kluczami, liczby przestawień kluczy oraz czas działania algorytmu sortującego

Po zakończeniu programu korzystąc z zebranych danych, przedstaw na wykresach za pomocą `numpy`:

- [ ] średnią liczbę wykonywanych porównań (c) w zależności od n
- [ ] średnią liczbę przedstawień kluczy (s) w zależności od n
- [ ] średni czas działania algorytmu w zależności od n
- [ ] iloraz c/n w zależności od n
- [ ] iloraz s/n w zależności od n

Zadbaj o to by dane dotyczące różnych algorytmów sortujących można było nakładać na te same osie i porównywać. Sprawdź, jak wykresy zmieniają się dla różnych wartości k (np. k = 1, k = 10, k = 1000)

### Strerr

`python3 zad1.py 2> err.txt` wypisuje to co na standardowym wyjściu było!
