import glob
import xml.etree.ElementTree as ET

fish_dict = {
        "Dascyllus Reticulatus": 0,
        "Chaetodon Lununatus": 1,
        "Pempheris Vanicolensis": 2,
        "Dascyllus Aruanus": 3,
        "Plectrogly-Phidodon Dickii": 4,
        "Amphiprion Clarkii": 5,
        "Chaetodon Trifascialis": 6,
        "Acanthurus Nigrofuscus": 7,
        "Chromis Chrysura": 8,
        "Hemigumnus Malapterus": 9,
        "Myripristis Kuntee": 10,
        "Chaetodon Speculum": 11,
        "Abudefduf Vaigiensis": 12,
        "Neoglyphidodon Nigroris": 13,
        "Zebrasoma Scopas": 14,
        }

for xml_file in glob.glob("./xml-files/vid20.xml"):
    tree = ET.parse(xml_file)
    vid_num = xml_file.split("/")[2].split('.')[0]
    root = tree.getroot()
    for ele in root.findall("./frame"):
        print("Frame:", ele.attrib["id"])
        file_name = "./text-file-norm/video20/" + vid_num + "_" 
        file_name += "frame" + ele.attrib["id"] + ".txt"
        with open(file_name, "w") as file:
            for child in ele:
                class_name = fish_dict[child.attrib["fish_species"]]
                x = int(child.attrib["x"])
                y = int(child.attrib["y"])
                w = int(child.attrib["w"])
                h = int(child.attrib["h"])
                w_img = 320
                h_img = 240
                x = (x + w/2) / w_img
                y = (y + h/2) / h_img
                w = w / w_img
                h = h / h_img
                line = str(class_name) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                line += "\n"
                file.writelines(line)
                print(line)
        file.close()
