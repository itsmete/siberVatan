import requests
from bs4 import  BeautifulSoup as bs





file = open('malware_names.txt','w')
file.close()

for page in range(1,32):

       url = f'https://malpedia.caad.fkie.fraunhofer.de/families/{page}'

       response = requests.get(url)
       print(response) 

       data = bs(response.text, 'html.parser')


       list_elements = bs.find_all(data,class_ = 'clickable-row')

       # print(list_elements)


       for element in list_elements:
              e = bs(str(element),'html.parser')


              children = e.findChildren(class_='os')
              for child in children:
                     td = bs(str(child),'html.parser')
                     
                     family_name = td.findChild('i')['title']
                     

              if family_name == 'Windows':
                     malware_name = bs.find(e, class_="name").text
                     

              file = open('malware_names.txt','a')
              file.write(f'{malware_name[4:]} \n')
              file.close()



