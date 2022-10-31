import math

dane=open('ciagi.txt','r').readlines()

for i in range(len(dane)):
    dane[i]=dane[i].rstrip()
# print(dane)
s="slowok"

#4.1
# for i in dane:
#     if len(i)%2==0:
#         if i[:len(i)//2]==i[len(i)//2:]:
#             print(i)

#4.2

# for i in dane:
#     czysa = True
#     k=list(i)
#     for j in range(len(k)-1):
#         if k[j]=='1' and k[j+1]=='1':
#             czysa=False
#     if czysa==True:
#         print(i)

#4.2 drugi sposob

# for i in dane:
#     if i.count('11')==0:
#         print(i)


def pierwsza (a):
    if a==2:
        return True
    if a<2:
        return False
    for i in range(2,math.ceil(math.sqrt(a)+1)):
        if a%i==0:
            return False

    