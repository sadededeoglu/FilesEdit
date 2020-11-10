import os
Cad_Extension = [".dwg",".dxf"]
BackUp_Extension  = [".bak",".tmp"]
Plugin_Extension = [".crx",".plugin"]
Gis_Extension = [".gpx",".kml",".kmz"]
Font_Extension = [".fnt",".fon",".otf",".ttf"]
Settings_Extension = [".cfg",".config",".ini",".prf"]
Game_Extension = [".b",".dem",".gam",".nes",".rom",".sav"]
Database_Extension = [".accdb",".db",".dbf",".mdb",".pdb",".sql"]
Misc_Extension = [".crdownload",".ics",".msi",".part",".torrent"]
DiskImage_Extension = [".iso",".cue",".dmg",".iso",".mdf",".toast",".vcd"]
Data_Extension = [".pdf",".xls","xlsx",".pps",".ppt",".pptx",".sdf",".xlr"]
Text_Extension = [".doc",".docx",".txt",".rtf",".msg",".pages",".tex",".wpd",".wps"]
Executable_Extension = [".apk",".app",".bat",".cgi",".com",".exe",".gadget",".jar",".wsf"]
Audio_Extension = [".aif",".iff",".m3u",".m4a",".mid",".mp3",".mpa",".wav",".wma",".ogg",".aac"]
System_Extension = [".cab",".cpl",".cur",".deskthemepack",".dll",".dmp",".drv",".icns",".ico",".lnk",".sys"]
Compressed_Extension = [".7z",".cbr",".deb",".gz",".pkg",".rar",".rpm",".sitx",".tar",".tar.gz",".zip",".zipx"]
Web_Extension = [".asp",".aspx",".cer",".cfm",".csr",".css",".dcr",".htm",".html",".js",".jsp",".php",".rss",".xhtml"]
Video_Extension = [".3g2",".3gp",".asf",".avi",".flv",".m4v",".mov",".mp4",".mpg",".rm",".srt",".swf",".vob","wmv",".mkv"]
Developer_Extension = [".c",".class",".cpp",".cs",".dtd",".fla",".h",".java",".lua",".m",".pl",".py",".sh",".go",".sln",".swift",".vb",".vcxproj",".xcodeproj"]
Image_Extension = [".3dm",".3ds",".max",".obj",".bmp",".dds",".gif",".heic",".jpg",".jpeg",".png",".psd",".pspimage",".tga",".thm",".tif",".tiff",".yuv",".ai",".eps",".ps",".svg"]

Source = os.getcwd()
for File in os.listdir(Source):
	for arr in Cad_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Cad_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in BackUp_Extension:
		if File.endswith(arr):
			Target_File = Source + "/BackUp_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Plugin_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Plugin_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Gis_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Gis_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Font_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Font_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Settings_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Settings_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Game_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Game_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Database_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Database_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Misc_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Misc_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in DiskImage_Extension:
		if File.endswith(arr):
			Target_File = Source + "/DiskImage_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Data_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Data_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Text_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Text_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Executable_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Executable_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Audio_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Audio_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in System_Extension:
		if File.endswith(arr):
			Target_File = Source + "/System_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Compressed_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Compressed_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Web_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Web_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Video_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Video_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Developer_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Developer_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)

	for arr in Image_Extension:
		if File.endswith(arr):
			Target_File = Source + "/Image_Extension/"
			if not os.path.isdir(Target_File):
				os.mkdir(Target_File)
			os.rename(Source + "/" + File, Target_File + File)



