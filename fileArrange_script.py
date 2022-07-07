"""
Author:-Amit Verma
Email:-root.avanti@gmail.com

"""

import os
import shutil

class Arrange:

    def __init__(self,path) -> None:
        self.path=path
        self.folders=[]
       
        self.file_ext={
            "pdf":" PDFS",
            "mp3":" Music",
            "mpa":" Music",
            "ogg":" Music",
            "wav":" Music",
            "7z":" ZIP",
            "rar":" ZIP",
            "gz":" ZIP",
            "zip":" ZIP",
            "iso":" ISO",
            "mp4":" Videos",
            "3gp":" Videos",
            "avi":" Videos",
            "flv":" Videos",
            "m4v":" Videos",
            "mkv":" Videos",
            "mov":" Videos",
            "mpg":" Videos",
            "mpeg":" Videos",
            "wmv":" Videos",
            "txt":" Documents",
            "csv":" Documents",
            "doc":" Documents",
            "ppt":" Documents",
            "pptx":" Documents",
            "xls":"Documents",
            "xlsx":"Documents",
            "xml":"Documents",
            "c":" C",
            "py":" Python",
            "cpp":" CPP",
            "java":"Java",
            
            "sql":" Database",
            "apk":" Android",
            "exe":" Apps",
            "deb":" Apps",
            

            "png":" Images",
            "bmp":" Images",
            "ico":" Images",
            "jpeg":" Images",
            "jpg":" Images",
            "psd":" Images",
            "svg":" Images",
            "tif":" Images",
            "tiff":" Images"
            
            }
      

    @staticmethod
    def extension(file_path):
        """Function for returning the extension of the file"""
        ext=file_path.split(".")[-1]
        return ext

  

    def scan(self):
        """Function for moving files to respective folders"""
        for i in os.listdir(self.path):
            if os.path.isfile(i):
                if self.extension(i) not in self.folders:
                    if self.extension(i) in self.file_ext.keys():
                        try: 
                            os.mkdir(self.file_ext[self.extension(i)])

                        except:
                            pass
                        
                    else:
                        try:
                            os.mkdir("Other")
                        except:
                            pass

                    self.folders.append(self.extension(i))
                try:
                    shutil.move(i,self.file_ext[self.extension(i)])

                except KeyError as e:
                    shutil.move(i,"Other")

        print("Files Moved!!")
                    
                
                        



a=Arrange(os.getcwd())
a.scan()



    


    

