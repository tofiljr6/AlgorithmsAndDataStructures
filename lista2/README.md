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
- [ ] czas działania algorytmu
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
