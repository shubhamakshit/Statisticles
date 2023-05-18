from FileModificationHandler import FileModified
from ReadCsv import GetDevFromMean
import os 
import json

t= GetDevFromMean()
def file_modified():
    file =  open("data.csv", "w") 
    file.truncate(0)
    file.writelines("ClASS-DIFFERENCE,10\n")
    file.writelines("START_CLASS,10\n")
    file.writelines("2\n3\n4\n")
    file.close()
    os.system('start ./moderncsv/csvopen.exe ./data.csv')
    print('over')
    fileModifiedHandler = FileModified(r"data.csv",change_data)
    fileModifiedHandler.start()

def change_data():
    file =  open("data.csv", "r") 
    data= file.readlines()
    for line in data:
        try:
            cd = int(data[0].split(',')[1].strip('\n').strip())
        except ValueError as ve:
            print("Error! check if CLASS-DIFFERNCE is a valid integer")
        except Exception as e:
            print(e)
        
        try:
            scls = int(data[1].split(',')[1].strip('\n').strip())
        except ValueError as ve:
            print("Error! check if START_CLASS is a valid integer")
        except Exception as e:
            print(e)

    freq =[]
    for x in  data[2:]:
            try:
                ft = int(x.split(',')[0].strip())
                freq.append(ft)
            except Exception as e:
                pass
        
    with open("data.json", "r") as jsonFile:
            data = json.load(jsonFile)

            data["class-difference"] = cd
            data['start-class'] = scls
            data['frequency'] = freq

            with open("data.json", "w") as jsonFile:
                json.dump(data, jsonFile)

    t.printDev()

    return False

file_modified()