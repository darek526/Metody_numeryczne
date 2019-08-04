def hermite_interp(L):
    # utworzenie wektorów x i y
    x = []
    y = []

    for x_i, P in L:
        k = len(P)
        x += [float(x_i)] * k
        y += [float(P[0])] * k

    m = len(L) # liczba węzłów
    n = len(x) # długość wektora x (także wektora y)
    factorial = 1 # aktualna wartość silni
    
    # polczenie wartości ilorazów różnicowych
    for h in range(1, n): # dla kolejnych odstępów pomiędzy indeksami
        i = m - 1 # zapisanie do i wartości indeksu ostatniego węzła
        factorial *= h # uzyskanie nowej wartości silni

        # liczenie ilorazów różnicowych od końca
        for j in range(n - 1, h - 1, -1):
            if x[j] != x[j - h]: # jeśli wartości x różnią się na pozycjach odległych o h
                y[j] = (y[j] - y[j - 1]) / (x[j] - x[j - h]) # policz iloraz różnicowy standardowo
            else:
                y[j] = L[i][1][h] / factorial # na aktualnej pozycji należy umieścić wartość pochodnej podzieloną przez aktualną wartość silni

            if x[j] != x[j - 1]: # jeśli wartości wektora x różnią się na sąsiednich pozycjach
                i -= 1 # zmniejszenie i o 1 (przejście w dół do kolejnego węzła)

    # policzenie współczynników wielomianu
    a = [0.0] * n # wektor ze współczynnikami wielomianu interpolacyjnego (początkowo same 0)
    a[0] = y[n - 1] # umieszczenie na początku wektora a ostatniej wartości wektora y
    last = 0 # indeks ostatniego elementu w wektorze a reprezentującym wielomian

    for i in range(n - 2, -1, -1): # dla i od n - 2 do 0 włącznie z krokiem -1
        last += 1 # zwiększenie indeksu ostatniego elelemntu wielomianu
        c = -x[i] # współczynnik przez który należy pomnożyć odpowiednie współczynniki wielomianu

        # policzenie iloczynu wielomianów a, oraz (x + c)
        for j in range(last, 0, -1):
            a[j] += a[j - 1] * c

        a[last] += y[i] # dodanie do ostatniego współczynnika wielomianu a kolejnego ilorazu różnicowego

    return a[::-1] # zwrócenie odwróconej listy a

def test():
    print('x^8 + 1')
    L = [[-1, [2, -8, 56]], [0, [1, 0, 0]], [1, [2, 8, 56]]]
    print(hermite_interp(L))

    print('\n3x^4 - 7x^2 + 5')
    L = [[-3, [185]], [1, [1, -2]], [0, [5, 0]]]
    print(hermite_interp(L))

    print('\n3x^4 - 7x^2 + 13')
    L = [[0, [13, 0, -14, 0, 72]]]
    print(hermite_interp(L))

    print('\n1.5x^3 - 8x^2 + 13.5x - 4')
    L = [[1, [3, 2]], [3, [5, 6]]]
    print(hermite_interp(L))

test()
