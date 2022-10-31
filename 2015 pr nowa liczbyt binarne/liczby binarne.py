dane=open('liczby.txt','r').readlines()

for i in range (len(dane)):
    dane[i]=dane[i].rstrip()

licznik=0
for i in dane:
    if i.count('0')>i.count('1'):
        licznik+=1
print(licznik)


licznikprzez2=0
licznikprzez8=0
for i in dane:
    if int(i,2)%2==0:
        licznikprzez2+=1

    if int(i,2)%8==0:
        licznikprzez8+=1

print(licznikprzez2)
print(licznikprzez8)

max=0
min=100000000
for j in range(len(dane)):
    liczba=int(dane[j],2)
    if liczba>max:
        max=liczba

for j in range(len(dane)):
    liczba = int(dane[j],2)
    if liczba < min:
        min = liczba
print('max liczba',max)
print('min liczba',min)

for j in range (len(dane)):
    liczba = int(dane[j], 2)
    if liczba==max:
        print('linijkamax')
        print(j+1)
    if liczba==min:
        print('linijkamin')
        print(j+1)



