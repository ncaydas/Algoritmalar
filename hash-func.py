def cirpi_fonksiyonu(csv_dosyasi):
    
    import csv

    # Ogrenci listemiz
    csv_dosyasi = 'algoritmalar_2014_ogrenci_listesi.csv'

    # cirpi fonksiyonu icin hazir alfabemiz
    alfabe = 'abcdefghijklmnopqrstuvwxyz'

    #sonuc listemiz(cirpma_sonuclari) sozluk(hash) turunde tanimlandi
    cirpma_sonuclari = dict()

    cirpma_degeri = 0

    i = 0
    for row in csv.reader(open(csv_dosyasi)):
        d = 1
        for col in row:
            #hedeflenen mukemmel cirpi islevi
            cirpma_degeri += ord(col[0])*(d**5 ) * alfabe.find(col[len(col)-1])*(d**3) + ord(col[len(col)-2])*(d**2)
            d = d + 3 # her seferinde farkli degisim(d) kullan
        cirpma_sonuclari[i] = cirpma_degeri % 150
        i = i + 1
    print cirpma_sonuclari
    return cirpma_sonuclari



def nekadar_farklilar(cirpma_sonuclari):
    uzunluk = len(cirpma_sonuclari)

    for i in range(0, uzunluk):
        for j in range(0, uzunluk):
            if not(i==j):
                if (cirpma_sonuclari[i] == cirpma_sonuclari[j]):
                    cirpma_sonuclari[j] = -1
    farklilarin_sayisi = 0
    for i in range(0, uzunluk):
        if (cirpma_sonuclari[i] != -1):
            farklilarin_sayisi = farklilarin_sayisi + 1

    print '\nyerlesen farkli sayisi:', farklilarin_sayisi
    print 'Basari Orani : % ', ((farklilarin_sayisi * 100)/uzunluk)

#Python shell ekraninda: nekadar_farklilar(cirpi_fonksiyonu(''))  yazarak test edilebilir...
#ogrenci listesi ve program ayni dizinde kayitli olmalidir.
