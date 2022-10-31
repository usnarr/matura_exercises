import math

dane=open('dane_ulamki.txt','r').readlines()

for i in range (len(dane)):
    dane[i]=dane[i].rstrip()
# print(dane)


wartoscmin=11111110
ulamekmin=''

# for i in dane:
#     k=i.split()
#     wynik=int(k[0])/ int(k[1])
#     # print("{1},nfajfa {1}".format(i,i))
#     # print(f"ulamek to {i}, wynik to {wynik}")
#     # print(f" wartosc minimalna {wartoscmin},wynik to {wynik},test logiczny:{wynik<wartoscmin}")
#     if wynik<wartoscmin:
#         wartoscmin=wynik
#         ulamekmin=i
#     # print(f" po ew if {wartoscmin}")
# print(wartoscmin)
# print(ulamekmin)

licznik=0

for i in dane:
    k=i.split()
    if math.gcd(int(k[0]),int(k[1]))==1:
        licznik+=1
        # print(i)
# print(licznik)

sumalicznik=0
for i in dane:
    k=i.split()
    nwd=math.gcd(int(k[0]),int(k[1]))
    if nwd!=1:
        k[0]=int(k[0])/nwd
        k[1]=int(k[1])/nwd
    sumalicznik+=int(k[0])
# print(sumalicznik)


licznik2=0
mianownik=((2*3*5*7)**2)*13
for i in dane:
    k=i.split()
    mnoznik=mianownik/int(k[1])
    licznik2+=int(k[0])*mnoznik

print(licznik2)



