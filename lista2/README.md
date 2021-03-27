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
- [ ] standardowe wyjście błędu
- [ ] obsługa z konsoli
- [ ] porównania i przedstawienie NOW
- [ ] czas działania algorytmu
- [ ] final fun sprawdzajaca czy tablica jest faktycznie posortowana z podanym porządkiem

### Porównania

- porównania to każdy if else itp
- przedstawienia to elemntów np. ```A[j] = A[j+1]```
