# sprawdz czy dana liczba jest pierwsza

# n = int(input())
# for i in range(2, n):
#     if n % i == 0:
#         print("NIE JEST PIERWSZA")
#         exit(0)
# else:
#     print("TAK LICZBA JEST PIERWSZA")

# generator liczb pierwszych dla p,q
# p, q = int(input()) , int(input())

# for j in range(p, q+1):
#      for i in range(2, n):
#          if j % i == 0:
#              flaga = False
#              break
#     if flaga == True:
#         print(j = "")

# 3 generowanie liczb pierwszych (pierwsze n liczb pierwszych)
n = int(input("podaj ile chcesz liczb pierwszych"))
while 1:
    flaga = True
    for i in range(2, k):
        if k % i == 0:
            flaga = False
            break
    if flaga == True:
        print(k, end="")
        ilosc = ilosc +1
    if ilosc == n:
        break
    k = k +1
        
        