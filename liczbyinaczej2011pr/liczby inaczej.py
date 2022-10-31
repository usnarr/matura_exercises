dane=open('liczby.txt','r').readlines()

for i in range( len(dane)):
   dane[i]=dane[i].rstrip()
# print(dane)

# 4.1
# licznik=0
# for i in dane:
#    if i[-1:]=='0':
#       licznik+=1
# print(licznik)


# #4.2
#
# max=0
# max1=str()
# for i in dane:
#    if int(i,2)>max:
#        max=int(i,2)
#        max1=i
#
# print(max,max1)

# #4.3
# licznik=0
# sumaliczb=0
# for i in dane:
#    if len(i)==9:
#       sumaliczb+=int(i,2)
#       licznik+=1
# wynik=bin(sumaliczb)
#
# print(licznik,wynik)