# Algorytm Ewolucyjny / Evolution Algorythm

Algorytm ewolucyjny stworzony prze ze mnie na potrzeby zajęć na studiach. Jego celem jest optymalizacja funkcji jednowymiarowej.

Przykładowy wynik mojego algorytmy optymalizującego funkcje jednowymiarową:
![image](https://github.com/jerzy244/AlgorytmEwolucyjny/assets/77549671/de399636-35ab-4e00-b90c-0f3f5ec7ebac)

Parametry dla tego przykładu: 
population_size = 1000
generations = 500
mutation_rate = 0.2 


Ten algorytm ewolucyjny działa na następujących zasadach:

**Inicjalizacja populacji początkowej:**
Określamy rozmiar populacji (liczbę osobników w populacji) oraz parametry
początkowe, takie jak przedział wartości, w którym będą generowane osobniki.

**Ocena populacji:**
Dla każdego osobnika w populacji obliczamy wartość funkcji celu, czyli jakość
rozwiązania w kontekście problemu optymalizacyjnego. W tym przypadku używamy
funkcji jednowymiarowej.

**Pętla generacji:**
Powtarzamy określoną liczbę generacji (iteracji algorytmu).

**Selekcja:**
Wybieramy dwa osobniki z populacji rodzicielskiej na podstawie ich wartości fitness. W
tym przypadku stosujemy selekcję turniejową, gdzie losowo wybieramy dwa osobniki i
wybieramy najlepszego spośród nich.

**Krzyżowanie:**
Tworzymy potomka poprzez skrzyżowanie (kombinację) genów rodziców. W tym
przypadku stosujemy prostą operację krzyżowania, w której genotyp potomka to średnia
wartość genotypów rodziców.

**Mutacja:**
Istnieje pewne prawdopodobieństwo mutacji, które determinuje, czy potomek będzie
podlegał mutacji. Jeśli tak, to dodajemy do jego wartości genotypu losową wartość.
Obliczanie wartości funkcji celu dla potomka:
Obliczamy wartość funkcji celu dla potomka, aby ocenić jakość rozwiązania.

**Aktualizacja populacji:**
Zastępujemy jednego z osobników w populacji rodzicielskiej przez potomka, jeśli
wartość funkcji celu potomka jest lepsza od zastąpionego osobnika.

**Zapis najlepszego rozwiązania i wartości funkcji celu:**
Zapisujemy najlepsze znalezione rozwiązanie i wartość funkcji celu w danej generacji.

**Obliczanie odchylenia standardowego:**
Obliczamy odchylenie standardowe wartości funkcji celu w populacji. To służy do
monitorowania zmienności populacji w kolejnych generacjach.

Powtarzanie kroków 4-10 dla określonej liczby generacji.

Zwrócenie listy najlepszych wartości funkcji celu i odchyleń standardowych dla każdej
generacji.
