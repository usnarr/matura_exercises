dane=open('napisy.txt','r').readlines()

for i in range (len(dane)):
    dane[i]=dane[i].rstrip()

# print(dane)


#4.1
licznik1=0
for i in dane:
    if len(i)%2==0:
        licznik1+=1
print(licznik1)

print('zad2 ')
#4.2
licznik2=0
for i in dane:
    if i.count('0')==i.count('1'):
        licznik2+=1
print(licznik2)

#4.3
licznikzera=0
licznikjedynek=0
print('zad 3')
for i in dane:
    if i.count('0')==len(i):
        licznikzera+=1
    if i.count('1')==len(i):
        licznikjedynek+=1
print(licznikjedynek)
print(licznikzera)
k=2
licznikliczb2=0
licznikliczb3=0
licznikliczb4=0
licznikliczb5=0
licznikliczb6=0
licznikliczb7=0
licznikliczb8=0
licznikliczb9=0
licznikliczb10=0
licznikliczb11=0
licznikliczb12=0
licznikliczb13=0
licznikliczb14=0
licznikliczb15=0
licznikliczb16=0
print('zad 4')
for i in  dane:
    if len(i)==2:
        licznikliczb2+=1
print(licznikliczb2)

for i in  dane:
    if len(i)==3:
        licznikliczb3+=1
print(licznikliczb3)
for i in  dane:
    if len(i)==4:
        licznikliczb4+=1
print(licznikliczb4)
for i in  dane:
    if len(i)==5:
        licznikliczb5+=1
print(licznikliczb5)
for i in  dane:
    if len(i)==6:
        licznikliczb6+=1
print(licznikliczb6)
for i in  dane:
    if len(i)==7:
        licznikliczb7+=1
print(licznikliczb7)
for i in  dane:
    if len(i)==8:
        licznikliczb8+=1
print(licznikliczb8)
for i in  dane:
    if len(i)==9:
        licznikliczb9+=1
print(licznikliczb9)
for i in  dane:
    if len(i)==10:
        licznikliczb10+=1
print(licznikliczb10)
for i in  dane:
    if len(i)==11:
        licznikliczb11+=1
print(licznikliczb11)
for i in  dane:
    if len(i)==12:
        licznikliczb12+=1
print(licznikliczb12)
for i in  dane:
    if len(i)==13:
        licznikliczb13+=1
print(licznikliczb13)
for i in  dane:
    if len(i)==14:
        licznikliczb14+=1
print(licznikliczb14)
for i in  dane:
    if len(i)==15:
        licznikliczb15+=1
print(licznikliczb15)
for i in  dane:
    if len(i)==16:
        licznikliczb16+=1
print(licznikliczb16)



