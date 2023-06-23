from PIL import Image
import numpy as nump
class FileProcessor:
    def __init__(self, filePath):
        self.baseFile = Image.open(filePath) #Otwarcie zdjęcia z podanej ściezki
    def savefile(self): #Dodatkowa metoda która może zostać użyta do zapisu zdjęcia
        fileName = input("Enter file name: ")
        pathToSave = input("Enter path where to save file(leave blank to save to project folder):")
        if pathToSave == "":
            self.baseFile.save(fileName)
        else:
            self.baseFile.save(f"{pathToSave}/{fileName}")
        
    def previewimage(self): #Dodatkowe metoda która może zostać użyta do pokazania zdjęcia
        self.baseFile.show()
