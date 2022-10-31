dane=open("dokad.txt",'r').readlines()

for i in range(len(dane)):
    dane[i]=dane[i].rstrip()
# print(dane)


klucz="LUBIMYCZYTAC"

for i in dane:
    for j in range