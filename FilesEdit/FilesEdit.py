import os, os.path

Source = os.getcwd();

Files = os.listdir(Source);
for File in Files:
	if File.endswith(".txt"): 
		Target_File = Source + "/txt_Files/";

		if not os.path.isdir(Target_File):
			os.mkdir(Target_File)
		
			os.rename(Source + "/" + File, Target_File + File);

	if File.endswith(".ppt"):
		Target_File = Source + "/ppt_Files/";

		if not os.path.isdir(Target_File):
			os.mkdir(Target_File)

		os.rename(Source + "/" + File, Target_File + File);

	if File.endswith(".docx"):

		Target_File = Source + "/docx_Files/";
		if not os.path.isdir(Target_File):

			os.mkdir(Target_File)

		os.rename(Source + "/" + File, Target_File + File);
