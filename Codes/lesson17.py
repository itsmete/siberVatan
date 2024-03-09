#kullanıcıdan alınan bir kelimenin palindrom olup olmadığını kontrol eden fonksiyon


'''
def palindrom_controller(kw : str):
       kw = kw.lower()
       return kw == kw[::-1]    
'''    


#verilen iki listesideki ortak elemanları bulan donksiyonu yazınız

'''
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]


def liste_ortaklayici(list1,list2):

       ortaklar = []
       for i in list1:
              for j in list2 :
                     if i == j:
                            ortaklar.append(i)
       
       return ortaklar


print (liste_ortaklayici(list1,list2))
'''

'''
d={"isim":"ali","soyisim":"demirci"}


x = 'ali'

for i in d.keys():
       if d[i] == x:
              print(i)
'''

#verilen bir listedeki her bir elemanının frekansını bulan bir fonksiyon yazınız

x = [1,2,2,3,4,4,4,5,5,6,6,7,7,8,9]


def frequency_controller(liste : list):
       setted_list = set(liste)
       for i in setted_list:
              sayac = 0
              for j in liste:
                     if i == j:
                            sayac +=1

              print(f'{i} elemanı listede {sayac} kadar var.') 


frequency_controller(x)

