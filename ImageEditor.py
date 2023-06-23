import ImageFileWorker
import PIL.ImageShow
import matplotlib.pyplot as matplt
from PIL import Image, ImageFilter, ImageOps
from ImageFileWorker import FileProcessor
import numpy as nump
import cv2


class ImageEditor:
    def __init__(self, image):
        self.image = image

    def editingoptions(self):
        while True:
            print("Choose what kind of editing you want to execute:\n1. Color transformation\n2. Negative"
                  "\n3. Binarization/Morphology\n4. Use filter\n5. Equalize\n6. Compress\n7. Smoothening\n8. Save ") # menu do wyboru opcji edycji
            choice = int(input(""))
            self.image = self.image.convert("RGB") #Początkowo wykonywana jest konwersja obrazu do RGB aby zapewnić kompatybilność z każdą z bibliotek
            match choice:
                case 1:
                    self.image = self.image.convert("L") #Zamiana obrazu w greyscale
                    self.image.show()
                case 2:
                    self.image = self.image.convert("L")
                    self.image = self.image.point(lambda x: 255 - x) # Nałożenie negatywu
                    self.image.show()
                case 3:
                    imgToArray = nump.asarray(self.image.convert("L")) #zamian obrazu do formatu 2d array przy konwersji barw do odcienii szarości
                    ret1, threshold1 = cv2.threshold(imgToArray, 127, 255, cv2.THRESH_BINARY) #Metoda z bilbioteki opencv do wykoania binaryzacji obrazu
                    matplt.subplot(131)
                    matplt.title("")
                    matplt.axis("off")
                    matplt.imshow(threshold1, cmap = 'gray') #Przygotowanie wyświetlenia obrazu
                    core = nump.ones((8, 8), nump.uint8)
                    matplt.figure(1, figsize=(8, 8))
                    anotherchoice = int(input("After binarization, what you want to do with picture:\n1. Erode" #SubMenu do morfologicznych modyfikacji obrazu
                                              "\n2. Open\n3. Close"))
                    if anotherchoice == 1:
                        erosion = cv2.erode(threshold1, core, iterations = 1) #Metoda z opencv do wykonania erozji obrazu
                        matplt.imshow(erosion, cmap = 'gray')
                        matplt.title("Erosion")
                        matplt.axis("off")
                        matplt.show()
                        wantToSave = str(input("Do you want to save picture(y/n)?")).lower()#Dodatkowe miejsce do zapisu dokumentu po wykonaniu erozji
                        if wantToSave == "y":
                            fileName2 = input("Enter file name:")
                            cv2.imwrite(fileName2, erosion.astype(nump.uint8))
                    if anotherchoice == 2:
                        opening = cv2.morphologyEx(threshold1, cv2.MORPH_OPEN, core,)#Metoda z opencv do wykonania otwarcia obrazu
                        matplt.imshow(opening, cmap = 'gray')
                        matplt.title("Open")
                        matplt.axis("off")
                        matplt.show()
                        wantToSave = str(input("Do you want to save picture(y/n)?")).lower()#Dodatkowe miejsce do zapisu dokumentu po wykonaniu otwarcia
                        if wantToSave == "y":
                            fileName2 = input("Enter file name:")
                            cv2.imwrite(fileName2, opening.astype(nump.uint8))
                    if anotherchoice == 3:
                        close = cv2.morphologyEx(threshold1, cv2.MORPH_CLOSE, core)#Metoda z opencv do wykonania domknięcia obrazu
                        matplt.imshow(close, cmap = 'gray')
                        matplt.title("Close")
                        matplt.axis("off")
                        matplt.show()
                        wantToSave = str(input("Do you want to save picture?")).lower()#Dodatkowe miejsce do zapisu dokumentu po wykonaniu domknięcia
                        if wantToSave == "y":
                            fileName2 = input("Enter file name:")
                            cv2.imwrite(fileName2, close.astype(nump.uint8))
                case 4:
                    imgToArray = nump.asarray(self.image)
                    gaussNoise = cv2.GaussianBlur(imgToArray, (5,5), 0) #Nałożenie filtru rozmycie gaussa
                    matplt.imshow(gaussNoise)
                    matplt.title("Gauss noise filter")
                    matplt.axis("off")
                    matplt.show()
                    wantToSave = str(input("Do you want to save picture(y/n)?")).lower()#Dodatkowe miejsce do zapisu dokumentu po nalóżeniu rozmycia gaussa
                    if wantToSave == "y":
                        fileName2 = input("Enter file name:")
                        cv2.imwrite(fileName2, cv2.cvtColor(gaussNoise.astype(nump.uint8),cv2.COLOR_RGB2BGR))#Użycie biblioteki cv2 do zapisu zdjęcia wiążę się z przestawieniem
                                                                                                             # kolorów z RGB na BGR stąd przed zapisem zdjęcia po nałożeniu filtra wykonuje podmianę koloru
                case 5:
                    equalize = ImageOps.equalize(self.image)
                    equalize.show()
                case 6:
                    quality = int(input("Value of compression(0-100)?"))
                    self.image = self.image.save("Compressed.png", quality = quality)
                case 7:
                    imgToArray = nump.asarray(self.image)
                    smoothening = cv2.medianBlur(imgToArray, 9)
                    matplt.imshow(smoothening)
                    matplt.show()
                    wantToSave = str(input("Do you want to save picture(y/n)?")).lower()
                    if wantToSave == "y":

                        cv2.imwrite("Smoothening.png", cv2.cvtColor(smoothening.astype(nump.uint8), cv2.COLOR_RGB2BGR))
                                                                                                             #Użycie biblioteki cv2 do zapisu zdjęcia wiążę się z przestawieniem
                                                                                                             # kolorów z RGB na BGR stąd przed zapisem zdjęcia po nałożeniu filtra wykonuje podmianę koloru
                case 8:
                    fileName = input("Enter file name: ")
                    pathToSave = input("Enter path where to save file(leave blank to save to project folder):")
                    if pathToSave == "":
                        self.image.save(fileName) # jesli ścieżka wprowadzona przez użytkownika jest pusta to zapis wykonuje się w folderze projektu
                    else:
                        self.image.save(f"{pathToSave}/{fileName}")# przy podaniu ścieżki podstawiana jest ona do stringa z nazwą pliku.

#Ponieważ chciałem wykorzystać kilka bibliotek w celu pokazania działania zapis zdjęcia rozbija się na osobny zapis dla zdjęć z funkcji 3,4,7 oraz zapis pod funkcją 8 dla zdjęcia edytowanego prostszymi bibliotekami.








