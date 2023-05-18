import json
import os
class GetDevFromMean:

    FILE= "data.json"
    def __init__(self):
        pass

    def dict_to_html_table(self,dictionary):
        # Extract the keys and arrays from the dictionary
        keys = list(dictionary.keys())
        arrays = list(dictionary.values())

        # Determine the maximum length of the arrays
        max_length = max(len(array) for array in arrays)

        # Generate the HTML table headers
        headers = "<tr><th>{}</th></tr>".format("</th><th>".join(keys))

        # Generate the HTML table rows
        rows = ""
        for i in range(max_length):
            row_data = [array[i] if i < len(array) else "" for array in arrays]
            rows += "<tr><td>{}</td></tr>".format("</td><td>".join(row_data))

        # Combine the headers and rows into an HTML table
        html_table = "<table>{}</table>".format(headers + rows)

        return html_table


    def printDev(self):
        Heading ={

                    "Class-Interval":[],
                    "Frequency":[],
                    "Class-Mark":[],
                    "fᵢxᵢ":[],
                    "|xᵢ - x̄|":[],
                    "fᵢ|xᵢ - x̄|":[]
                }
        with open(self.FILE,"r") as file:
            data= json.load(file)
            cd = data['class-difference']
            scls = data['start-class']
            freq= data['frequency']


            sum = 0.0
            sumfreq = 0.0
            list_clsmark = []
            
            for f in freq:
                clsmark = (scls+scls+cd)/2  # [  lower-class + (lower-class  +  class-diference)  ]  /  2  , this is equal to xᵢ
                Heading["Class-Interval"].append(str(scls)+"-"+str(scls+cd))
                Heading["Frequency"].append(str(f))
                Heading['Class-Mark'].append(str((scls+scls+cd)/2))
                list_clsmark.append(clsmark)
                scls+=cd                    #  updating the value of start-class by 'cd' 
                sum = sum + (clsmark * f)   #  sum      += xᵢfᵢ
                Heading["fᵢxᵢ"].append(str(clsmark * f))
                sumfreq += f                #  sumfreq  += fᵢ
            mean = sum/sumfreq              #  calc mean

            sumdis = 0.0
            index = 0
            for f in freq : 
                displacement = f * abs(list_clsmark[index] - mean ) # fᵢ|xᵢ - x̄|
                Heading["|xᵢ - x̄|"].append(str(abs(list_clsmark[index] - mean )))
                Heading["fᵢ|xᵢ - x̄|"].append(str(displacement))
                sumdis += displacement
                index += 1

            dev_from_mean = sumdis/sumfreq
            html= self.dict_to_html_table(Heading)
            with open("table.html","w") as htmlfile:
                htmlfile.writelines(str(r'<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/css/materialize.min.css" integrity="sha512-17AHGe9uFHHt+QaRYieK7bTdMMHBMi8PeWG99Mf/xEcfBLDCn0Gze8Xcx1KoSZxDnv+KnCC+os/vuQ7jrF/nkw==" crossorigin="anonymous" referrerpolicy="no-referrer" />')+str(html.encode('cp1252', errors='ignore')))
            os.system('start table.html')
            print(dev_from_mean)

    
    #print(json.dumps(data,indent=4))