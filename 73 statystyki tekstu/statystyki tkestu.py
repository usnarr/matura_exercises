dane=open('tekst.txt','r').readlines()

for i in range (len(dane)):
    dane[i]=dane[i].rstrip()
licznik=0
for i in dane:

    k=i.split()
    for j in range (len(k)):
        l=k[j]

        for m in range(len(l)-1):
            if l[m]==l[m+1]:
                licznik+=1
            else:continue



print(licznik)



alfabet="ABCDEFGHIJKLMNOPRSQUTYWZXV"
iloscslow=0
for i in dane:
    licznik = 0
    for j in range(len(alfabet)):
        licznik = i.count(alfabet[j])
        iloscslow+=licznik


for i in dane:
    licznik=0
    for j in range (len(alfabet)):
        licznik=i.count(alfabet[j])

        # print(licznik, alfabet[j],round(licznik/iloscslow*100,2))


samogloski="AEIOUY"
spolgloski='BCDFGHJKLMNPRSQTVXZW'

max=0
listamax=[]
for i in dane[0].split():

    podciag = ''
    for l in i:
        if  l  in spolgloski:
            podciag+=l
            if len(podciag) > max:
                max = len(podciag)
                listamax+=podciag
            if len(podciag)==4:
                print(i)
        else: podciag=''



print(max)




