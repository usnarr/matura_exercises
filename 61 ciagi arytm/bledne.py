dane=open('bledne.txt','r').readlines()

for i in range(len(dane)):
    dane[i]=dane[i].rstrip()
print(dane)

for i in dane:
    k=i.split()
    if len(k)==1:
        break
    else: continue
    roznica=0
    licznikroznic=0
    for j in range(len(k-1)):
        roznica=