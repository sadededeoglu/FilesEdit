import os
import shutil

Text_Extension = [".doc",".docx",",.log",".odt",".txt",".rtf",".msg",".pages",".tex",".wpd",".wps"]
Data_Extension = [".pdf",".xls","xlsx",".cvs",".ini",".dat",".ged",".key",".keychain",".pps",".ppt",".pptx",".sdf",".xlr"]
Audio_Extension = [".aif",".iff",".m3u",".m4a",".mid",".mp3",".mpa",".wav",".wma",".ogg",".aac"]
Video_Extension = [".3g2",".3gp",".asf",".avi",".flv",".m4v",".mov",".mp4",".mpg",".rm",".srt",".swf",".vob","wmv",".mkv"]
Image_Extension = [".3dm",".3ds",".max",".obj",".bmp",".dds",".gif",".heic",".jpg",".jpeg",".png",".psd",".pspimage",".tga",".thm",".tif",".tiff",".yuv",".ai",".eps",".ps",".svg"]
Database_Extension = [".accdb",".db",".dbf",".mdb",".pdb",".sql"]
Executable_Extension = [".apk",".app",".bat",".cgi",".com",".exe",".gadget",".jar",".wsf"]
Game_Extension = [".b",".dem",".gam",".nes",".rom",".sav"]
Cad_Extension = [".dwg",".dxf"]
Gis_Extension = [".gpx",".kml",".kmz"]
Web_Extension = [".asp",".aspx",".cer",".cfm",".csr",".css",".dcr",".htm",".html",".js",".jsp",".php",".rss",".xhtml"]
Plugin_Extension = [".crx",".plugin"]
Font_Extension = [".fnt",".fon",".otf",".ttf"]
System_Extension = [".cab",".cpl",".cur",".deskthemepack",".dll",".dmp",".drv",".icns",".ico",".lnk",".sys"]
Settings_Extension = [".cfg",".config",".ini",".prf"]
Compressed_Extension = [".7z",".cbr",".deb",".gz",".pkg",".rar",".rpm",".sitx",".tar",".tar.gz",".zip",".zipx"]
DiskImage_Extension = [".iso",".cue",".dmg",".iso",".mdf",".toast",".vcd"]
Developer_Extension = [".c",".class",".cpp",".cs",".dtd",".fla",".h",".java",".lua",".m",".pl",".py",".sh",".go",".sln",".swift",".vb",".vcxproj",".xcodeproj"]
BackUp_Extension  = [".bak",".tmp"]
Misc_Extension = [".crdownload",".ics",".msi",".part",".torrent"]

path = input("Enter the path to organize : ")

