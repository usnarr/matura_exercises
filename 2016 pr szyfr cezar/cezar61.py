dane=open('dane_6_1.txt','r').readlines()

for i in range(len(dane)):
    dane[i]=dane[i].rstrip()

k=107
realk=3
for i in dane:
    szyfr=''

    k=list(i)
    for j in range (len(k)):
        wartosc = 0
        wartosc=ord(k[j])+realk
        szyfr+=chr(wartosc)
    print(szyfr)

