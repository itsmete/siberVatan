'''
Kullanıcıdan bir cümle alın, cümlenin başındaki ve sonundaki boşlukları kaldırın, ardından tüm harfleri küçük harfe çevirin.
Bir string içinde belirli bir karakterin kaç kez geçtiğini sayın.
Kullanıcıdan bir kelime ve bir harf alın, kelimenin içindeki o harfi kaç kez içerdiğini kontrol edin.
'''

text = str(input('Enter a Text..\n'))


stripped_text = text.strip()
casefolded_text = stripped_text.casefold()

char = str(input('Enter a word or char...\n'))


counted = casefolded_text.count(char)

print(f'There are {counted} values in the sentence from the value you entered.')

'''
Kullanıcıdan iki string alın, bu stringleri birleştirin ve tüm karakterleri küçük harfe çevirin.
İki string'i birleştirin ve ardından bir substring arayın ve konumunu bulun.
'''


str1 = str(input('Enter a string value...\n'))
str2 = str(input('Enter a another string value...\n'))

united_string = f'{str1}{str2}'

casefolded_string = united_string.casefold()

substring = str(input('Enter a Substring to search for...\n')).lower()


try:
                  substring_index = casefolded_string.index(substring)
                  print(f"The substring you're looking for is index {substring_index}")
except ValueError:
        print('No result was found with the calue of you requested in this sentence.')


#Kullanıcıdan bir cümle alın ve cümlenin içindeki kelimeleri alfabetik sıraya göre sıralayın.

sentence = str(input("Please enter a sentence...\n"))
words = sentence.split()
sorted_words = sorted(words,key=str.lower)
print(sorted_words)

#Bir string içinde belirli bir alt dizeyi (substring) arayın ve yerine başka bir alt dize ekleyin.
original_text = str(input('Enter a text..\n'))


try:
        substring_to_find = str(input('Enter the value you want to search..\n'))
        replacement_text = str('Enter the value you want to replacement')
        position = original_text.find(substring_to_find)
        new_text = original_text[:position] + replacement_text + original_text[position:]
        print(new_text)
except ValueError:
        print('No result was found with the calue of you requested in this sentence.')


#Kullanıcıdan bir kelime alın ve kelimenin içindeki tüm 'a' harflerini '@' ile değiştirin.
word = input('Enter a word..\n')
stripped_word = word.strip()
replaced_word = stripped_word.replace('a','@')
print(replaced_word)

#Kullanıcıdan bir cümle alın, cümlede geçen kelimelerin içinde en uzun olanını bulun.
sentence1 = input('Enter a sentence..\n')
stripped_sentence = sentence1.strip().split()
longest_word = max(stripped_sentence, key=len)
print(f"The longest word is '{longest_word}'")

#Bir liste oluşturun ve listenin ortasındaki elemanı bulun.
numbers = [56,23,89,45,76,32,90]
middle_element = numbers[len(numbers)//2]
print(f"The middle element is {middle_element}")

#Bir tuple oluşturun, tuplein 2. ve 4. elemanlarını yeni bir tuple olarak alın.
tuple1 = (1,2,3,4,5,6,7,8,9)
second_fourth_tuple = (tuple1[1],tuple1[3])
print(second_fourth_tuple)

#Bir set oluşturun, set içine bir sayı ekleyin, ardından bu sayıyı setden çıkarın.
set1 = set([1,2,3,4,5,6,7,8,9])
number = 10
set1.add(number)
print(set1)
set1.remove(number)
print(set1)

#Bir dict oluşturun, dicte yeni bir anahtar-değer çifti ekleyin, ardından bir anahtarı silin.
dictionary = {
        'name':'mete',
        'surname':'cakir'
}
pair = ('age','18')
dictionary[pair[0]] = pair[1]
del dictionary['key2']
print(dictionary)

#Bir liste oluşturun, listenin ortasına yeni bir sayı ekleyin.
list1 = [1,2,3,4,5,6,7,8,9]
index = len(list1) // 2
value = list1[index - 1] + list1[index] 
list1.insert(index, value)
print(list1)

#Bir liste oluşturun ve listenin ortasındaki elemanı bir tuplee ekleyin.
list2 = ['A','B','C','D','E','F','G']
mid = len(list2) // 2
item = (list2[mid], list2[mid+1])
list2.insert(mid, item)
print(list2)


#Bir set oluşturun ve setin elemanlarını içeren bir liste oluşturun, ardından bu liste elemanlarının toplamını hesaplayın.
set2 = set([5,6,7,8,9])
set_to_list = list(set2)
summed_list = sum(set_to_list)

#Bir dict oluşturun ve dictin içindeki string türündeki değerlerin karakter sayılarının toplamını bulun.
dict2= {
        'name':"Mete", 
        'surname':'Çakır'
}
total_chars = sum([len(value) for key, value in dict2.items()])
print(total_chars)

#Bir liste oluşturun ve listenin içindeki en büyük sayıyı bulun, ancak sadece aritmetik operatörler (+, -, *, /) kullanmadan yapın.
numbers2 = [5,567,-787,78,345,8765,45]
largest_num = max(numbers)
print(f'The largest number is {largest_num} in your list') 


#Bir dict oluşturun ve bu dict içindeki string türündeki değerlerin hepsini birleştirerek tek bir string elde edin.
dictionary2 = {
        'name':'mete',
        'surname':'cakir',
        'age' : 18,
        'country': 'Turkiye'
}


valuelist = []
for key,value in dictionary2.items():
        if type(value) == str:
             valuelist.append(value)

summed_strings = ''.join(valuelist)
print(summed_strings)



