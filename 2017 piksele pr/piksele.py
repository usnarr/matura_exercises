dane=open('dane.txt','r').readlines()

for i in range(len(dane)):
    dane[i]=dane[i].rstrip().split()


max=0
min=111111110

for i in dane:
    k=i
    for j in range(len(k)):
        if int(k[j]) > max:
            max = int(k[j])
        if int(k[j]) < min:
            min = int(k[j])


print(max,min)

licznikwierszyzlych=0
for i in dane:
    k=i
    licznik=0


    if k!=k[::-1]:
        licznikwierszyzlych+=1
print(licznikwierszyzlych)

licznik1=0
for i in range(len(dane)):


    for j in range(320):
        wartosc1=int(dane[i][j])
        if j!=0:
            wartosclewy=int(dane[i][j-1])
            if abs(wartosclewy-wartosc1)>128:
                licznik1+=1
                continue
        if j!=319:
            wartoscprawy=int(dane[i][j+1])
            if abs(wartoscprawy-wartosc1)>128:
                licznik1+=1
                continue
        if i!=0:
            wartoscgora=int(dane[i-1][j])
            if abs(wartoscgora-wartosc1)>128:
                licznik1+=1
                continue
        if i!=199:

            wartoscdol=int(dane[i+1][j])
            if abs(wartoscdol-wartosc1)>128:
                licznik1+=1
                continue
print(licznik1)

max=0

for j in range(320):
    licznik = 1
    for i in range(199):

        if dane[i][j]==dane[i+1][j]:
            licznik+=1
            if licznik > max:
                max = licznik
        else:licznik=1

print(max)





