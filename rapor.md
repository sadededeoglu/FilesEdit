# FilesEdit

Proje Amacı: Hedef klasörde bulunan dosyaların uzantılarına göre klasörlere toplanmasını sağlamak.

1) os kütüphanesini import ediyoruz. 
Os kütüphanesi bize işletim sistemi hakkında bilgi verir ve işletim sistemiyle ilgili işler yapmamızı sağlar.

import os

2) Getcwd fonksiyonu ile bulunduğum konumu döndürüp kaynak değişkenine eşitliyorum. 

Source = os.getcwd()

3)Bir for döngüsü açıp Listdir fonksiyonu ile dizinin içinde bulunan dosya ve klasörleri listeliyorum.

for File in os.listdir(Source):

4)Endswitch fonksiyonu ile dosyaların uzantılarını İf bloğu altında kontrol ediyorum

if File.endswith(".txt”, “.apk",".app",".bat",".cgi"…. vb):

5)Uzantısına göre yerleşmesi gereken klasörü belirtiyorum

Target_File = Source + "/txt_Files/", "/ppt_Files/"….vb

6) if not fonksiyonu altında Path fonksiyonu ile parametre olarak verilen değerin dizin olup olmadığını kontol ediyorum.
 
if not os.path.isdir(Target_File):

7)Mkdir fonksiyonu ile yeni bir dizin oluşmasını sağlıyorum.

os.mkdir(Target_File)

8)Rename fonksiyonu ile dizinlerin isimlerini değiştiriyorum

os.rename(Source + "/" + File, Target_File + File)
