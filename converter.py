# from arepldump import dump

def readcurrency(filename):
    result = []
    with open(filename,'r') as f:
        for line in f:
            x = line.split()
            d = {"symbol" : x[0], "rate" : x[1]}
            result.append(d)
        return d

def save(filename, data):


print(readcurrency("currency.txt"))



        # new_d = {"symbol" + k : "rate" for k, v in d.items():
        # new_e = ("Symbol : {0}, Rate : {1}".format(k, v))
        

        # for i in ccy_data:

