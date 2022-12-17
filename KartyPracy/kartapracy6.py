def zadanie1():
    a = int(input())
    b = int(input())
    c = int(input())

    print("Arytmetyczny: ", end="")
    if b * 2 == a + c:
        print("TAK")
    else:
        print("NIE")

    print("Geometryczny: ", end="")
    if b * b == a * c:
        print("TAK")
    else:
        print("NIE")

    print("Rosnący: ", end="")
    if b > a and c > b:
        print("TAK")
    else:
        print("NIE")

    print("Malejący: ", end="")
    if a > b and b > c:
        print("TAK")
    else:
        print("NIE")


# zadanie1()


def zadanie2():
    suma = 0
    for liczba in range(100, 1000):
        if liczba % 8 == 0 and liczba % 16 != 0:
            suma += liczba
    print(suma)


# zadanie2()


def zadanie3():
    liczba_dwucyfrowa = 0
    ilosc = 0

    for i in range(99, 1, -1):
        if i % 7 == 0:
            liczba_dwucyfrowa = i
            break

    for liczba in range(1000, 10000):
        if liczba % liczba_dwucyfrowa == 0:
            ilosc += 1

    print(ilosc)


# zadanie3()


def zadanie5():
    ilosc = 0
    suma = 0

    for liczba in range(100, 1000):
        cs = liczba // 100
        cd = (liczba % 100) // 10
        cj = liczba % 10

        if cs > cd + cj:
            ilosc += 1
            suma += liczba

    print(ilosc, suma)


# zadanie5()


def zadanie6():
    n = int(input())
    suma = 0

    for liczba in range(10, 100):
        if n == 0:
            break

        if liczba % 19 == 0:
            suma += liczba
            n -= 1
            print(liczba)

    if n > 0:
        print(f"Nie udalo mi się znaleźć {n} liczb!")

    print(f"Suma: {suma}")


# zadanie6()


def zadanie7():
    n = int(input())
    suma = 0

    for liczba in range(999, 99, -1):
        if n == 0:
            break

        if liczba % 37 == 0:
            suma += liczba
            n -= 1
            print(liczba)

    if n > 0:
        print(f"Nie udalo mi się znaleźć {n} liczb!")

    print(f"Suma: {suma}")


# zadanie7()


def zadanie8():
    n = int(input())
    suma = 0

    # i = 0 => 2 + 0 * 3 = 2
    # i = 1 => 2 + 1 * 3 = 5
    # i = 2 => 2 + 2 * 3 = 8

    for i in range(n):
        expresion = 2 + i * 3
        if i % 2 != 0:
            expresion *= -1

        print(f"{i+1}: {expresion}")

        suma += expresion

    print(f"Suma: {suma}")


# zadanie8()


def zadanie9():
    n = int(input())
    iloczyn = 1
    liczba = 1
    for i in range(n):
        iloczyn *= liczba
        liczba *= -2

    print(iloczyn)


# zadanie9()


def silnia(n):
    iloczyn = 1
    for i in range(1, n + 1):
        iloczyn *= i
    return iloczyn


def zadanie10():
    # 4! = 1 * 2 * 3 * 4
    n = int(input())
    suma = 0

    for i in range(1, n + 1):
        suma += silnia(i)

    print(suma)


# zadanie10()


def zadanie11():
    n = int(input())
    suma = 0

    for i in range(1, n + 1):
        # licznik: i * 2 - 1
        # mianownik: (i) ** 2

        licznik = i * 2 - 1
        mianownik = i**2

        suma += licznik / mianownik

    print(suma)


# zadanie11()


def zadanie12():
    n = int(input())
    suma = 0

    licznik = 0
    mianownik = 0

    for i in range(1, n + 1):
        # licznik: i * 2 - 1
        # mianownik: (i) ** 2

        licznik += i * 2 - 1
        mianownik += i**2

    suma = licznik / mianownik

    print(suma)


# zadanie12()


def zadanie13():
    n = int(input())
    suma = 0

    for i in range(1, n + 1):
        licznik = 2 * i
        mianownik = i**3 + 2

        suma += licznik / mianownik

    print(suma)


# zadanie13()


def zadanie15():
    n = int(input())
    iloczyn = 1

    for i in range(1, n + 1):
        licznik = 2 + i
        mianownik = 2**i - 1

        iloczyn *= licznik / mianownik

    print(iloczyn)


# zadanie15()


# f(n) = f(n-1) + f(n-2)
def rec_fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return rec_fib(n - 1) + rec_fib(n - 2)


def zadanie16():
    n = int(input())
    iloczyn = 1

    for i in range(1, n + 1):
        licznik = rec_fib(i)
        mianownik = 2 ** (i - 1)
        iloczyn *= licznik / mianownik

    print(iloczyn)


zadanie16()