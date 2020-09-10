import os
import shutil

class Organizer:
    def __init__( self ):
        self.folders = {
            "shell scripts": [".sh"],
            "Executables": [".exe"],
            "HTML": [".html", ".htm", ".html5", ".xhtml"],
            "Stylesheets": [".css"],
            "Java": [".java"],
            "Javascript": [".js"],
            "Json": [".json"],
            "Images": [".jpeg",".jpg",".tiff",".svg",".png",".bmp",".bpg",".heif",".psd"],
            "Audios": [".aac",".aa",".dvf",".m4a",".m4p",".m4b",".mp3",".msv",".ogg",".oga",".raw",".vox",".wav",".wma"],
            "Videos": [".avi",".flv",".wmv",".mov",".mp4",".webm",".vob",".mng",".qt",".mpg",".3gp",".mpeg"],
            "GIFs": [".gif"],
            "PDFs": [".pdf"],
            "Documents":['.oxps','.epub','.pages','.csv','.docx','.doc','.fdf','.ods','.odt','.pwi','.xsn','.xps','.dotx','.docm','.dox','.rvg','.rtf','.rtfd','.wpd','.xls','.xlsx','.ppt','.pptx'],
            "Archives":['.a','.ar','.cpio','.iso','.tar','.gz','.rz','.7z','.dmg','.rar','.xar','.zip'],
            "Text":['.txt','.in','.out'],
            "Python":['.py'],
            "XML":['.xml'],
            #"Desktop ShortCuts":['.lnk'],
            "Database":['.db','.db-journal','.sqlite3'],
            "Readme": [".md"],
        }
        
        self.media = ["Images","Audios","Videos","GIFs"]
        
    def check( self, path ):
        if os.path.exists(path):
           return True
        else:
           return False
    
    def execute( self, paths, path ):
        
        for k,v in paths.items():
            old_path = r"{}/{}".format(path, k)

            if v in self.media:
               new_path = r"{}/Media/{}/{}".format(path, v, k)
               folder_path = r"{}/Media/{}".format(path, v)
               media_path = r"{}/Media".format(path)
               num = 2

            elif v[-1] == "s":
               new_path = r"{}/{}/{}".format(path, v, k)
               folder_path = r"{}/{}".format(path, v)
               num = 1

            else:
               new_path = r"{}/{} Files/{}".format(path, v, k)
               folder_path = r"{}/{} Files".format(path, v)
               num = 1

            if not os.path.exists(folder_path):
               if num == 2:
                  if not os.path.exists(media_path):
                     os.mkdir(media_path)
                  os.mkdir(folder_path)
               else:
                  os.mkdir(folder_path)

            if os.path.exists(folder_path) and os.path.exists(path):
                try:
                   shutil.move(old_path, new_path)
                except Exception as e:
                   print(e)
            return True
        
    def organize( self, path ):
        folders = self.folders

        selected_paths = dict()
        
        if self.check(path):
           files = os.listdir(path)
           
           for i in files:
               for j in folders:
                   for k in folders[j]:
                       if str(i).endswith(k):
                          selected_paths[i] = j
                       
           
           if selected_paths:
              self.execute(selected_paths, path)
              print("\'"+path+'\' folder has been organized!')
           else:
              print("\'"+path+'\' folder is already organized!')
        else:
           raise Exception(f'\'{path}\' no such directory found!')

    def organize_more( self, folders ):
        print('Organizing the folders...')
        for i in folders:
            self.organize(i)
        return True
