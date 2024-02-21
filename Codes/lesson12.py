# #LESSON12

# def hesaplamasaatlik(saat : int):
       
#        if saat <= 40:
#               odeme = saat* 50

#        if saat >40 :
#               ilkodeme = saat * 40
#               mesailiodeme = (saat-40) * (50 * 1.5)
#               odeme = ilkodeme + mesailiodeme
       
#        return odeme


# def hesaplamakomisyon(ayliksatis : int):
#        ayliksatisinodeme = ayliksatis * 0.05
#        odeme = 500 + ayliksatisinodeme
#        return odeme



     
# def karsilama():
       
#        print('Odeme sistemine hosgeldinizz..')  
#        print('1 - SAATLIK ISCI    2 - KOMISYONLU ISCI')  
#        odemekodu = int(input('Odeme kodunu giriniz..'))

#        if odemekodu == 1:
#               calisilansaat = int(input('Calisma saatinizi giriniz..'))
#               odeme = hesaplamasaatlik(calisilansaat)
#               print(f'Maasiniz {odeme} TL ...')
       
#        if odemekodu == 2:
#               ayliksatis = int(input('Aylik satisinizi giriniz..'))
#               odeme = hesaplamakomisyon(ayliksatis)
#               print(f'Maasiniz {odeme} TL ...')
       
#        else:
#               raise ValueError()


# def iterate_karsilama():
#        try:
#               karsilama()

#        except ValueError:
#               print('Lutfen gecerli bir deger girin')
#               iterate_karsilama()


# iterate_karsilama()






sicaklik_degerleri = [5,-15,25,12,2,30,18,-5,-35,-18-8]



def sicaklik_ayiraci(sicaklik_list : list):

       tempatures = {
              '(-20) - 0' : [],
              '0 - (+20)' : [],
              '(+20) - (+40)' : [],
       }
       

       for sicaklik in sicaklik_list:
              
              if sicaklik < 0 and sicaklik > -20:
                     tempatures['(-20) - 0'].append(sicaklik)
              
              if sicaklik > 0 and sicaklik < 20:
                     tempatures['0 - (+20)'].append(sicaklik)
              if sicaklik >20 and sicaklik < 40:
                     tempatures['(+20) - (+40)'].append(sicaklik)
       

       return tempatures


temp_dict = sicaklik_ayiraci(sicaklik_degerleri)
print(f"-20 ile 0 arasinda {len(temp_dict['(-20) - 0'])} deger var.Sicaklik degerleri :{temp_dict['(-20) - 0']}")
print(f"0 ile +20 arasinda {len(temp_dict['0 - (+20)'])} deger var.Sicaklik degerleri :{temp_dict['0 - (+20)']}")
print(f"+20 ile +40 arasinda {len(temp_dict['(+20) - (+40)'])} deger var.Sicaklik degerleri :{temp_dict['(+20) - (+40)']}")



