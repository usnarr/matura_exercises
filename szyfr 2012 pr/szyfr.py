sz=open('sz.txt','r').readlines()
tj=open('tj.txt','r').readlines()
klucz1=open('klucze1.txt','r').readlines()
klucz2=open('klucze2.txt','r').readlines()

for i in range(len(sz)):
    sz[i]=sz[i].rstrip()
for i in range(len(tj)):
    tj[i]=tj[i].rstrip()
for i in range(len(klucz1)):
    klucz1[i]=klucz1[i].rstrip()
for i in range(len(klucz2)):
    klucz2[i]=klucz2[i].rstrip()

#4.1
for i in range( len(tj)):
    szyfr=''
    k1=klucz1[i]
    s=tj[i]
    for j in range (len(s)):
        wartosc1=ord(s[j])
        wartosc2=ord(k1[j%len(k1)])-64
        wartosc=wartosc1+wartosc2
        if wartosc>90:
            wartosc-=26
        szyfr+=chr(wartosc)
    # print(szyfr)

#4.2
for i in range( len(tj)):
    szyfr=''
    k2=klucz2[i]
    s=sz[i]
    for j in range (len(s)):
        wartosc1=ord(s[j])
        wartosc2=ord(k2[j%len(k2)])-64
        wartosc=wartosc1-wartosc2
        if wartosc<65:
            wartosc+=26
        szyfr+=chr(wartosc)
    print(szyfr)