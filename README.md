# FilesEdit

# Proje Adı: Files_Edit

# Proje Amacı: Hedef klasörde bulunan dosyaların uzantılarına göre klasörlere toplanmasını sağlamak.

1) os kütüphanesini import ediyoruz. 
Os kütüphanesi bize işletim sistemi hakkında bilgi verir ve işletim sistemiyle ilgili işler yapmamızı sağlar.

# import os

2)Kullanacağim dizileri tanımlıyorum.

# Cad_Extension = [".dwg",".dxf"] ……

3) Getcwd fonksiyonu ile bulunduğum konumu döndürüp kaynak değişkenine eşitliyorum. 

# Source = os.getcwd()

4)Bir for döngüsü açıp Listdir fonksiyonu ile dizinin içinde bulunan dosya ve klasörleri listeliyorum.

# for File in os.listdir(Source):

5)For döngüsü kullanarak arr değişkeni ile dizilerimi listeliyorum.

# for arr in Cad_Extension:

6)İf bloğu altında endswitch fonksiyonu ile arr değişkenini kullanarak dosyaların uzantılarını kontrol ediyorum.

# if File.endswith(arr):

7)Uzantısına göre yerleşmesi gereken klasörü belirtiyorum

# Target_File = Source + "/Cad_Extension/", "/BackUp_Extension/” vb

8) if not fonksiyonu altında Path fonksiyonu ile parametre olarak verilen değerin dizin olup olmadığını kontol ediyorum.
 
# if not os.path.isdir(Target_File):

9)Mkdir fonksiyonu ile yeni bir dizin oluşmasını sağlıyorum.

# os.mkdir(Target_File)

10)Rename fonksiyonu ile dizinlerin isimlerini değiştiriyorum

# os.rename(Source + "/" + File, Target_File + File)



















