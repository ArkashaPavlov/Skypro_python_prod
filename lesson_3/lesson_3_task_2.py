from smartphone import Smartphone

catalog = [Smartphone("Shagcung","s10+", "89961232323"), 
           Smartphone("Iphone","Pro Max Hd Full Primier", "89345758494"), 
           Smartphone("Xiaomy","Red12", "89034329873"), 
           Smartphone("BananaPhone","Alter", "89961234563"),
           Smartphone("Vivo","Super Puper", "81029384329")
           ]


for i in range(0,len(catalog)):    
    print(catalog[i].wendor,"-", catalog[i].model, catalog[i].number)