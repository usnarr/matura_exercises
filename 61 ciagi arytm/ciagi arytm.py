import math

dane=open('ciagi.txt','r').readlines()

for i in  range (len(dane)):
    dane[i]=dane[i].rstrip()
# print(dane)

#zad 1
licznik=0
roznicamax=0
for i in dane:
    k=i.split()
    czyjest=True
    if len(k)==1:
        czyjest=False
    if len(k)!=1:
        roznica=int(k[1])-int(k[0])
    for j in range(len(k)-1):
        if  int(k[j+1])- int(k[j])!=roznica:
            czyjest=False
    if czyjest==True:
        if roznica>roznicamax:
            roznicamax=roznica
        licznik+=1
print(licznik)
print(roznicamax)


for i in dane:
    k=i.split()
    czyjest = True
    if len(k) == 1:
        czyjest = False
    if len(k) != 1:
        roznica = int(k[1]) - int(k[0])
    for j in range(len(k) - 1):
        if int(k[j + 1]) - int(k[j]) != roznica:
            czyjest = False
    if czyjest == True:
        czyszescian=False
        maxszescian=0
        for j in range (len(k)):
            liczba=math.pow(int(k[j]),1.0/3)
            if liczba%1==0:
                czyszescian=True
            if czyszescian==True and liczba>maxszescian:
                maxszescian=liczba
        print(maxszescian)






