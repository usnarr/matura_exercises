dane=open('sygnaly.txt','r').readlines()

for i in range(len(dane)):
    dane[i]=dane[i].rstrip()

liczbaslow=1000//40
# print(liczbaslow)

przeslanie=''
for i in range(len(dane)):

    if (i+1)%40==0:
        slowo=list(dane[i])
        przeslanie+=slowo[9]

print(przeslanie)

znaki='ABCDEFGHIJKLMNOPRSTUWVQXYZ'
maxliter=0
maxslowo=0
#
# for i in dane:
#     k=i
#     powtorki=0
#     litery=len(i)
#     if k == 'SUOLDQWISCDRFLRWHZBNTMIAPHALMNCWHVGMXOZSQNXWXSFELZVTUTILXWKCTYBQYSUAKNYJKRXDJQYHXAQGWN':
#         print('--------------------------')
#         print('--------------------------')
#         print('--------------------------')
#         print('--------------------------')
#         print('--------------------------')
#         print('--------------------------')
#
#     for j in range(len(znaki)):
#         if k.count(znaki[j])>1:
#             print(znaki[j],k.count(znaki[j]))
#             powtorki+=(k.count(znaki[j])-1)
#             # print(znaki.count(k[j]))
#
#     liczbaliter=litery-powtorki
#
#
#     if liczbaliter>maxliter:
#         maxslowo=k
#         maxliter=liczbaliter
# print(maxliter)
# print(maxslowo)



for i in dane:
    ileliter=0
    for j in znaki:
        if i.__contains__(j):
            ileliter+=1
    if ileliter > maxliter:
        maxliter=ileliter
        maxslowo=i
print(maxliter,maxslowo)


#zad 3



for i in dane:
    k=list(i)
    czyo10=True
    for j in range(len(k)):

        for l in range(len(k)):
            roznica=ord(k[j])-ord(k[l])
            if roznica<0:
                roznica=ord(k[l])-ord(k[j])
            if roznica>10:
                czyo10=False



    # if czyo10==True:
    #     print(i)




