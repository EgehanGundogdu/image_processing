import json
import shutil
import requests
import os
pwd_path = os.getcwd()
os.mkdir(pwd_path+'/photos')

# json dosyasında veriler okundu. Python-Json dönüsümü yapıldı.
with open('fotos.json', 'r', encoding='utf-8') as file:
    json_foto = json.load(file)

#Links.txt dosyasına linkler alt alta gelecek sekilde yazıldı.
with open('links.txt', 'w', encoding='utf-8') as link_file:
    for photo_link in json_foto:
        link_file.write(photo_link['frame_link'] + "\n")
# Dosya acıldı. Linkler okunuyor. Tek tek linkler üzerinde dolasılıp fotografın link elde edildi.
file1 = open('links.txt', 'r', encoding='utf-8')
links = file1.readlines()
links_length = 0
file_number = 1
while True:
    # Link replace komutu ile düzenlendi. Requests kütüphanesi kullanılarak istek atılıyor.
    link = links[links_length]
    link = link.replace('\n', '')
    req = requests.get(link, stream=True)
    # Link dönüs kodu 200 ise dosya icerigi okunup photos klasörü altına dosya olusturuluyor.
    if req.status_code == 200:
        with open('photos/photo_{}.png'.format(file_number), 'wb') as photo_file:
            shutil.copyfileobj(req.raw, photo_file)
            print('success')
            print(link)
        file_number += 1
        link += 1
    else:
        print("{} link is broken !".format(link))
    if links_length == len(links)-1:
        print('all files downloaded.')
        file1.close()
        break


