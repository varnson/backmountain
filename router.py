from flask import request, Flask
from dataset import dataset
import json
def home():
    return "welcome to scikit-learn!"


def version():
    return "ver 1.0.0 by fzc"

#create dataset
#param: ds=xxxx
def createds():
    ds=request.args.get("ds", "")

    return "new ds:" + dataset.create_dataset(ds)

#list dataset
def listds():

    return "list ds:" + ','.join(dataset.list_dataset())

#add data to dataset
#param: ds=xxxx
#data:json
def adddata():
    
    ds=request.args.get("ds", "")
    datastr=request.data.decode('utf-8')
    data = json.loads(datastr)
    return "new ds:" + str(dataset.add_data(ds,json.dumps(data)))

#get ds info
#param: ds=xxxx
#return: ds name, data def, data count, last data
def dsinfo():
    ds=request.args.get("ds", "")
    return "info ds:" + dataset.info_dataset(ds)

rules=({"rule":"/", "view_func":home},
        {"rule":"/ver", "view_func":version},
        {"rule":"/createds", "view_func":createds},
        {"rule":"/listds", "view_func":listds},
        {"rule":"/adddata", "view_func":adddata, "methods":('POST',)},
        {"rule":"/dsinfo", "view_func":dsinfo})
