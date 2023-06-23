from ImageEditor import ImageEditor
from ImageFileWorker import FileProcessor


while True:
    try:
        imagePath = input("Enter path of image file you want to edit: ") #Podajemy ścieżkę do obrazu która
                                                                        #przekazywana jest do klasy FileProcessor
                                                                        # w ImageFileWorker gdzie obraz jest wczytywany i przekazywany do klasy ImageEditor(preferowany format to .png)
        image = FileProcessor(imagePath)
        imageEditor = ImageEditor(image.baseFile)
        while True:
            imageToSave = imageEditor.editingoptions()

    except FileNotFoundError: #występuje jeśli nie zostanie odnaleziony plik w podanej ścieżce
        print("File not found")
    except OSError: #występuje jeśli zamiast ścieżki podamy coś innego np. fragment kodu
        print("Wrong format of path")

## Użyte biblioteki to:
# PIL - Pillow - proste konwertowanie obrazu oraz zapis dla podstawowych filtrów
# matplotlib.pyplot - do modyfikacji "mocy filtra" oraz wyswietlania obrazów po operacjach morfologicznych
# numpy - konwersja obrazu do formatu 2d array
# opencv - używane do wykonywania morfologii zdjęc, binaryzacji, wygładzania oraz nałożenia filtru












