dane=open('hasla.txt','r').readlines()

for i in range(len(dane)):
    dane[i]=dane[i].rstrip()
# print(dane)
nienumer='abcdefghijklmnoprstuyvzqxwABCDEFGHIJKLMNOPRSTUWYZXVQ'

licznik=0
for i in range(len(dane)):
    czyjest=True
    k=dane[i]
    for j in range(len(k)):
        if k[j] in nienumer:
            czyjest=False




    if czyjest==True:
        licznik+=1
# print(licznik)
#zad 2
licznik2=0
for j in range(len(dane)):
    czysaa=False
    if dane.count(dane[j])>1:
        czysaa=True
    # if czysaa==True:
    #     print(dane[j])









licznik3=0
for i in range(len(dane)):
    k=dane[i]

    for m in range(len(k)-3):
        b=sorted([ord(k[m]),ord(k[m+1]),ord(k[m+2]),ord(k[m+3])])
        if b[0]+1==b[1] and b[1]+1==b[2] and b[2]+1==b[3]:
            licznik3+=1
            break



# print(licznik3)


licznik5=0


male='abcdefghijklmnoprstuyvzqxw'
duze='ABCDEFGHIJKLMNOPRSTUWYZXVQ'
numer='0123456789'
for i in range(len(dane)):
    k=dane[i]
    czynumer=False
    czymale=False
    czyduze=False
    for j in range(len(k)):
        if k[j] in numer:
            czynumer=True

    for j in range(len(k)):
        if k[j] in male:
            czymale=True

    for j in range(len(k)):
        if k[j] in duze:
            czyduze=True

    if czynumer==True and czymale==True and czyduze:
        licznik5+=1


print(licznik5)