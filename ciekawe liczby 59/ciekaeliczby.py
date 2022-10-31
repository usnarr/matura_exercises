dane=open('liczby.txt','r').readlines()

for i in range (len(dane)):
    dane[i]=dane[i].rstrip()
# print(dane)


a=634
def czynniki(a):
    czynnik=2
    lista=[]
    a=int(a)
    while a>1:
        if a%czynnik ==0:
            a//=czynnik
            if czynnik  not in lista:
                lista.append(czynnik)
        else:
            czynnik+=2
    return lista
licznik1=0
for i in dane:
    if int(i)%2==0:
        continue
    b=czynniki(i)

    if len(b)==3:
        licznik1+=1
print(licznik1)




#zad 2
licznik=0
for i in dane:
    suma=int(i)+int(i[::-1])
    if str(suma)==str(suma)[::-1]:
        licznik+=1
# print(licznik)



#zad 3
licznik11=0
licznik22=0
licznik33=0
licznik44=0
licznik55=0
licznik66=0
licznik77=0
licznik88=0


for i in dane:
    k=i.split()
    moc=0

    if len(i)==1:
        moc=1
    for j in range(len(k)-1):
        wynik=+k[j]*k[j+1]



