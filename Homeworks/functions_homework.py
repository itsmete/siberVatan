from random import *
# 1)Bir fonksiyon oluşturun. Emeklilik yaşını 65 olarak belirleyin. Kullanıcıdan yaşını alıp 65 yaş altındakilere emekliliğine kaç yıl kaldığını 65 yaş üstüne zaten emekli olduğunu ekrana yazdırın.

def emeklilik_hesapla(yas:int):
          emeklilik_yasi = 65
          if yas <= emeklilik_yasi:
                  print(f'Emekliliginize {emeklilik_yasi - yas} yil kadar kalmistir.')
          elif yas > emeklilik_yasi:
                  print(f'Emekliginiz uzerinden {yas - emeklilik_yasi} yil kadar gecti.')

#yas = int(input("Yasini giriniz..\n "))

#emeklilik_hesapla(yas)

#2)Bir fonksiyon oluşturun.Fonksiyon kullanıcıdan iki sayı alıp bu iki sayı arasındaki asal sayıları ekrana bastırın.




 

def asal_sayi_bulucu(sayi1,sayi2):
        
          asallar = []

          sayi1,sayi2 = abs(sayi1),abs(sayi2)
          
          
          for i in range(sayi1,sayi2):
                    asalcounter = 0
                    
                    if i == 1:
                            continue

                    for j in range (2,i-1):                              
                              if i % j == 0:
                                        asalcounter += 1

                    if asalcounter == 0:
                            asallar.append(i) 
                    
          
          return asallar


#print(asal_sayi_bulucu(1,78))

# 3)İki fonksiyon oluşturun. İki fonksiyon içinde de listeler olsun ilk fonksiyon içindeki listenin en büyük sayısını ikinci fonksiyon içindeki listenin en küçük sayısını toplayıp ekrana bastırın.                             

def func1(list):

          return max(list)
def func2(list):
           return min(list)

res = func1([1,2,3,4,5,6,7,8,9]) + func2([10,20,30,40,50,60,70])

#print(res)

#4)Bir fonksiyon oluşturun. Fonksiyon içinde bir tane liste olsun ve bu listenin ilk ve son sayısı eşitse ekrana true değilse false yazdırsın.


                    
def listfunc(list):
        
        if list[0] == list[-1]:
                return True
        else:
                return  False
        
# print(listfunc([1,2,34,5,5,5,7,1]))
        
# 5)Bir sayının palindrom sayı olup olmadığını kontrol eden fonksiyonu yazınız.
        

def palindrom_controller(sayi):
         
          sayi = str(sayi)
          if len(sayi) % 2 == 0:
                    if sayi == sayi[::-1]:
                            return f'{sayi} sayisi palindrom sayidir'
                    else:
                              return f'{sayi} sayisi palindrom sayisi degildir'
          else:
                    if sayi[: int((len(sayi)-1)/ 2  ) ] == sayi[:int((len(sayi)-1) / 2 ):-1]:
                            #print(sayi[0 : int((len(sayi)-1)/ 2  - 1) ])
                            #print(sayi[ int((len(sayi)+1) / 2 -1):-1])
                            return f'{sayi} sayisi palindrom sayidir'
                    else:
                            #print(sayi[: int((len(sayi)-1)/ 2  ) ])
                            #print(sayi[:int((len(sayi)-1) / 2 ):-1])
                            return f'{sayi} sayisi palindrom sayisi degildir'
                


print(palindrom_controller(52425))
print(palindrom_controller(5222))
                              
                                             
#6)Bir fonksiyon oluşturun. Fonksiyon içinde iki liste olsun ilk listenin çift sayılarını ikinci listenin tek sayılarını alıp yeni bir listeye ekleyin ve ekrana yazdırın.

def funclist1():
          liste  = [1,2,3,4,34,5,6,65]

          respondlist = []
          for i in liste:
                    if i % 2 == 0:
                              respondlist.append(i)
          
          return respondlist

def funclist2():
          liste  = [1,2,3,4,3,45,6,324,35,4,654,54,5,6,65]

          respondlist = []
          for i in liste:
                    if i % 2 == 1:
                              respondlist.append(i)
          
          return respondlist


res1 = [funclist1(),funclist2()]
#print(res1)

# 7)Rus ruleti oyunu yazın. Random kütüphanesi kullanarak 1-6 arasında bir sayı seçilsin ve kullanıcıdan bir sayı alsın eşit olduğunda oyun biter. 2 fonksiyon kullanarak yazabilirsiniz.




def rus_ruleti():
          

          while True:
                    mermi = randint(1,6)
                    kullanici = int(input('1-6 arasi bir rakam giriniz .. \n'))
                    
                    if kullanici < 1 or kullanici > 6:
                            print('gecerli bir deger girin')

                            continue
                    if mermi == kullanici :
                            print('Kaybettiniz')
                            break
                    else:
                            print('Sanslisiniz')
                            continue


rus_ruleti()
           