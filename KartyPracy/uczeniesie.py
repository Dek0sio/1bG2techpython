# zad 1
# a = int(input())
# b = int(input())
# c = int(input())
# if b * 2 == a + c:
#     print("ciag jest arytmetyczny")
# else:
#     print("ciag nie jest arytmetyczny")
# if b * b == a * c:
#     print("ciag jest geometryczny")
# else:
#     print("ciag nie jest geometryczny")
# if b > a and c > b:
#     print("ciag jest rosnący")
# else:
#     print("ciag nie jest rosnacy")
# if b < a and c < b:
#     print("ciag jest malejacy")
# else:
#     print("ciag nie jest malejacy")

# zad 2
# suma = 0
# for i in range(100, 1000):
#     if i % 8 == 0 and i % 16:
#         suma += i
# print(suma)

# zad 3
# liczba_dwucyfrowa = 0
# ilosc = 0
# for i in range(99, 1, -1):
#     if i % 7 == 0:
#         liczba_dwucyfrowa = i
#         break
        
# for liczba in range(1000, 10000):
#     liczba % liczba_dwucyfrowa == 0
#     ilosc += 1
# print(ilosc)

# zad 4
# ilosc = 0
# for i in range(10,100):
#     cd = i // 10
#     cj = i % 10
#     if cd >= 2*cj:
#         ilosc = ilosc + 1
# print(ilosc)

# zad 5
# suma = 0
# ilosc = 0
# for i in range(100, 1000):
#     cd = (i % 100) // 10
#     cj = i % 10
#     cs = i // 100
#     if cs > cd + cj:
#      ilosc = ilosc + 1
#      suma = suma + i
# print(ilosc, suma)

# zad 6
# n = int(input())
# suma = 0
# for i in range(10, 100):
#     if n == 0:
#         break

# if i % 19 == 0:
#     suma = suma + i
#     n = n - 1
# print(i)

# if n > 0:
#     print(f"nie udało sie znalesc {n} liczb")
# print(f"Suma: {suma}")

# zad 7
# n = int(input())
# suma = 0
# for i in range(999,99,-1):
#     if n == 0:
#         break

# if i % 37 == 0:
#     suma = suma + i
#     n = n - 1
# print(i)

# if n > 0:
#     print(f"nie udało sie znalesc {n} liczb")
# print(f"Suma: {suma}")