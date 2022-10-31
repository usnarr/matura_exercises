dane=open('napisy.txt','r').readlines()

for i in range (len(dane)):
    dane[i]=dane[i].rstrip()
licznik=0
for i in dane:
    k=i.split()
    if len(k[0])>=len(k[1])*3 or len(k[0])*3<=len(k[1]):
        licznik+=1
    if licznik==1:
        print(i)
print(licznik)

for i in dane:
    k=i.split()
    l=k[0]
    m=k[1]
    licznik1=0
    if len(l)<len(m):
        licznik1 = 0
        for j in range(len(l)):
            if l[j] == m[j]:
                licznik1 += 1

    if licznik1==len(k[0]):
        print(i)
max=0
for i in dane:
    k=i.split()
    licznik3=0
    l=k[0][::-1]
    m=k[1][::-1]
    if len(l)>len(m):
        g=len(m)
    else:g=len(l)
    for j in range(g):
        if l[j]==m[j]:
            licznik3+=1
        else:continue
    if licznik3>max:
        max=licznik3

print(max-1)

for i in dane:
    k=i.split()
    licznik3=0
    l=k[0][::-1]
    m=k[1][::-1]
    if len(l)>len(m):
        g=len(m)
    else:g=len(l)
    for j in range(g):
        if l[j]==m[j]:
            licznik3+=1
        else:continue
    if licznik3==16:
        print(i)