for i in os.listdir(path):
    if os.path.isfile(path+"/"+i):
        filename,extension = os.path.splitext(i)
        extension = extension.lower()
        if extension in Text_Extension:
            if os.path.exists(path+"/TextFiles"):
                shutil.move(path +"/"+i,path+"/TextFiles/"+i)
            else:
                os.mkdir(path+"/TextFiles")
                shutil.move(path+"/"+i,path+"/TextFiles/"+i)

        elif extension in Data_Extension:
            if os.path.exists(path+"/DataFiles"):
                shutil.move(path+"/" + i,path+"/DataFiles/"+i)
            else:
                os.mkdir(path+"/DataFiles")
                shutil.move(path +"/" + i,path+"/DataFiles/"+i)

        elif extension in Audio_Extension:
            if os.path.exists(path+"/AudioFiles"):
                shutil.move(path+"/" + i, path+"/AudioFiles/"+i)
            else:
                os.mkdir(path+"/AudioFiles")
                shutil.move(path +"/" + i, path+"/AudioFiles/"+i)

        elif extension in Video_Extension:
            if os.path.exists(path+"/VideoFiles"):
                shutil.move(path+"/" + i, path+"/VideoFiles/"+i)
            else:
                os.mkdir(path+"/VideoFiles")
                shutil.move(path +"/" + i, path+"/VideoFiles/"+i)

        elif extension in Image_Extension:
            if os.path.exists(path+"/ImageFiles"):
                shutil.move(path+"/" + i, path+"/ImageFiles/"+i)
            else:
                os.mkdir(path+"/ImageFiles")
                shutil.move(path +"/" + i, path+"/ImageFiles/"+i)

        elif extension in Database_Extension:
            if os.path.exists(path+"/DatabaseFiles"):
                shutil.move(path+"/" + i, path+"/DatabaseFiles/"+i)
            else:
                os.mkdir(path+"/DatabaseFiles")
                shutil.move(path +"/" + i, path+"/DatabaseFiles/"+i)

        elif extension in Executable_Extension:
            if os.path.exists(path+"/ExecutableFiles"):
                shutil.move(path+"/" + i, path+"/ExecutableFiles/"+i)
            else:
                os.mkdir(path+"/ExecutableFiles")
                shutil.move(path +"/" + i, path+"/ExecutableFiles/"+i)

        elif extension in Game_Extension:
            if os.path.exists(path+"/GameFiles"):
                shutil.move(path+"/" + i, path+"/GameFiles/"+i)
            else:
                os.mkdir(path+"/GameFiles")
                shutil.move(path +"/" + i, path+"/GameFiles/"+i)

        elif extension in Cad_Extension:
            if os.path.exists(path+"/CadFiles"):
                shutil.move(path+"/" + i, path+"/CadFiles/"+i)
            else:
                os.mkdir(path+"/CadFiles")
                shutil.move(path +"/" + i, path+"/CadFiles/"+i)

        elif extension in Gis_Extension:
            if os.path.exists(path+"/GisFiles"):
                shutil.move(path+"/" + i, path+"/GisFiles/"+i)
            else:
                os.mkdir(path+"/GisFiles")
                shutil.move(path +"/" + i, path+"/GisFiles/"+i)

        elif extension in Web_Extension:
            if os.path.exists(path+"/WebFiles"):
                shutil.move(path+"/" + i, path+"/WebFiles/"+i)
            else:
                os.mkdir(path+"/WebFiles")
                shutil.move(path +"/" + i, path+"/WebFiles/"+i)

        elif extension in Plugin_Extension:
            if os.path.exists(path+"/PluginFiles"):
                shutil.move(path+"/" + i, path+"/PluginFiles/"+i)
            else:
                os.mkdir(path+"/PluginFiles")
                shutil.move(path +"/" + i, path+"/PluginFiles/"+i)

        elif extension in Font_Extension:
            if os.path.exists(path+"/FontFiles"):
                shutil.move(path+"/" + i, path+"/FontFiles/"+i)
            else:
                os.mkdir(path+"/FontFiles")
                shutil.move(path +"/" + i, path+"/FontFiles/"+i)

        elif extension in System_Extension:
            if os.path.exists(path+"/SystemFiles"):
                shutil.move(path+"/" + i, path+"/SystemFiles/"+i)
            else:
                os.mkdir(path+"/SystemFiles")
                shutil.move(path +"/" + i, path+"/SystemFiles/"+i)

        elif extension in Settings_Extension:
            if os.path.exists(path+"/SettingsFiles"):
                shutil.move(path+"/" + i, path+"/SettingsFiles/"+i)
            else:
                os.mkdir(path+"/SettingsFiles")
                shutil.move(path +"/" + i, path+"/SettingsFiles/"+i)

        elif extension in Compressed_Extension:
            if os.path.exists(path+"/CompressedFiles"):
                shutil.move(path+"/" + i, path+"/CompressedFiles/"+i)
            else:
                os.mkdir(path+"/CompressedFiles")
                shutil.move(path +"/" + i, path+"/CompressedFiles/"+i)

        elif extension in DiskImage_Extension:
            if os.path.exists(path+"/DiskImageFiles"):
                shutil.move(path+"/" + i, path+"/DiskImageFiles/"+i)
            else:
                os.mkdir(path+"/DiskImageFiles")
                shutil.move(path +"/" + i, path+"/DiskImageFiles/"+i)

        elif extension in Developer_Extension:
            if os.path.exists(path+"/DeveloperFiles"):
                shutil.move(path+"/" + i, path+"/DeveloperFiles/"+i)
            else:
                os.mkdir(path+"/DeveloperFiles")
                shutil.move(path +"/" + i, path+"/DeveloperFiles/"+i)

        elif extension in BackUp_Extension:
            if os.path.exists(path+"/BackUpFiles"):
                shutil.move(path+"/" + i, path+"/BackUpFiles/"+i)
            else:
                os.mkdir(path+"/BackUpFiles")
                shutil.move(path +"/" + i, path+"/BackUpFiles/"+i)

        else:
            if os.path.exists(path+"/MiscFiles"):
                shutil.move(path+"/" + i, path+"/MiscFiles/"+i)
            else:
                os.mkdir(path+"/MiscFiles")
                shutil.move(path +"/" + i, path+"/MiscFiles/"+i)


print("Organizer done !")