dane=open('dane_6_3.txt','r').readlines()

for i in range(len(dane)):
    dane[i]=dane[i].rstrip()

# print(dane)

for i in dane:
    l=i.split()
    czydobrze=False
    k=l[0]
    m=l[1]
    # print(k,m)
    klucz= ord(m[0])-ord(k[0])
    if klucz<0:
        klucz+=26
    for j in range(len(k)):
        if ord(k[j])+klucz==ord(m[j]):
            czydobrze=True
    if czydobrze==False:
        print(i)