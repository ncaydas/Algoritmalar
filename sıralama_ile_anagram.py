#sirala ve bul -> anagram mi?
#---ncaydas---


import time
def Anagram(s1,s2):

    start = time.clock()
    
    liste1 = list(s1)
    liste2 = list(s2)

    liste1.sort()
    liste2.sort()

    sayac=0
    sonuc = True

    while (sayac<len(liste1) and sonuc):

           if liste1[sayac]==liste2[sayac]:
               sayac+=1
           else:
               sonuc = False
    
    end = time.clock()
    gecen_sure = end - start
    print gecen_sure
    return sonuc
