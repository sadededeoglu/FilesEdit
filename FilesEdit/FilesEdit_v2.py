import os
Text_Extension = [".doc",".docx",".txt",".rtf",".msg",".pages",".tex",".wpd",".wps"]
Data_Extension = [".pdf",".xls","xlsx",".pps",".ppt",".pptx",".sdf",".xlr"]

Source = os.getcwd()
#Getcwd:İçinde bulunduğumuz klasörü döndüren bir fonksiyondur.
for File in os.listdir(Source):
#Listdir:Bir dizin içindeki dosya ve klasörleri listeleme imkanı verir. 
	if File.endswith(Text_Extension):
		Target_File = Source + "/txt_Files/"

		if not os.path.isdir(Target_File):
			os.mkdir(Target_File)
		os.rename(Source + "/" + File, Target_File + File)

	elif File.endswith(Data_Extension):
		Target_File = Source + "/ppt_Files/"

		if not os.path.isdir(Target_File):
			os.mkdir(Target_File)

		os.rename(Source + "/" + File, Target_File + File)


