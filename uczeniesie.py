
# # karta pracy 3b



# def tablice():
#     tab = [1, 2, 3, 4]
#     # tab1= [0, 1, 2, 3]
#     tab[1] = 7
#     tab.append("Kuba")
#     print("0")
#     print(0)
#     print("0" == 0)


# def zadanie1():
#     for i in range(1, 31):
#         print(f"{i} listopada 2022")


# def zadanie2():
#     for i in range(1, 10, 2):
#         print(i, i * i)


# def zadanie3():
#     for i in range(1000, 10000):
#         if i % 379 == 0:
#             print(i)


# def zadanie4():
#     for i in range(100, 1000):
#         if i % 5 == 0 or i % 6 == 0 or i % 11 == 0:
#             print(i)


# def zadanie5():
#     tab = []
#     n = int(input("Podaj ilosc liczb: "))
#     for _ in range(n):
#         a = float(input("Podaj Liczbe: "))
#         tab.append(a)
#     print(tab)
#     print(sum(tab))

#     # n = int(input("Podaj ilosc liczb: "))
#     # suma = 0
#     # for _ in range(n):
#     #     a = float(input("Podaj Liczbe: "))
#     #     suma += a
#     # print(suma)


# # zadanie5()


# def zadanie6():
#     suma = 0
#     k = int(input("Podaj k: "))
#     for i in range(1, k + 1):
#         suma += i * 2
#         print(i, i * 2)

#     # for i in range(2, (k + 1) * 2, 2):
#     #     suma += i
#     #     print(i)
#     print(suma)


# def zadanie7():
#     m = int(input("Podaj m: "))
#     suma = 0
#     for i in range(1, m * 2, 2):
#         suma += 100 + i
#     print(suma)


# def zadanie8():
#     K = 0.06
#     W = float(input("Podaj W0: "))
#     L = int(float(input("Podaj Lata: ")) * 12)
#     K /= 12
#     for _ in range(L):
#         W += W * (K)
#         print("{:.2f}".format(W))

#     print("Wynik: {:.2f}".format(W))


# def zadanie9():
#     # 121 % 100 == 21
#     # 221 % 100 == 21

#     m = int(input("Podaj m: "))
#     suma = 0
#     i = 21
#     while m > 0:
#         if i % 100 == 21:
#             print(i)
#             suma += i
#             m -= 1
#         i += 1

#     # for i in range(m):
#     #     suma += 21 + i * 100
#     print(suma)


# def zadanie10():
#     import math
#     for i in range(1, 1001):
#         num1 = str(i)
#         num2 = str(math.sqrt(i))
#         if num2[-2:] == ".0":
#             num2 = num2[:-2]
#         if num1.endswith(num2):
#             print(num1)


# zadanie10()
