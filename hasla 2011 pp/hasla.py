dane=   open("hasla.txt", "r").read().split()
# odpowiedz=open("wynik.txt","w")
print(dane)

#4.a
parzyste=0
nieparzyste=0

for i in range (len(dane)):
    if len(dane[i])%2==0:
        parzyste+=1
    else:
        nieparzyste+=1

# print(" ilosc parzystych",parzyste)
# print("ilosc nieparzystych",nieparzyste)
#
# print(f"liczby parzyste {parzyste} \n ilosc nieparzystych {nieparzyste}")
# odpowiedz.write(f"liczby parzyste {parzyste} \n ilosc nieparzystych {nieparzyste}")

#4.b

def palindrom(a):
    a = str(a)
    return a == a[::-1]


for i in dane:
    if palindrom(i):
        print(i)

#4.3
tab=[]

# for i in dane:
#     tab=list(i)
#     # print(tab)
#     for j in range (len(tab)-1):
#         if ord(tab[j])+ord(tab[j+1])==220:
#             print(i)
#             break


# odpowiedz.close()