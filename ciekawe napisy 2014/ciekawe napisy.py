import math

dane=open("NAPIS.TXT",'r').readlines()

for i in range (len(dane)):
    dane[i]=dane[i].rstrip()
# print(dane)
print("zad 1")
def pierwsza (a):
    if a==2:
        return True
    if a<2:
        return False
    for i in range(2,math.ceil(math.sqrt(a)+1)):
        if a%i==0:
            return False
    return True
licznik=0
for i in dane:
    k=list(i)
    wynik=0
    for j in range(len(k)):
        wynik+=ord(k[j])
    if pierwsza(wynik)==True:
        licznik+=1
print(licznik)

print("Zad 2")
licznik2=0

for i in dane:
    czyjest = True
    k=list(i)
    for j in range (len(k)-1):
        if ord(k[j])>=ord(k[j+1]):
            czyjest=False
    if czyjest==True:
        print(i)
print("zad 3")


for i in dane:
    licznik3 = 0
    for j in range (len(dane)):
        if i==dane[j]:
            licznik3+=1
    if licznik3>1:
        print(i)