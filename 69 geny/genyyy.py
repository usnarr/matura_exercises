dane=open('dane_geny.txt','r').readlines()

for i in  range (len(dane)):
    dane[i]=dane[i].rstrip()

tab=[0]*501
liczbagatunk=0


for i in dane:
    tab[len(i)]+=1

print(max(tab))

for i in tab:
    if i!= 0:
        liczbagatunk+=1

print(liczbagatunk)
