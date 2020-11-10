import os

Source = os.getcwd()
#Getcwd:İçinde bulunduğumuz klasörü döndüren bir fonksiyondur.
for File in os.listdir(Source):
#Listdir:Bir dizin içindeki dosya ve klasörleri listeleme imkanı verir. 
	if File.endswith(".txt"):
		Target_File = Source + "/txt_Files/"

		if not os.path.isdir(Target_File):
			os.mkdir(Target_File)
		os.rename(Source + "/" + File, Target_File + File)

	elif File.endswith(".ppt"):
		Target_File = Source + "/ppt_Files/"

		if not os.path.isdir(Target_File):
			os.mkdir(Target_File)

		os.rename(Source + "/" + File, Target_File + File)

	elif File.endswith(".docx"):
#Bir karakter dizisinin hangi karakter dizisi ile bittiğini sorgulayabilir.
		Target_File = Source + "/docx_Files/";
#dosyanın uzantısı .txt ile bitiyor ise bulunması gereken klasör e taşır.
		if not os.path.isdir(Target_File):
#İsdir:Parametre olarak verilen öğenin bir dizin olup olmadığını sorgular.
			os.mkdir(Target_File)
#Mkdir:Yeni dizinler oluşturabilmemizi sağlar.
		os.rename(Source + "/" + File, Target_File + File)
#Rename:Dizinlerin adlarını değiştirebiliriz.
