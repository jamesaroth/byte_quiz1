# from arepldump import dump
import json

def readcurrency(filename):
    result = []
    with open(filename,'r') as f:
        for line in f:
            x = line.split()
            d = {"symbol" : x[0], "rate" : x[1]}
            result.append(d)
        return result

def save(output_file, data):
    with open(output_file,'w+') as file_object:
        d = {"data" : data}
        json.dump(d, file_object, indent=2)
    return

save("currency.json", readcurrency("currency.txt"))
        
        
        




        # new_d = {"symbol" + k : "rate" for k, v in d.items():
        # new_e = ("Symbol : {0}, Rate : {1}".format(k, v))
        

        # for i in ccy_data:

