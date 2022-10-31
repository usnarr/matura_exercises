dane=open("anagram.txt","r").readlines()

str(dane)
for i in range (len(dane)):
    dane[i]=dane[i].rstrip()
# print(dane)


#4.1


# for i in  dane:
#     liczbaliter = True
#     i=i.split()
#     for j in range(len(i)-1):
#         if len(i[j])!=len(i[j+1]):
#             liczbaliter=False
#             break
#     if liczbaliter:
#         print(" ".join(i))


#4.2

# rozbijam na liste stringi
# sortuje i lacze za pomoca join
#

alfabet='abcdefghijklmnopqrstuvwxyz'


#abcd cdba dbac cbad dcba

# for i in dane:
#     tab=i.split()
#     # print(tab)
#     czyanagram=True
#     for j in range(len(tab)-1):
#         lista1 = [0] * 26
#         lista2 = [0] * 26
#         if len(tab[j])==len(tab[j+1]):
#             for x in range (len(tab[j])):
#                 indeks1=alfabet.index(tab[j][x])
#                 indeks2=alfabet.index(tab[j+1][x])
#                 lista1[indeks1]+=1
#                 lista2[indeks2]+=1
#         if lista2!=lista1 or lista1.count(0)==len(lista1):
#             czyanagram=False
#             break
#     if czyanagram==True:
#          print(tab)

for i in dane:
    czyjest = True
    tab=i.split()
    for j in range(len(tab)-1):
        tab[j]=sorted(list(tab[j]))
        tab[j+1]=sorted(list(tab[j+1]))
        if tab[j]!=tab[j+1]:
            czyjest=False
            break
    if czyjest==True:
        print(i)







