dane=open('dane_6_2.txt','r').readlines()

for i in range(len(dane)):
    dane[i]=dane[i].rstrip()
# print(dane)

for i in dane:
    deszyfr=''
    l=i.split()
    if len(l)<2:
        klucz=0
    else:klucz= int(l[1])%26

    k= list(l[0])
    for j in range(len(k)):
        wartosc=0
        wartosc=ord(k[j])-klucz
        if wartosc<65:
            wartosc+=26
        deszyfr+=chr(wartosc)
    print(deszyfr)